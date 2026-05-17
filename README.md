# 👁️ Vision Education Chatbot
### An LLM-Powered Clinical Decision-Support Prototype for Blurry Vision Triage

> A healthcare-focused generative AI application that interprets free-text descriptions of blurry vision, extracts structured clinical information using a locally hosted Large Language Model, applies deterministic safety guardrails, and provides safe, non-diagnostic educational recommendations.

---

## Table of Contents

1. Overview
2. Project Evolution
3. Clinical Motivation
4. Problem Statement
5. System Architecture
6. How It Works
7. How the LLM Works
8. Key Design Decisions
9. Key Features
10. Tech Stack
11. Project Structure
12. Prerequisites
13. Installation
14. Running the Application
15. How to Use the Chatbot
16. Testing and Validation
17. Example Clinical Scenarios
18. Limitations
19. Future Enhancements
20. Learning Outcomes
21. Author
22. Disclaimer

---

## Overview

The Vision Education Chatbot is a Streamlit-based educational application that simulates how an eye care professional gathers symptom information from a patient presenting with blurry vision.

Users describe their symptoms in natural language, and the system:

1. Uses a Large Language Model (LLM) to extract structured clinical information.
2. Detects urgent red flags such as flashes, floaters, and eye pain.
3. Applies deterministic safety rules.
4. Generates a safe educational recommendation.
5. Displays the results in a modern Streamlit interface.

The system is intended for educational use only and does not provide medical diagnosis.

---

## Project Evolution

The initial prototype relied primarily on deterministic keyword matching to identify urgent symptoms. The current version extends that prototype by integrating a locally hosted Large Language Model through Ollama, enabling the chatbot to interpret free-text symptom descriptions while preserving deterministic safety guardrails.

---

## Clinical Motivation

Blurry vision is one of the most common reasons patients seek eye care. While many cases are caused by refractive error, symptoms such as sudden onset, eye pain, flashes, or floaters may indicate urgent pathology requiring prompt evaluation.

Examples of potentially serious conditions include:

- Retinal detachment
- Acute angle-closure glaucoma
- Optic neuritis
- Posterior vitreous detachment

This project demonstrates how AI can support early symptom triage while remaining within safe educational boundaries.

---

## Problem Statement

Develop a healthcare chatbot that can:

1. Accept free-text descriptions of blurry vision.
2. Extract structured clinical information.
3. Detect urgent warning signs.
4. Provide safe educational guidance.
5. Recommend either routine or urgent follow-up.
6. Avoid making diagnoses or treatment recommendations.

---

## System Architecture

