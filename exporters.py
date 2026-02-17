import csv
import io


def questions_to_csv(data: dict) -> str:
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow([
        "ID", "Type", "Question", "Option_A", "Option_B", "Option_C", "Option_D",
        "Correct_Answer", "Model_Answer", "Key_Points", "Explanation", "Difficulty", "Topic"
    ])
    for q in data.get("mcqs", []):
        opts = q.get("options", {})
        writer.writerow([
            q.get("id"), "MCQ", q.get("question"),
            opts.get("A", ""), opts.get("B", ""), opts.get("C", ""), opts.get("D", ""),
            q.get("correct_answer"), "", "",
            q.get("explanation", ""),
            q.get("difficulty"), q.get("topic")
        ])
    for q in data.get("short_answers", []):
        writer.writerow([
            q.get("id"), "Short Answer", q.get("question"),
            "", "", "", "", "",
            q.get("model_answer"), "; ".join(q.get("key_points", [])),
            "", q.get("difficulty"), q.get("topic")
        ])
    return output.getvalue()


def badge_html(difficulty: str, q_type: str = "MCQ") -> str:
    if q_type == "Short Answer":
        return '<span class="difficulty-badge badge-short">Short Answer</span>'
    d = (difficulty or "").lower()
    css = {"easy": "badge-easy", "medium": "badge-medium", "hard": "badge-hard"}.get(d, "badge-medium")
    return f'<span class="difficulty-badge {css}">{difficulty}</span>'
