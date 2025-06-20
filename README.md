# 🧠 MindGuard: Your Emotional Safety & Cognitive Health Assistant

> A multi-agent AI system that detects emotional manipulation, cognitive overload, and helps you build healthier boundaries — all in one place.

---

## 🌟 What is MindGuard?

**MindGuard** is an intelligent emotional awareness assistant built with AI. It detects:

- 💔 **Emotional manipulation** (gaslighting, guilt-tripping, control)
- 🧠 **Invisible mental load** (task overwhelm, decision fatigue)
- 🧘‍♀️ **Boundary violations** (coercion, self-neglect)

It uses a **multi-agent system** powered by Google ADK and Gemini API to help users reflect, understand, and act.

---

## 🧩 Architecture: Modular Multi-Agent System

| Agent Name                | Role                                                                 |
|--------------------------|----------------------------------------------------------------------|
| 🧠 `Cognitive Load Agent` | Detects overload from journaling or to-do logs                       |
| 💬 `Message Analyzer Agent` | Scans messages for manipulation red flags                           |
| 🔁 `Pattern Detector Agent` | Tracks recurring emotional stress patterns over time                |
| 🌱 `Insight Agent`         | Summarizes your current emotional state based on agent outputs       |
| 🛡 `Boundary Coach Agent`   | Suggests healthy responses and boundaries when red flags are detected |

Each agent can be developed and improved independently.

---

## ✨ Key Features

- 🔍 Detect gaslighting, guilt-tripping, coercive language
- 🧠 Identify burnout or invisible workload
- 📊 See recurring patterns across time
- 🌱 Get emotional insights and feedback
- 🛡 Receive boundary-setting responses and reflection prompts

---

## 🚀 Demo

*Coming soon via Streamlit Cloud*

You can also run it locally by following the steps below 👇

---

## 🛠️ Local Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/rd1875/mindguard.git
cd mindguard
```

### 2. Create & Activate a Virtual Environment

```bash
python -m venv .venv
```


Then activate it based on your OS:

#### 🔹 Windows CMD:
```bash
.venv\Scripts\activate.bat
```

#### 🔹 Windows PowerShell:
```powershell
.venv\Scripts\Activate.ps1
```

#### 🔹 macOS/Linux:
```bash
source .venv/bin/activate
```

---


> 💡 If you need a  `requirements.txt`, feel free to ask.

---

### 3. Add Your API Key Securely

Create a file named `.env` in the root `mindguard/` folder:

```ini
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=your_actual_google_gemini_api_key_here
```

✅ Your `.env` file is listed in `.gitignore`, so **your API key won't be pushed** to GitHub.

---

### 4. Run the ADK Dev UI

```bash
adk web
```
or 
```bash
adk web --no-reload
```

Then open in your browser:

```
http://localhost:8000
```

From the dropdown in the top-left corner, select:

```text
mindguard_agents
```

---

## 💬 Sample Prompts to Try

```text
“I had to cook, clean, finish work, and remind everyone again.”

“If you loved me, you'd just do it.”

“You always overreact.”

“I'm tired of remembering everything while others relax.”

“You're too sensitive. It was just a joke.”
```


---

## 📁 Folder Structure

```bash
mindguard/
├── mindguard_agents/
│   ├── __init__.py
│   ├── agent.py
│   ├── cognitive_load_agent.py
│   ├── message_analyzer_agent.py
│   ├── pattern_detector_agent.py
│   ├── insight_agent.py
│   └── boundary_coach_agent.py
├── .env             # <- your private Gemini API key here
├── app.py           # optional Streamlit or FastAPI frontend
└── README.md
```

---

## 🤝 Contributing

We welcome contributors!


---



## 🌱 Inspiration

Inspired by real emotional struggles, invisible stress, and the need for reflection tools that support awareness — not judgment.

> **MindGuard** isn’t just a chatbot.  
> It’s a mirror — for emotional clarity.
