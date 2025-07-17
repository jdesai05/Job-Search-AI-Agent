from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from resume_parser import extract_text
from matcher import job_matcher
from job_scraper import fetch_jsearch_jobs
import shutil
import os
import re

app = FastAPI(title="Job Application API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def infer_query_from_resume(text: str):
    keyword_map = {
        "machine learning": "machine learning engineer",
        "deep learning": "machine learning",
        "tensorflow": "machine learning",
        "data analysis": "data analyst",
        "excel": "data analyst",
        "sql": "data analyst",
        "statistics": "data analyst",
        "java": "java developer",
        "python": "python developer",
        "flask": "python developer",
        "django": "python developer",
        "react": "frontend developer",
        "html": "frontend developer",
        "css": "frontend developer",
        "android": "android developer",
        "kotlin": "android developer",
        "flutter": "mobile app developer",
        "aws": "cloud engineer",
        "docker": "devops engineer",
        "network": "network engineer",
        "cybersecurity": "cybersecurity analyst",
    }

    text = text.lower()
    matches = []

    for keyword, role in keyword_map.items():
        if re.search(r"\b" + re.escape(keyword) + r"\b", text):
            matches.append(role)

    if matches:
        return max(set(matches), key=matches.count)
    else:
        return "software engineer"  
    
@app.post("/upload_resume")
async def upload_resume(file: UploadFile = File(...)):
    file_path = f"temp_resumes/{file.filename}"
    os.makedirs("temp_resumes", exist_ok=True)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    extracted_text = extract_text(file_path)
    os.remove(file_path)

    return {
        "filename": file.filename,
        "extracted_text": extracted_text
    }

@app.post("/match_jobs/")
async def match_jobs(file: UploadFile = File(...)):
    file_path = f"temp_resumes/{file.filename}"
    os.makedirs("temp_resumes", exist_ok=True)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    resume_text = extract_text(file_path)
    os.remove(file_path)

    inferred_query = infer_query_from_resume(resume_text)

    job_listings = fetch_jsearch_jobs(query=inferred_query, location="India", limit=10)

    matched_jobs = job_matcher(resume_text, job_listings)

    results = []
    for job, score in matched_jobs:
        job_with_score = job.copy()
        job_with_score["match_score"] = round(score * 100, 2)
        results.append(job_with_score)

    return {
        "query_used": inferred_query,
        "matches": results
    }
