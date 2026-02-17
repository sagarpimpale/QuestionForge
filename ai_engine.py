import json
import re

import google.generativeai as genai


DIFFICULTY_INSTRUCTIONS = {
    "Balanced": "Mix difficulties: roughly equal Easy, Medium, Hard.",
    "Easy-focused": "Mostly Easy (60%) and Medium (40%) questions.",
    "Hard-focused": "Mostly Hard (60%) and Medium (40%) questions.",
    "All Easy": "All questions should be Easy.",
    "All Medium": "All questions should be Medium.",
    "All Hard": "All questions should be Hard.",
}


def build_prompt(content: str, num_mcq: int, num_short: int, difficulty_mix: str) -> str:
    diff_note = DIFFICULTY_INSTRUCTIONS.get(difficulty_mix, "Mix difficulties.")

    return f"""You are an expert educational content creator and instructional designer.

Given the course material below, generate a structured question bank with:
- {num_mcq} Multiple Choice Questions (MCQs)
- {num_short} Short Answer Questions

Difficulty instruction: {diff_note}

STRICT OUTPUT FORMAT — return ONLY valid JSON, no markdown fences, no commentary:

{{
  "mcqs": [
    {{
      "id": "MCQ_001",
      "question": "...",
      "options": {{
        "A": "...",
        "B": "...",
        "C": "...",
        "D": "..."
      }},
      "correct_answer": "A",
      "explanation": "Brief explanation why this is correct.",
      "difficulty": "Easy|Medium|Hard",
      "topic": "Topic from the course content"
    }}
  ],
  "short_answers": [
    {{
      "id": "SA_001",
      "question": "...",
      "model_answer": "A concise model answer in 2-4 sentences.",
      "key_points": ["point 1", "point 2"],
      "difficulty": "Easy|Medium|Hard",
      "topic": "Topic from the course content"
    }}
  ]
}}

COURSE MATERIAL:
---
{content[:12000]}
---

Return ONLY the JSON object. No other text."""


def call_gemini(api_key: str, prompt: str) -> dict:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(
        prompt,
        generation_config=genai.types.GenerationConfig(
            temperature=0.7,
            max_output_tokens=8192,
        )
    )
    raw = response.text.strip()
    raw = re.sub(r"^```(?:json)?\s*", "", raw)
    raw = re.sub(r"\s*```$", "", raw)
    return json.loads(raw)
