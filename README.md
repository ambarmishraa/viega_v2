<div align="center">

# 🤖 AI Market Intelligence & Decision System

**Built in 48 hours · Future BUILD DAYS 2026 · Frankfurt**

*Viega × Wisag × Techem*

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Gemini API](https://img.shields.io/badge/Gemini_API-LLM-4285F4?style=flat-square&logo=google&logoColor=white)](https://ai.google.dev/)
[![Plotly](https://img.shields.io/badge/Plotly-Visualisation-3F4F75?style=flat-square&logo=plotly&logoColor=white)](https://plotly.com/)
[![Built at Hackathon](https://img.shields.io/badge/Future_BUILD_DAYS-2026-orange?style=flat-square)](https://github.com/ambarmishraa/viega_v2)

</div>

---

## 🧠 The Problem

Product Managers at companies like Viega are overwhelmed by market signals — competitor launches, technology shifts, regulatory changes, industry movements — with no structured way to identify which signals matter or what action to take. The result: slow, manual, and subjective product decisions.

## 💡 The Solution

An LLM-powered market intelligence system that ingests raw market signals, runs them through a **multi-agent AI pipeline**, and outputs structured, actionable recommendations — so Product Managers can act fast instead of drowning in noise.

---

## 🏗️ Architecture

```
Raw Market Data (Web Scraped + Synthetic)
        ↓
  signal_engine.py  ←  Signal classification & scoring
        ↓
   pipeline.py      ←  Multi-agent pipeline
                        ├── Portfolio Strategy Agent
                        ├── Investment Mindset Agent
                        └── Risk Filtering Agent
        ↓
   Gemini API       ←  LLM reasoning & decision synthesis
        ↓
    app.py          ←  Streamlit dashboard
                        ├── BUILD / INVEST / IGNORE recommendations
                        ├── KPI dashboards
                        ├── Trend analysis
                        ├── Market structure visualisation
                        ├── Decision matrix
                        ├── Confidence & urgency scoring
                        └── Human feedback loop
```

---

## 📁 Project Structure

```
viega_v2/
├── app.py              # Streamlit UI — dashboard entry point
├── pipeline.py         # Multi-agent orchestration pipeline
├── signal_engine.py    # Signal ingestion, classification & scoring
├── data.py             # Synthetic + web-scraped data generation
├── requirements.txt    # Dependencies
└── .gitignore
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- A [Google Gemini API key](https://ai.google.dev/)

### Installation

```bash
# Clone the repository
git clone https://github.com/ambarmishraa/viega_v2.git
cd viega_v2

# Install dependencies
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_api_key_here
```

### Run

```bash
streamlit run app.py
```

---

## 📊 Screenshots

### Signal Generation

The system ingests and classifies market signals from multiple sources, scoring each by relevance, urgency, and strategic fit.

<img width="1884" alt="Signal Generation Overview" src="https://github.com/user-attachments/assets/72db136c-b574-42d0-a1d5-e7afc8dd1d8f" />

<img width="1905" alt="Signal Feed" src="https://github.com/user-attachments/assets/bb827ec4-9065-41c4-8b9f-c8b7da739e8c" />

<img width="1898" alt="Signal Classification" src="https://github.com/user-attachments/assets/7dd66c2a-6d67-4830-bcdc-58ac36bdf31f" />

<img width="1881" alt="Market Trend Analysis" src="https://github.com/user-attachments/assets/a02e5980-3549-498d-b7fe-2fa5ebcbd453" />

<img width="1870" alt="KPI Dashboard" src="https://github.com/user-attachments/assets/b3158d80-1413-46e5-9e56-b94b2ce250f3" />

<img width="1881" alt="Market Structure Visualisation" src="https://github.com/user-attachments/assets/537544cb-89da-4672-835b-0a5071f624fd" />

---

### AI Engine

The multi-agent pipeline simulates three decision perspectives — portfolio strategy, investment mindset, and risk filtering — before synthesising a final recommendation via Gemini.

<img width="1902" alt="AI Engine Pipeline" src="https://github.com/user-attachments/assets/2ccf31a8-b535-4e9e-bda0-354e8433422f" />

**Filter Options** — Slice signals by category, urgency, confidence, or market domain:

<img width="429" alt="Filter Options" src="https://github.com/user-attachments/assets/384c7f4b-77ff-4407-9ed8-0e75dbbe92cb" />

<img width="1886" alt="Decision Matrix" src="https://github.com/user-attachments/assets/d743d60b-8368-4a60-bae3-92ba887019f6" />

<img width="1888" alt="Build Invest Ignore Recommendations" src="https://github.com/user-attachments/assets/c23129cc-9b3e-4288-97e6-ef1d6911639c" />

<img width="1880" alt="Confidence and Urgency Scoring" src="https://github.com/user-attachments/assets/b46f8a75-38e4-4c4e-9f2a-8b3cfe140e07" />

<img width="1884" alt="Human Feedback Loop" src="https://github.com/user-attachments/assets/13342b9b-3551-4647-ae3a-2111576ae9d3" />

<img width="1892" alt="Final Output Summary" src="https://github.com/user-attachments/assets/7571a73a-eedf-4aa5-8d07-1bf69a724a79" />

---

## ⚙️ Tech Stack

| Layer | Technology |
|-------|-----------|
| UI & Dashboard | Streamlit |
| LLM Reasoning | Google Gemini API (`google-generativeai`, `google-genai`) |
| Visualisation | Plotly |
| Data Ingestion | Python · Web Scraping · Synthetic data generation |
| Multi-Agent Orchestration | Custom Python pipeline |
| Config | python-dotenv |

---

## 🎯 Output: What It Produces

For every market signal, the system produces:

- **BUILD** — Signals that justify building a new product feature or capability
- **INVEST** — Signals that warrant strategic investment or partnership
- **IGNORE** — Signals that are noise relative to current portfolio priorities

Each recommendation includes a **confidence score**, **urgency rating**, and an **AI-generated rationale** traceable back to the source signals.

---

## 👤 Built By

**Ambar Mishra** — M.Sc. Computer Science, TU Darmstadt

[![Portfolio](https://img.shields.io/badge/Portfolio-ambarmishra.vercel.app-black?style=flat-square&logo=vercel)](https://ambarmishra.vercel.app)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat-square&logo=linkedin)](https://linkedin.com/in/ambar-mishra-5940922b4/)