```text
User Input
    ↓
Streamlit Interface (ui.py)
    ↓
LLM Symptom Extraction (llm_utils.py)
    ↓
Ollama Local API
    ↓
Llama 3.2 Model
    ↓
Structured JSON Output
    ↓
Safety Guardrails
    ↓
Educational Recommendation
    ↓
Clinical Summary Dashboard

How It Works
Step 1 — Symptom Capture

The user describes their vision concern in natural language.

Step 2 — LLM-Based Interpretation

A locally hosted Llama 3.2 model running through Ollama analyzes the message and extracts clinically relevant fields.

Step 3 — Structured JSON Extraction

The LLM returns a JSON object containing:

blur_type
eye
onset
red_flags
urgency
explanation

Step 4 — Safety Validation

Deterministic guardrails ensure that symptoms such as pain, flashes, floaters, and sudden vision changes always trigger urgent recommendations.

Step 5 — Recommendation Generation

The system provides either:

✅ Routine eye exam guidance
🚨 Urgent in-person eye care recommendation

Step 6 — Interactive Display

Results are rendered in a polished Streamlit dashboard with a clinical summary and educational explanation.

How the LLM Works

The llm_utils.py module sends the user's symptom description to the local Ollama API:

http://localhost:11434/api/generate

The llama3.2 model is instructed to return structured JSON output.

Example Input
My distance vision is blurry and I see flashes.
Example Output
{
  "blur_type": "distance",
  "eye": "both",
  "onset": "gradually",
  "red_flags": ["flashes"],
  "urgency": "urgent",
  "explanation": "Flashes can be a warning sign and should be evaluated urgently."
}
Extracted Fields
Field	Description
blur_type	near, distance, both, unknown
eye	one eye, both eyes, unknown
onset	suddenly, gradually, unknown
red_flags	pain, flashes, floaters
urgency	routine or urgent
explanation	Plain-language educational explanation
Key Design Decisions
Hybrid AI Architecture

Combines probabilistic LLM reasoning with deterministic safety rules.

Structured JSON Output

Constrains the model to return machine-readable data for transparency and downstream processing.

Safety-First Approach

Urgent symptoms always override the LLM's recommendation.

Local Inference with Ollama

Runs entirely on the local machine, eliminating API costs and improving privacy.

Synthetic Test Data

Uses non-identifiable simulated cases instead of real patient information.

Modular Design

Separates the user interface (ui.py) from the LLM logic (llm_utils.py) for maintainability.

Key Features
🤖 Ollama-powered natural language symptom interpretation
🧠 Locally hosted Llama 3.2 model
📊 Structured clinical information extraction
🛡️ Deterministic safety guardrails
💬 Modern Streamlit user interface
✅ Consent gate and educational disclaimer
🧪 Synthetic test dataset (test_cases.csv)
🔍 Standalone LLM testing script (test_llm.py)
🌐 Public GitHub repository

Tech Stack
Component	Technology
Frontend	Streamlit
LLM Runtime	Ollama
Model	Llama 3.2
API Interface	Local REST API (requests)
Prompt Engineering	Structured JSON extraction
Testing	Synthetic CSV + standalone Python scripts
Version Control	Git & GitHub
Language	Python 3

Project Structure
vision-education-chatbot/
├── ui.py                # Streamlit application
├── llm_utils.py         # Ollama integration
├── test_llm.py          # LLM validation script
├── test_cases.csv       # Synthetic test cases
├── requirements.txt
├── README.md
├── .gitignore
└── screenshots/         # Optional UI screenshots

Prerequisites

Before running the project, ensure you have:

Python 3.10 or later
Ollama installed
The llama3.2 model downloaded
Git (optional, for cloning the repository)
Install Ollama

Download and install Ollama from:

https://ollama.com

Download the Model
ollama pull llama3.2
Installation
git clone https://github.com/danybortey-code/vision-education-chatbot.git
cd vision-education-chatbot
pip install -r requirements.txt

Running the Application
1. Start Ollama

Ensure the Ollama service is running.

2. Launch Streamlit
streamlit run ui.py
3. Open in Browser
http://localhost:8501

How to Use the Chatbot
Launch the Streamlit application.
Review and accept the educational disclaimer.
Describe your vision symptoms in natural language.
Review the extracted clinical summary.
Read the educational recommendation.
Start a new chat to analyze another case.
Example Prompts
“My near vision is blurry when reading.”
“I suddenly noticed flashes and floaters.”
“My right eye hurts and my vision is blurry.”
Testing and Validation
Synthetic Test Dataset

test_cases.csv contains representative symptom scenarios, including:

Routine refractive blur
Eye pain
Flashes and floaters
Sudden onset blur
Greetings and edge cases
Standalone LLM Test
python test_llm.py

This verifies that the local Llama 3.2 model returns valid structured JSON.

Example Clinical Scenarios
Routine Case

Input: “My near vision is blurry when reading.”

Recommendation: Schedule a routine eye examination.

Urgent Case

Input: “I suddenly noticed flashes and floaters.”

Recommendation: Seek urgent in-person eye care.

Future Enhancements
Retrieval-Augmented Generation (RAG) with ophthalmology references
Voice input
OCT report interpretation
Visual field analysis
Multimodal image uploads
Automated evaluation metrics

Learning Outcomes

This project provided hands-on experience in:

LLM integration using Ollama and Llama 3.2
Prompt engineering for structured outputs
Safety-aware healthcare AI design
Streamlit application development
Building local AI applications
Professional project documentation


GitHub: https://github.com/danybortey-code
Project Repository: https://github.com/danybortey-code/vision-education-chatbot
Disclaimer

This application is intended solely for educational purposes and should not be used as a substitute for professional medical advice, diagnosis, or treatment.