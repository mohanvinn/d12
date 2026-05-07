import pdfplumber
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

# 🔹 Extract text from PDF
def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text


# 🔹 Clean text
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return text


# 🔹 Match Score using TF-IDF
def calculate_match(resume, jd):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume, jd])
    similarity = cosine_similarity(vectors[0], vectors[1])
    return round(similarity[0][0] * 100, 2)


# 🔹 Missing Skills
def get_missing_skills(resume, jd):
    resume_words = set(resume.split())
    jd_words = set(jd.split())

    missing = jd_words - resume_words
    return list(missing)[:20]


# 🔹 ATS Category
def ats_rating(score):
    if score < 40:
        return "❌ Poor"
    elif score < 70:
        return "⚠️ Average"
    else:
        return "✅ Strong"