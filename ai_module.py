from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

def generate_suggestions(resume, jd):
    prompt = f"""
    You are an expert resume reviewer.

    Compare the resume with the job description and provide:
    1. Key improvements
    2. Missing skills
    3. Better bullet points for experience

    Resume:
    {resume}

    Job Description:
    {jd}
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return response.choices[0].message.content