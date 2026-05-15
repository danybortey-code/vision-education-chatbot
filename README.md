# 👁️ Vision Education Chatbot

A Streamlit-based educational chatbot that guides users experiencing blurry vision through a structured symptom intake process and provides safe, non-diagnostic next-step recommendations.

The system combines a Large Language Model (LLM) for natural language understanding with deterministic safety guardrails to ensure urgent warning signs are always escalated appropriately.

---

## 🎯 Project Overview

This project simulates a basic vision triage assistant for patients who report blurry near or distance vision.

Users describe their symptoms in natural language, and the system:

1. Uses an LLM to extract structured clinical information.
2. Detects safety-critical warning signs.
3. Provides educational guidance.
4. Recommends either routine eye care or urgent evaluation.

The chatbot is intended for educational purposes only and does not provide medical diagnosis.

---

## 🤖 LLM Integration

Based on instructor feedback, the original rule-based prototype was upgraded to include OpenAI-powered symptom interpretation.

The `llm_utils.py` module sends the user's free-text description to an LLM and returns structured JSON with:

- Blur type (`near`, `distance`, `unknown`)
- Eye involvement (`one eye`, `both eyes`, `unknown`)
- Onset (`suddenly`, `gradually`, `unknown`)
- Red flags (`pain`, `flashes`, `floaters`)
- Urgency (`routine`, `urgent`)
- Plain-language educational explanation

### Example LLM Output

```json
{
  "blur_type": "distance",
  "eye": "unknown",
  "onset": "unknown",
  "red_flags": ["flashes"],
  "urgency": "urgent",
  "explanation": "Flashes can be a warning sign and should be evaluated urgently."
}