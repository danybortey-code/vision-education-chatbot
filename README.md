# 👁️ Vision Education Chatbot

A Streamlit-based educational chatbot designed to guide users experiencing blurry vision (near or distance) through a structured intake process and provide safe, non-diagnostic next steps.

---

##  Project Overview

This project simulates a basic vision triage assistant. It helps users describe their symptoms and uses rule-based logic to guide them toward appropriate next steps while prioritizing safety.

The chatbot is intentionally limited in scope and does **not provide medical diagnosis**, but instead focuses on safe education and decision support.

---

##  Key Features

- Interactive chat interface built with Streamlit  
- Consent gate before use (educational disclaimer)  
- Structured intake flow:
  - Near vs distance blur  
  - One eye vs both eyes  
  - Sudden vs gradual onset  
- Safety guardrails:
  - Detects flashes, floaters, and eye pain  
  - Sudden onset automatically triggers urgent care recommendation  
- Clean, user-friendly responses designed for the general public  

---

##  Safety Design

This chatbot follows a **safety-first design**:

- Any mention of:
  - flashes  
  - floaters  
  - eye pain  
  triggers immediate urgent care guidance  

- Sudden onset of vision changes is treated as a red flag and escalated.

This ensures the system does not delay potentially serious conditions.

---

##  How It Works

The chatbot uses a **rule-based decision system** with session state tracking:

1. User describes vision problem  
2. System identifies near vs distance blur  
3. Follow-up questions collect additional context  
4. Safety rules override normal flow when necessary  
5. Output is generated:
   - Routine eye exam recommendation  
   - OR urgent care escalation  

---

##  Test Data

A synthetic dataset (`test_cases.csv`) is included to validate system behavior.

It covers:
- Routine cases (refractive blur)
- Urgent cases (flashes, floaters, sudden onset)
- Edge cases (greetings, invalid input)

This approach avoids using real patient data while still testing system reliability.

---

##  How to Run

```bash
pip install -r requirements.txt
streamlit run ui.py