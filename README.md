# MP3 — AI Resume Feedback Analyzer

This mini project is a client-server web application that compares a resume to a target job description using Together.ai.

## Overview

The user pastes a resume and a target job description into a browser-based interface. The FastAPI backend sends both inputs to Together.ai using a structured prompt. The model returns formatted feedback as text, which is then displayed in the frontend.

This project demonstrates:
- client/server architecture
- browser-based user input
- backend processing with FastAPI
- real-time LLM integration through Together.ai
- AI-assisted development and documentation

## Features

- Paste a resume into the browser
- Paste a target job description
- Send both inputs to the backend
- Receive AI-generated feedback in real time
- Display:
  - score
  - strengths
  - improvements
  - missing keywords
  - rewritten summary

## Tech Stack

- Python
- FastAPI
- Uvicorn
- Together.ai API
- HTML
- CSS
- JavaScript
- python-dotenv
- Pydantic

## Project Structure

```text
resume-review/
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   └── .env
├── frontend/
│   └── index.html
└── .gitignore
