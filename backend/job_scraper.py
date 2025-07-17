import requests

RAPIDAPI_KEY = "ee1701e0c1mshbc8d288772ee746p1f9ca6jsnd552f8559324"

def fetch_jsearch_jobs(query="software developer", location="India", limit=30):
    url = "https://jsearch.p.rapidapi.com/search"
    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": "jsearch.p.rapidapi.com"
    }

    jobs = []
    seen_companies = set()

    for page in range(1, 4):  # fetch up to 30 jobs
        params = {
            "query": f"{query} in {location}",
            "page": str(page),
            "num_pages": "1"
        }

        response = requests.get(url, headers=headers, params=params)

        if response.status_code != 200:
            continue

        data = response.json().get("data", [])

        for job in data:
            company = job.get("employer_name", "N/A")
            if company in seen_companies:
                continue
            seen_companies.add(company)

            jobs.append({
                "title": job.get("job_title", "N/A"),
                "company": company,
                "description": job.get("job_description", "No description"),
                "location": f"{job.get('job_city') or 'N/A'}, {job.get('job_country') or 'N/A'}",
                "employment_type": job.get("job_employment_type", "N/A"),
                "remote_type": job.get("job_is_remote", False),
                "salary": job.get("job_salary", "Not specified"),
                "date_posted": job.get("job_posted_at_datetime_utc", "Unknown"),
                "job_url": job.get("job_apply_link", "#")
            })

            if len(jobs) >= limit:
                break

        if len(jobs) >= limit:
            break

    return jobs