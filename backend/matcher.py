from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import re

model = SentenceTransformer("all-MiniLM-L6-v2")


def clean_text(text):
    text = re.sub(r"\n+", " ", text)                      
    text = re.sub(r"[^\w\s.,]", "", text)                 
    text = re.sub(r"\s+", " ", text)                     
    return text.lower().strip()


def job_matcher(resume_text, job_listings):
    resume_text_clean = clean_text(resume_text)
    resume_embedding = model.encode(resume_text_clean)

    similarities = []

    for job in job_listings:
        title = clean_text(job.get("title", ""))
        desc = clean_text(job.get("description", ""))
        combined_text = (title + " ") * 3 + desc  
        job_embedding = model.encode(combined_text)

        score = cosine_similarity([resume_embedding], [job_embedding])[0][0]

        job_with_score = job.copy()
        job_with_score["match_score"] = round(score * 100, 2)
        job_with_score["match_quality"] = (
            "Excellent" if score >= 0.65 else
            "Good" if score >= 0.45 else
            "Low"
        )

        similarities.append((job_with_score, score))

    matches = sorted(similarities, key=lambda x: x[1], reverse=True)
    top_matches = [match for match in matches if match[1] >= 0.35][:7]

    return top_matches
