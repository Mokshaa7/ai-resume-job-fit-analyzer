import os
import re
import nltk
from nltk.corpus import stopwords

# -----------------------------
# NLTK setup (Render-safe)
# -----------------------------

NLTK_DATA_DIR = "/tmp/nltk_data"

# Ensure NLTK knows where to look
if NLTK_DATA_DIR not in nltk.data.path:
    nltk.data.path.append(NLTK_DATA_DIR)

# Load stopwords safely (download if missing)
try:
    STOP_WORDS = set(stopwords.words("english"))
except LookupError:
    nltk.download("stopwords", download_dir=NLTK_DATA_DIR)
    STOP_WORDS = set(stopwords.words("english"))

# -----------------------------
# Text cleaning function
# -----------------------------

def clean_text(text: str) -> str:
    """
    Cleans input text by:
    - Lowercasing
    - Removing URLs, emails, special characters
    - Removing stopwords
    - Normalizing whitespace
    """

    if not text:
        return ""

    # Lowercase
    text = text.lower()

    # Remove URLs
    text = re.sub(r"http\\S+|www\\S+", " ", text)

    # Remove emails
    text = re.sub(r"\\S+@\\S+", " ", text)

    # Remove non-alphabetic characters
    text = re.sub(r"[^a-z\\s]", " ", text)

    # Tokenize & remove stopwords
    tokens = [word for word in text.split() if word not in STOP_WORDS]

    # Reconstruct text
    cleaned_text = " ".join(tokens)

    return cleaned_text.strip()
