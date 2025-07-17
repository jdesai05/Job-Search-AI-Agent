from backend.job_scraper import fetch_jsearch_jobs

jobs = fetch_jsearch_jobs("machine learning engineer", "India", limit=5)

for job in jobs:
    print("🔹", job["title"])
    print("🏢", job["company"])
    print("📍", job["location"])
    print("💼", job["employment_type"])
    print("💰", job["salary"])
    print("📅", job["date_posted"])
    print("🌐", "Remote" if job["remote_type"] else "Onsite/Hybrid")
    print("🔗", job["job_url"])
    print("📄", job["description"][:150], "...")
    print("-" * 40)
