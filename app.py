import streamlit as st
from utils import extract_text_from_pdf, clean_text, calculate_match, get_missing_skills, ats_rating
from ai_module import generate_suggestions

st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

st.title("📄 AI Resume Analyzer")
st.write("Upload your resume and compare it with a job description")

# Upload + Input
uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf")
jd = st.text_area("Paste Job Description")

if st.button("Analyze Resume"):
    if uploaded_file and jd:

        # Extract text
        resume_text = extract_text_from_pdf(uploaded_file)

        # Clean text
        resume_clean = clean_text(resume_text)
        jd_clean = clean_text(jd)

        # Score
        score = calculate_match(resume_clean, jd_clean)
        missing_skills = get_missing_skills(resume_clean, jd_clean)
        ats = ats_rating(score)

        # Display results
        st.subheader(f"📊 Match Score: {score}%")
        st.subheader(f"📌 ATS Rating: {ats}")

        st.subheader("❌ Missing Skills")
        st.write(", ".join(missing_skills))

        # AI Suggestions
        with st.spinner("Generating AI suggestions..."):
            suggestions = generate_suggestions(resume_text, jd)

        st.subheader("💡 AI Suggestions")
        st.write(suggestions)

    else:
        st.warning("Please upload resume and enter job description")