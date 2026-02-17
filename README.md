# ⚡ QuestionForge — AI Question Bank Generator

> POC Assignment · Option 1: Auto Question Bank Generator

---

## What It Does

QuestionForge takes any course document (PDF, Word, or plain text) and uses **Gemini 2.5 Flash** to automatically generate:

- **MCQs** (Multiple Choice Questions) with 4 options, correct answer, and explanation
- **Short Answer Questions** with a model answer and key points
- **Difficulty tagging** — Easy / Medium / Hard per question
- **Export** — Download results as JSON or CSV

---

## Project Structure

```
questionforge/
├── main.py              # Streamlit UI & app logic
├── styles.py            # All CSS (dark theme)
├── document_parser.py   # PDF / DOCX / TXT text extraction
├── ai_engine.py         # Gemini prompt builder & API caller
├── exporters.py         # CSV export + badge HTML helpers
├── README.md            # This file
└── docs/
    └── approach.md      # Approach, assumptions & evaluation notes
```

---

## Prerequisites

| Requirement | Version |
|---|---|
| Python | 3.9+ |
| Gemini API Key | Free at [aistudio.google.com](https://aistudio.google.com/app/apikey) |

---

## Setup & Run

### 1. Clone / unzip the project

```bash
cd questionforge
```

### 2. Install dependencies

```bash
pip install streamlit google-generativeai PyPDF2 python-docx
```

### 3. Run the app

```bash
streamlit run main.py
```

The app opens at `http://localhost:8501` in your browser.

### 4. Use it

1. Paste your **Gemini API key** in the first field
2. **Upload** a course document (PDF, DOCX, or TXT — up to ~15 pages works best)
3. Set the number of MCQs and Short Answer questions using the sliders
4. Choose a **difficulty distribution** (Balanced / Easy-focused / Hard-focused / All Easy / All Medium / All Hard)
5. Click **⚡ Generate Question Bank**
6. Browse results in the MCQs and Short Answers tabs
7. **Export** as JSON or CSV from the Export tab

---

## Output Format

### JSON
```json
{
  "mcqs": [
    {
      "id": "MCQ_001",
      "question": "...",
      "options": { "A": "...", "B": "...", "C": "...", "D": "..." },
      "correct_answer": "B",
      "explanation": "...",
      "difficulty": "Medium",
      "topic": "..."
    }
  ],
  "short_answers": [
    {
      "id": "SA_001",
      "question": "...",
      "model_answer": "...",
      "key_points": ["point 1", "point 2"],
      "difficulty": "Easy",
      "topic": "..."
    }
  ]
}
```

### CSV
Columns: `ID, Type, Question, Option_A, Option_B, Option_C, Option_D, Correct_Answer, Model_Answer, Key_Points, Explanation, Difficulty, Topic`

---

## Notes

- The app sends the **first 12,000 characters** of the extracted text to the model to stay within token limits.
- Gemini 2.5 Flash is used for speed and cost-efficiency; swap to `gemini-1.5-pro` in `ai_engine.py` for richer output on complex documents.
- No data is stored — everything lives in the browser session.
