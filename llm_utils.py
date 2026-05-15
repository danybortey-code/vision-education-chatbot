import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def analyze_vision_symptoms(user_message):
    prompt = f"""
Analyze this vision-related message and return ONLY valid JSON.

Message:
"{user_message}"

JSON format:
{{
  "blur_type": "near, distance, both, or unknown",
  "eye": "one eye, both eyes, or unknown",
  "onset": "suddenly, gradually, or unknown",
  "red_flags": [],
  "urgency": "routine or urgent",
  "explanation": "brief educational explanation"
}}

Rules:
- If pain, flashes, floaters, or sudden vision change are present, urgency must be urgent.
- Do not diagnose.
- Do not prescribe.
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are a cautious eye-care education assistant. Return only valid JSON."},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    content = response.choices[0].message.content
    return json.loads(content)