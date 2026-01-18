# 🧠 AI Resume–Job Fit Analyzer

An **AI-powered job-seeker tool** that analyzes how well a resume matches a given job description using **semantic NLP similarity** and **skill gap analysis**, and provides **actionable feedback** for improvement.

---

## 🚀 Features

- 📄 Upload a resume (PDF)
- 📝 Paste a job description
- 📊 Get a **match score (%)**
- 🧠 Uses **transformer-based semantic similarity**
- 🛠️ Identifies **matched & missing technical skills**
- 💡 Provides **clear improvement suggestions**
- 🔒 Runs **fully offline** after model download

---

## 🧠 How It Works

The system combines **two complementary approaches**:

### 1️⃣ Semantic Similarity (NLP)

- Uses a pre-trained **SentenceTransformer** (`all-MiniLM-L6-v2`)
- Converts resume and job description into vector embeddings
- Computes **cosine similarity** to measure contextual relevance

This captures **meaning**, not just keywords.

---

### 2️⃣ Skill Gap Analysis (Rule-Based)

- Uses a curated list of **technical (CS / AI / ML) skills**
- Checks which required skills appear in:
  - the job description
  - the resume
- Applies **weighted scoring** to emphasize important skills

This ensures **explainability and precision**.

---

## 🔢 Final Score Calculation

```
Final Score = 0.6 × Semantic Similarity + 0.4 × Skill Match Score
```

---

## 🎯 Target Audience

**Job seekers** applying for:

- Software Engineering roles
- AI / ML roles
- Data-related positions

> The NLP engine is domain-agnostic, but the current skill ontology is intentionally scoped to **technical roles**.

---

## 🛠️ Tech Stack

- **Python**
- **FastAPI** – backend & API
- **SentenceTransformers** – NLP embeddings
- **Scikit-learn** – cosine similarity
- **NLTK** – text preprocessing
- **Jinja2** – HTML templating
- **PDF parsing + OCR fallback** – resume extraction

---

## 📂 Project Structure

```
ai-resume-job-fit-analyzer/
│
├── backend/
│   ├── api.py
│   ├── ranker.py
│   ├── parser.py
│   ├── skills.py
│   ├── explain.py
│   ├── confidence.py
│   ├── preprocessor.py
│   └── templates/
│       └── index.html
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ▶️ Running Locally

### 1️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 2️⃣ Run the app

```bash
python -m uvicorn backend.api:app --reload
```

---

### 3️⃣ Open in browser

```
http://127.0.0.1:8000/
```

---

## 🌐 Offline Support

- The NLP model is downloaded **once**
- After caching, the app runs **fully offline**
- No external APIs are used at runtime

---

## 🔮 Future Improvements

- Support for DOCX resumes
- Multiple domain skill ontologies (non-CS roles)
- Resume improvement suggestions per section
- Cloud deployment with persistent storage

---

## 📌 Why This Project

This project demonstrates:

- Practical NLP usage (not toy examples)
- Explainable ML design
- End-to-end system thinking
- Clean separation of preprocessing, scoring, and UI
- Real-world ATS-inspired logic with a job-seeker focus

---

## 👤 Author

**Moksha Shah**  
Computer Engineering Undergraduate
Interested in NLP, ML systems, and applied AI

