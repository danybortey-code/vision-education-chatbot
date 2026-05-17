import json
import requests


def analyze_vision_symptoms(user_text):
    prompt = f"""
You are an ophthalmic triage assistant.

Analyze the patient's symptom description and return ONLY valid JSON.

Extract the following fields:
- blur_type: near, distance, both, or unknown
- eye: one eye, both eyes, or unknown
- onset: suddenly, gradually, or unknown
- red_flags: list containing any of [pain, flashes, floaters]
- urgency: routine or urgent
- explanation: brief educational explanation

Patient description:
{user_text}
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2",
            "prompt": prompt,
            "stream": False,
            "format": "json"
        },
        timeout=120
    )

    response.raise_for_status()

    result = response.json()
    return json.loads(result["response"])