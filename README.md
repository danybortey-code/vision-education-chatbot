# 👁️ Vision Education Chatbot
### An LLM-Powered Clinical Decision-Support Prototype for Blurry Vision Triage

The Vision Education Chatbot is a Streamlit-based educational application that simulates how an eye care professional gathers symptom information from a patient presenting with blurry vision.

The system combines:

- **Large Language Models (LLMs)** for natural language understanding
- **Deterministic safety guardrails** for urgent symptom detection
- **Structured clinical reasoning**
- **A modern Streamlit user interface**

This project demonstrates how artificial intelligence can be used to build safe, explainable healthcare decision-support tools.

---

## 🎯 Project Motivation

Patients frequently describe vision problems using free text, such as:

> “My distance vision has been blurry for a few weeks.”

> “I suddenly noticed flashes and floaters in one eye.”

Interpreting these descriptions requires extracting clinically relevant features such as:

- Whether blur is worse at near or distance
- Whether one or both eyes are affected
- Whether symptoms began suddenly or gradually
- Whether urgent warning signs are present

This project automates that process using an LLM while preserving strict safety rules.

---

## ❓ Problem Statement

Develop a healthcare chatbot that can:

1. Accept free-text descriptions of blurry vision.
2. Extract structured symptom information.
3. Detect urgent red flags.
4. Provide educational guidance.
5. Recommend routine or urgent follow-up.
6. Clearly communicate that the system is **not a medical diagnosis**.

---

## 🧠 System Overview

The application follows a hybrid architecture:

1. **User enters symptoms in natural language**
2. **LLM extracts structured clinical information**
3. **Safety guardrails validate urgent symptoms**
4. **Educational recommendations are generated**
5. **Results are displayed in Streamlit**

This design combines the flexibility of LLMs with the reliability of deterministic clinical safety logic.

---

## 🏗️ System Architecture

```text
User Input
    ↓
Streamlit Interface (ui.py)
    ↓
LLM Symptom Extraction (llm_utils.py)
    ↓
Structured JSON Output
    ↓
Safety Guardrails
    ↓
Educational Recommendation
    ↓
Rendered Clinical Summary