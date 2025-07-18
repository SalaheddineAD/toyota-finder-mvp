# toyota-finder-mvp

This project is a Streamlit web app that helps users find their ideal Toyota car model based on various preferences. It leverages OpenAI's GPT API to intelligently match user inputs with Toyota car data and can generate AI images of selected cars using DALL·E.

---

## Features

- Filter Toyota cars by type, color, horsepower, drive type, budget, fuel type, transmission, and MPG.
- Use natural language input to describe desired car features.
- AI-powered ranking of top matching cars using OpenAI GPT models.
- Generate AI images of selected cars with DALL·E.
- Built with Streamlit for an interactive web UI.

---

## Setup and Installation

### Prerequisites

- Python 3.8 or higher
- [pip](https://pip.pypa.io/en/stable/installation/)
- OpenAI API Key (sign up at [OpenAI](https://platform.openai.com/signup))

### Steps

1. **Clone this repository:**
```bash
git clone https://github.com/your-username/find-your-ideal-toyota.git
cd find-your-ideal-toyota
```

2. **Create and activate a virtual environment:**
```bash
python -m venv venv
venv\Scripts\activate
```
3. **Install dependencies:**
```bash
pip install -r requirements.txt
```
4. **Configure environment variables:**

Create a .env file in the root directory with your OpenAI API key:
OPENAI_API_KEY=your_openai_api_key_here
5. **Run the Streamlit app:**

```bash
streamlit run app.py
```
This will open the app in your default web browser.

## Important Note: Cache Issue
If you encounter an import error similar to:

ImportError: cannot import name 'OpenAI' from 'openai'
This may be caused by stale Python cache files (.pyc) or __pycache__ directories.

To fix this issue:
Delete all __pycache__ folders and .pyc files in your project directory and inside the virtual environment’s Lib folder.

Restart your terminal, IDE, and Streamlit server.

Run the app again.
