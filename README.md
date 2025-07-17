# ✅ ResumeRadar

An intelligent, full-stack AI Agent that:
- Parses your **resume (PDF or DOCX)**
- Understands your **skills and experience**
- Recommends **relevant job listings** in real-time
- Powered by **FastAPI**, **Sentence Transformers**, and **JSearch API**

---

## 🚀 Features

- 📄 Upload your resume (PDF/DOCX)
- 🔍 Extracts keywords and skills using AI
- 🤖 Embeds your profile using `sentence-transformers`
- 🔗 Fetches jobs from JSearch API (RapidAPI)
- 📊 Ranks and matches jobs using cosine similarity
- ⚡ Built with `FastAPI` and `scikit-learn`

## 🛠️ How to Run

1. **Clone the repo**
   ```bash
   git clone https://github.com/jdesai05/Job-Search-AI-Agent.git
   cd Job-Search-Agent
   ```


**Run the FastAPI server**
   ```bash
   uvicorn main:app --reload
   ```

**Access the interface**
   Visit https://job-search-ai-agent.vercel.app/ to upload your resume and test.

---

## 📂 Project Structure

```
├── main.py              # FastAPI backend
├── scraper.py           # JSearch API scraper
├── matcher.py           # Resume embedding & matching logic
├── utils.py             # File parsing & helpers
├── requirements.txt
└── README.md
```

---

## 🔐 API Configuration

Set your **RapidAPI key** in the `scraper.py` file:

```python
headers = {
    'x-rapidapi-host': 'jsearch.p.rapidapi.com',
    'x-rapidapi-key': 'YOUR_API_KEY_HERE'
}
```

---

## 🧠 Future Enhancements

- Add cover letter generation using LLM
- Integrate email/job application automation
- Skill gap analysis and recommendations

---
