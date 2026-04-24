from google import genai

client = genai.Client(api_key="AIzaSyDvbvNln4qdBsVZLboiFolVE8bjqeMQPYI")


# -----------------------------
# PERSONA PROMPTS
# -----------------------------

PERSONAS = {
    "portfolio": """
You are a Product Portfolio Strategist at Viega.

Decide if the company should CHANGE PRODUCT PORTFOLIO.

Focus:
- Product lines
- Market relevance
- Competitive overlap

Return STRICT JSON:
{
  "decision": "BUILD / INVEST / IGNORE",
  "confidence": 0-100,
  "reason": "...",
  "action_items": ["...","..."]
}
""",

    "investment": """
You are a Technology Investment Strategist.

Decide if Viega should INVEST IN TECHNOLOGY.

Focus:
- emerging tech
- partnerships
- long-term advantage

Return STRICT JSON:
{
  "decision": "BUILD / INVEST / IGNORE",
  "confidence": 0-100,
  "reason": "...",
  "action_items": ["...","..."]
}
""",

    "ignore": """
You are a Risk Filtering Analyst.

Decide if signals should be IGNORED.

Focus:
- noise filtering
- weak signals
- irrelevant trends

Return STRICT JSON:
{
  "decision": "BUILD / INVEST / IGNORE",
  "confidence": 0-100,
  "reason": "...",
  "action_items": ["...","..."]
}
"""
}


# -----------------------------
# SINGLE PERSONA CALL
# -----------------------------

def run_persona(persona_key, signals):

    prompt = f"""
{PERSONAS[persona_key]}

Signals:
{signals}

Return only JSON.
"""

    try:
        response = client.models.generate_content(
            model="models/gemini-2.5-flash",
            contents=prompt
        )
        return response.text
    except Exception as e:
        return {"error": str(e)}


# -----------------------------
# FINAL JUDGEMENT ENGINE
# -----------------------------

def final_judgement(portfolio, investment, ignore):

    prompt = f"""
You are the Chief Product Officer at Viega.

You will receive 3 strategic opinions:

PORTFOLIO:
{portfolio}

INVESTMENT:
{investment}

IGNORE:
{ignore}

TASK:
- Choose ONE final decision:
  BUILD / INVEST / IGNORE

- Give:
1. Final Decision
2. Reasoning
3. Action Plan (bullet points)
4. Risk if wrong decision

Be extremely precise and non-generic.
"""

    response = client.models.generate_content(
        model="models/gemini-2.5-flash",
        contents=prompt
    )

    return response.text


# -----------------------------
# MAIN PIPELINE
# -----------------------------

def run_pipeline(signals):

    portfolio = run_persona("portfolio", signals)
    investment = run_persona("investment", signals)
    ignore = run_persona("ignore", signals)

    final = final_judgement(portfolio, investment, ignore)

    return {
        "portfolio": portfolio,
        "investment": investment,
        "ignore": ignore,
        "final": final
    }