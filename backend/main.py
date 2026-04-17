import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from together import Together

load_dotenv()

API_KEY = os.getenv("TOGETHER_API_KEY")
if not API_KEY:
    raise RuntimeError("TOGETHER_API_KEY not found in .env")

client = Together(api_key=API_KEY)

app = FastAPI(title="AI Resume Analyzer")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ResumeRequest(BaseModel):
    resume_text: str
    job_description: str


@app.get("/")
def root():
    return {"message": "backend is running"}


@app.get("/health")
def health():
    return {"status": "ok"}


def build_prompt(resume: str, job: str) -> str:
    return f"""
You are a professional resume reviewer.

Compare the resume to the job description.

Respond in THIS EXACT FORMAT:

Score: <number from 0-100>

Strengths:
- bullet point
- bullet point

Improvements:
- bullet point
- bullet point

Missing Keywords:
- keyword
- keyword

Rewritten Summary:
<write a better professional summary>

Resume:
{resume}

Job Description:
{job}
""".strip()


@app.post("/analyze")
def analyze_resume(payload: ResumeRequest):
    prompt = build_prompt(payload.resume_text, payload.job_description)

    try:
        response = client.chat.completions.create(
            model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
            messages=[
                {"role": "system", "content": "Follow formatting exactly."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.3,
            max_tokens=800,
        )

        result_text = response.choices[0].message.content
        return {"result": result_text}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))