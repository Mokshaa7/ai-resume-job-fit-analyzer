import os
import re
import nltk

# -----------------------------
# NLTK setup (Render-safe)
# -----------------------------

NLTK_DATA_DIR = "/tmp/nltk_data"

# Ensure directory exists
os.makedirs(NLTK_DATA_DIR, exist_ok=True)

# Tell NLTK where to look
if NLTK_DATA_DIR not in nltk.data.path:
    nltk.data.path.append(NLTK_DATA_DIR)

# ALWAYS ensure stopwords are available
nltk.download("stopwords", download_dir=NLTK_DATA_DIR, quiet=True)

from nltk.corpus import stopwords

STOP_WORDS = set(stopwords.words("english"))

# -----------------------------
# Text cleaning function
# -----------------------------

def clean_text(text: str) -> str:
    """
    Cleans input text by:
    - Lowercasing
    - Removing URLs and emails
    - Removing non-alphabetic characters
    - Removing English stopwords
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

    # Remove stopwords
    tokens = [word for word in text.split() if word not in STOP_WORDS]

    return " ".join(tokens).strip()
