import json
from pathlib import Path

DATA_FILE = Path("data/sample_outputs.json")
OUTPUT_FILE = Path("reports/example_report.md")


def score_response(text: str) -> dict:
    length = len(text.split())
    accuracy = 4
    clarity = 5 if length > 8 else 3
    reasoning = 4 if "because" in text.lower() or "helps" in text.lower() else 3
    tone = 5

    total = accuracy + clarity + reasoning + tone
    return {
        "accuracy": accuracy,
        "clarity": clarity,
        "reasoning": reasoning,
        "tone": tone,
        "total": total,
    }


def main() -> None:
    responses = json.loads(DATA_FILE.read_text())
    lines = ["# Evaluation Report", ""]

    for item in responses:
        scores = score_response(item["output"])
        lines.extend(
            [
                f"## {item['id']}",
                "",
                f"**Prompt:** {item['prompt']}",
                "",
                f"**Output:** {item['output']}",
                "",
                f"- Accuracy: {scores['accuracy']}",
                f"- Clarity: {scores['clarity']}",
                f"- Reasoning: {scores['reasoning']}",
                f"- Tone: {scores['tone']}",
                f"- Total: {scores['total']}/20",
                "",
            ]
        )

    OUTPUT_FILE.write_text("\n".join(lines))
    print(f"Saved report to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
