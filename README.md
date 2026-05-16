# 👁️ Vision Education Chatbot
### An LLM-Powered Clinical Decision-Support Prototype for Blurry Vision Triage

The Vision Education Chatbot is a Streamlit-based educational application that simulates how an eye care professional gathers symptom information from a patient presenting with blurry vision.

The system combines:

- Large Language Models (LLMs) for natural language understanding
- Deterministic safety guardrails for urgent symptom detection
- Structured clinical reasoning
- A modern Streamlit user interface

This project demonstrates how generative AI can be used to build safe, explainable healthcare decision-support tools.

---

## Instructor Feedback Addressed

The initial prototype relied primarily on rule-based keyword matching to identify urgent symptoms. Based on instructor feedback, the project was refactored to integrate the OpenAI API, enabling the chatbot to use a Large Language Model (LLM) to interpret free-text symptom descriptions and extract structured clinical information while retaining deterministic safety guardrails.

---

## Table of Contents

1. Overview
2. Problem Statement
3. System Architecture
4. High-Level Pipeline
5. How the LLM Works
6. Safety Guardrails
7. Key Features
8. Technology Stack
9. Directory Overview
10. Testing and Validation
11. Installation
12. Environment Variables
13. Running the Application
14. Example Use Cases
15. Limitations
16. Future Enhancements
17. Learning Outcomes
18. Author
19. Disclaimer

---

## Overview

Patients often describe symptoms in free text:

> “My distance vision is blurry.”

> “I suddenly noticed flashes and floaters.”

The chatbot interprets these descriptions, extracts clinically relevant information, and provides educational next-step recommendations.

---

## Problem Statement

Build an AI-powered educational chatbot that can:

1. Accept natural language descriptions of blurry vision.
2. Extract structured symptom information.
3. Detect urgent red flags.
4. Recommend routine or urgent follow-up.
5. Avoid making diagnoses.

---

## System Architecture

```text
User Input
    ↓
Streamlit UI (ui.py)
    ↓
OpenAI LLM (llm_utils.py)
    ↓
Structured JSON Extraction
    ↓
Safety Guardrails
    ↓
Educational Recommendation
    ↓
Clinical Summary Display