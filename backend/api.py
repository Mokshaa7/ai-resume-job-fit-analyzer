from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from typing import List
import tempfile
import os

from backend.parser import load_resumes_from_folder
from backend.ranker import rank_resumes
from backend.preprocessor import clean_text

app = FastAPI(title="AI Resume Screener")
templates = Jinja2Templates(directory="backend/templates")

@app.post("/rank-resumes/")
async def rank_uploaded_resumes(
    job_description: str,
    resumes: List[UploadFile] = File(...)
):
    temp_dir = tempfile.mkdtemp()

    # Save uploaded resumes
    for resume in resumes:
        path = os.path.join(temp_dir, resume.filename)
        with open(path, "wb") as f:
            f.write(await resume.read())

    resumes_text = load_resumes_from_folder(temp_dir)
    ranked = rank_resumes(resumes_text, clean_text(job_description))

    return ranked


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "results": None}
    )

@app.post("/rank", response_class=HTMLResponse)
async def rank_ui(
    request: Request,
    job_description: str = Form(...),
    resumes: List[UploadFile] = File(...)
):
    temp_dir = tempfile.mkdtemp()

    for resume in resumes:
        path = os.path.join(temp_dir, resume.filename)
        with open(path, "wb") as f:
            f.write(await resume.read())

    resumes_text = load_resumes_from_folder(temp_dir)
    ranked = rank_resumes(resumes_text, clean_text(job_description))

    match_score = None
    verdict = None
    advice = None
    suggestions = []

    if ranked:
        top = ranked[0]
        match_score = round(top["final_score"] * 100, 2)

        verdict, advice, suggestions = generate_user_feedback(
            match_score,
            top["missing_core_skills"]
        )

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "match_score": match_score,
            "verdict": verdict,
            "advice": advice,
            "suggestions": suggestions
        }
    )
   

def generate_user_feedback(score, missing_skills):
    if score >= 75:
        verdict = "Strong match ✅"
        advice = "Your resume aligns well with this job description."
    elif score >= 50:
        verdict = "Moderate match ⚠️"
        advice = "Your resume matches partially, but can be improved."
    else:
        verdict = "Low match ❌"
        advice = "Your resume needs improvement to match this role."

    suggestions = []
    if missing_skills:
        suggestions.append(
            "Consider adding or highlighting these skills: "
            + ", ".join(missing_skills[:3])
        )

    return verdict, advice, suggestions
