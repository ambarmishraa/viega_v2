# import streamlit as st
# import pandas as pd
# import plotly.express as px

# from signal_engine import generate_signals
# from pipeline import run_pipeline

# st.set_page_config(
#     page_title="Viega AI Decision Engine",
#     layout="wide"
# )

# # -------------------------
# # HEADER KPI STYLE
# # -------------------------
# st.title("🏭 Viega AI Market Intelligence System")

# st.markdown("### 🧠 Turning Market Noise into Product Decisions")

# # -------------------------
# # GENERATE SIGNALS
# # -------------------------
# if st.button("🚀 Generate Market Signals"):

#     signals = generate_signals(15)
#     df = pd.DataFrame(signals)

#     st.session_state["df"] = df

#     # KPI METRICS
#     col1, col2, col3 = st.columns(3)

#     col1.metric("Total Signals", len(df))
#     col2.metric("High Impact Signals", len(df[df["impact_score"] > 0.7]))
#     col3.metric("Companies Tracked", df["company"].nunique())

#     st.divider()

#     # RAW TABLE
#     st.subheader("📡 Market Signals (Filtered Intelligence View)")
#     st.dataframe(df.sort_values("impact_score", ascending=False), use_container_width=True)

#     # CHARTS
#     col1, col2 = st.columns(2)

#     with col1:
#         fig1 = px.histogram(df, x="company", title="Signals by Company")
#         st.plotly_chart(fig1, use_container_width=True)

#     with col2:
#         fig2 = px.pie(df, names="signal_type", title="Signal Type Distribution")
#         st.plotly_chart(fig2, use_container_width=True)

#     fig3 = px.histogram(df, x="domain", title="Domain Coverage")
#     st.plotly_chart(fig3, use_container_width=True)


# # -------------------------
# # AI DECISION ENGINE
# # -------------------------
# if st.button("🧠 Run AI Decision Engine"):

#     if "df" not in st.session_state:
#         st.warning("Generate signals first")
#         st.stop()

#     signals = st.session_state["df"].to_dict(orient="records")

#     results = run_pipeline(signals)

#     st.divider()
#     st.subheader("⚔️ AI Persona Debate (Core Intelligence Layer)")

#     c1, c2, c3 = st.columns(3)

#     with c1:
#         st.markdown("### 📦 Portfolio Expansion Expert")
#         st.info(results["portfolio"])

#     with c2:
#         st.markdown("### 💰 Investment Strategist")
#         st.success(results["investment"])

#     with c3:
#         st.markdown("### 🚫 Risk / Ignore Analyst")
#         st.warning(results["ignore"])

#     st.divider()

#     # FINAL DECISION CARD
#     st.subheader("🏁 FINAL AI DECISION")

#     decision = results["final"]

#     if "BUILD" in decision:
#         st.success(decision)
#     elif "INVEST" in decision:
#         st.info(decision)
#     else:
#         st.error(decision)

#     # OPTIONAL: confidence if you add later
#     if "confidence" in results:
#         st.metric("Confidence Score", f"{results['confidence']}%")


# # -------------------------
# # IMPACT ANALYSIS
# # -------------------------
# if "df" in st.session_state:

#     st.divider()
#     st.subheader("📊 Strategic Impact Analysis")

#     df = st.session_state["df"]

#     fig4 = px.bar(
#         df,
#         x="company",
#         y="impact_score",
#         color="signal_type",
#         title="Market Impact Heatmap"
#     )

#     st.plotly_chart(fig4, use_container_width=True)

#     # HIGH VALUE SIGNALS ONLY
#     st.subheader("🔥 High Priority Signals (Noise Filtered)")

#     high_df = df[df["impact_score"] > 0.7]

#     st.dataframe(high_df, use_container_width=True)



import streamlit as st
import pandas as pd
import plotly.express as px

from signal_engine import generate_signals
from pipeline import run_pipeline

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(
    page_title="Viega AI Decision Engine",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------
# CUSTOM UI — AWARD-WINNING REDESIGN
# -------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=IBM+Plex+Mono:wght@300;400;600&family=Syne:wght@400;700;800&display=swap');

/* ── ROOT TOKENS ─────────────────────────────────────── */
:root {
  --bg:          #050507;
  --surface:     #0d0d12;
  --surface2:    #13131c;
  --border:      rgba(255,255,255,0.06);
  --accent:      #00ffe0;
  --accent2:     #ff3cac;
  --accent3:     #ffe600;
  --text:        #e8e8f0;
  --muted:       #5a5a78;
  --radius:      12px;
  --glow:        0 0 24px rgba(0,255,224,0.18);
  --glow2:       0 0 24px rgba(255,60,172,0.18);
}

/* ── GLOBAL RESET ────────────────────────────────────── */
html, body, [class*="css"] {
  font-family: 'IBM Plex Mono', monospace !important;
  background-color: var(--bg) !important;
  color: var(--text) !important;
}

/* Animated grain overlay */
body::before {
  content: '';
  position: fixed;
  inset: 0;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.04'/%3E%3C/svg%3E");
  pointer-events: none;
  z-index: 9999;
  opacity: 0.5;
}

/* ── SIDEBAR ─────────────────────────────────────────── */
[data-testid="stSidebar"] {
  background: linear-gradient(180deg, #09090f 0%, #0d0d18 100%) !important;
  border-right: 1px solid var(--border) !important;
  box-shadow: 4px 0 40px rgba(0,255,224,0.04) !important;
}

[data-testid="stSidebar"] * {
  font-family: 'IBM Plex Mono', monospace !important;
}

[data-testid="stSidebar"] .stMarkdown h1,
[data-testid="stSidebar"] .stMarkdown h2,
[data-testid="stSidebar"] .stMarkdown h3 {
  color: var(--accent) !important;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  font-size: 0.75rem !important;
}

/* ── MAIN CONTAINER ──────────────────────────────────── */
.main, [data-testid="stAppViewContainer"] {
  background: var(--bg) !important;
}

div.block-container {
  padding: 2.5rem 2.5rem 4rem !important;
  max-width: 1400px !important;
}

/* ── HEADER ──────────────────────────────────────────── */
h1 {
  font-family: 'Bebas Neue', sans-serif !important;
  font-size: clamp(3rem, 6vw, 5.5rem) !important;
  letter-spacing: 0.05em !important;
  background: linear-gradient(90deg, var(--accent) 0%, #00c8ff 50%, var(--accent2) 100%);
  -webkit-background-clip: text !important;
  -webkit-text-fill-color: transparent !important;
  background-clip: text !important;
  line-height: 1 !important;
  margin-bottom: 0.25rem !important;
  animation: shimmer 4s ease-in-out infinite;
  background-size: 200% auto;
}

@keyframes shimmer {
  0%   { background-position: 0% center; }
  50%  { background-position: 100% center; }
  100% { background-position: 0% center; }
}

h2 {
  font-family: 'Syne', sans-serif !important;
  font-weight: 800 !important;
  font-size: 1.4rem !important;
  color: var(--text) !important;
  letter-spacing: 0.02em !important;
}

h3 {
  font-family: 'Syne', sans-serif !important;
  font-weight: 700 !important;
  color: var(--accent) !important;
  font-size: 1rem !important;
  text-transform: uppercase;
  letter-spacing: 0.1em !important;
}

/* ── SUBTITLE ────────────────────────────────────────── */
.subtitle-tag {
  display: inline-block;
  font-family: 'IBM Plex Mono', monospace;
  font-size: 0.72rem;
  color: var(--accent);
  border: 1px solid rgba(0,255,224,0.3);
  border-radius: 4px;
  padding: 0.2rem 0.7rem;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  margin-bottom: 0.5rem;
  background: rgba(0,255,224,0.05);
}

/* ── DIVIDER ─────────────────────────────────────────── */
hr {
  border: none !important;
  border-top: 1px solid var(--border) !important;
  margin: 1.5rem 0 !important;
}

/* ── METRIC CARDS ────────────────────────────────────── */
[data-testid="stMetric"] {
  background: var(--surface2) !important;
  border: 1px solid var(--border) !important;
  border-radius: var(--radius) !important;
  padding: 1.2rem 1.5rem !important;
  position: relative;
  overflow: hidden;
  transition: transform 0.2s, box-shadow 0.2s;
}

[data-testid="stMetric"]:hover {
  transform: translateY(-3px);
  box-shadow: var(--glow) !important;
  border-color: rgba(0,255,224,0.25) !important;
}

[data-testid="stMetric"]::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 2px;
  background: linear-gradient(90deg, var(--accent), var(--accent2));
}

[data-testid="stMetricLabel"] {
  font-family: 'IBM Plex Mono', monospace !important;
  font-size: 0.65rem !important;
  letter-spacing: 0.15em !important;
  text-transform: uppercase !important;
  color: var(--muted) !important;
}

[data-testid="stMetricValue"] {
  font-family: 'Bebas Neue', sans-serif !important;
  font-size: 2.8rem !important;
  color: var(--accent) !important;
  line-height: 1.1 !important;
}

/* ── SECTION LABEL ───────────────────────────────────── */
.section-label {
  font-family: 'IBM Plex Mono', monospace;
  font-size: 0.6rem;
  letter-spacing: 0.25em;
  text-transform: uppercase;
  color: var(--muted);
  border-left: 2px solid var(--accent);
  padding-left: 0.7rem;
  margin-bottom: 1rem;
}

/* ── BUTTONS ─────────────────────────────────────────── */
.stButton > button {
  font-family: 'IBM Plex Mono', monospace !important;
  font-size: 0.72rem !important;
  letter-spacing: 0.12em !important;
  text-transform: uppercase !important;
  background: transparent !important;
  border: 1px solid var(--accent) !important;
  color: var(--accent) !important;
  border-radius: 6px !important;
  padding: 0.6rem 1rem !important;
  transition: all 0.2s !important;
  position: relative;
  overflow: hidden;
}

.stButton > button:hover {
  background: rgba(0,255,224,0.08) !important;
  box-shadow: var(--glow) !important;
  transform: translateY(-1px) !important;
}

.stButton > button:active {
  transform: scale(0.97) !important;
}

/* ── SLIDERS ─────────────────────────────────────────── */
.stSlider [data-baseweb="slider"] div[role="slider"] {
  background: var(--accent) !important;
  box-shadow: var(--glow) !important;
}

.stSlider [data-baseweb="slider"] [data-testid="stThumbValue"] {
  color: var(--accent) !important;
  font-family: 'IBM Plex Mono', monospace !important;
  font-size: 0.7rem !important;
}

/* ── SELECTBOX / MULTISELECT ─────────────────────────── */
[data-baseweb="select"] {
  background: var(--surface) !important;
  border-radius: 6px !important;
}

[data-baseweb="select"] > div {
  background: var(--surface2) !important;
  border: 1px solid var(--border) !important;
  border-radius: 6px !important;
  font-family: 'IBM Plex Mono', monospace !important;
  font-size: 0.78rem !important;
  color: var(--text) !important;
}

/* ── INFO / SUCCESS / WARNING BOXES ──────────────────── */
[data-testid="stInfo"] {
  background: rgba(0,255,224,0.04) !important;
  border: 1px solid rgba(0,255,224,0.2) !important;
  border-radius: var(--radius) !important;
  color: var(--text) !important;
  font-family: 'IBM Plex Mono', monospace !important;
  font-size: 0.82rem !important;
  padding: 1rem 1.25rem !important;
}

[data-testid="stSuccess"] {
  background: rgba(0,255,128,0.05) !important;
  border: 1px solid rgba(0,255,128,0.25) !important;
  border-radius: var(--radius) !important;
  color: #00ff80 !important;
  font-family: 'IBM Plex Mono', monospace !important;
  font-size: 0.82rem !important;
}

[data-testid="stWarning"] {
  background: rgba(255,230,0,0.05) !important;
  border: 1px solid rgba(255,230,0,0.25) !important;
  border-radius: var(--radius) !important;
  color: var(--accent3) !important;
  font-family: 'IBM Plex Mono', monospace !important;
  font-size: 0.82rem !important;
}

[data-testid="stError"] {
  background: rgba(255,60,172,0.05) !important;
  border: 1px solid rgba(255,60,172,0.25) !important;
  border-radius: var(--radius) !important;
  color: var(--accent2) !important;
  font-family: 'IBM Plex Mono', monospace !important;
  font-size: 0.82rem !important;
}

/* ── EXPANDER ────────────────────────────────────────── */
[data-testid="stExpander"] {
  background: var(--surface2) !important;
  border: 1px solid var(--border) !important;
  border-radius: var(--radius) !important;
}

[data-testid="stExpander"] summary {
  font-family: 'IBM Plex Mono', monospace !important;
  font-size: 0.78rem !important;
  letter-spacing: 0.08em !important;
  color: var(--muted) !important;
  text-transform: uppercase;
}

/* ── DATAFRAME ───────────────────────────────────────── */
[data-testid="stDataFrame"] {
  border: 1px solid var(--border) !important;
  border-radius: var(--radius) !important;
  overflow: hidden;
}

/* ── TEXT AREA ───────────────────────────────────────── */
textarea {
  background: var(--surface2) !important;
  border: 1px solid var(--border) !important;
  border-radius: 6px !important;
  color: var(--text) !important;
  font-family: 'IBM Plex Mono', monospace !important;
  font-size: 0.8rem !important;
}

textarea:focus {
  border-color: rgba(0,255,224,0.4) !important;
  box-shadow: 0 0 0 1px rgba(0,255,224,0.15) !important;
}

/* ── PLOTLY CHART FRAMES ─────────────────────────────── */
[data-testid="stPlotlyChart"] {
  background: var(--surface) !important;
  border: 1px solid var(--border) !important;
  border-radius: var(--radius) !important;
  padding: 0.5rem;
  transition: box-shadow 0.3s;
}

[data-testid="stPlotlyChart"]:hover {
  box-shadow: var(--glow) !important;
  border-color: rgba(0,255,224,0.15) !important;
}

/* ── SCROLLBAR ───────────────────────────────────────── */
::-webkit-scrollbar { width: 5px; height: 5px; }
::-webkit-scrollbar-track { background: var(--bg); }
::-webkit-scrollbar-thumb { background: #1e1e2e; border-radius: 99px; }
::-webkit-scrollbar-thumb:hover { background: var(--muted); }

/* ── HEADER HERO LAYOUT ──────────────────────────────── */
.hero-wrapper {
  padding: 1.5rem 0 2rem;
  border-bottom: 1px solid var(--border);
  margin-bottom: 2rem;
  position: relative;
}

.hero-wrapper::after {
  content: '';
  position: absolute;
  bottom: -1px; left: 0;
  width: 200px; height: 1px;
  background: linear-gradient(90deg, var(--accent), transparent);
}

/* ── STATUS TICKER ───────────────────────────────────── */
.ticker {
  font-family: 'IBM Plex Mono', monospace;
  font-size: 0.6rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--muted);
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 0.5rem 0;
}

.ticker-dot {
  width: 6px; height: 6px;
  border-radius: 50%;
  background: var(--accent);
  display: inline-block;
  animation: pulse 2s ease-in-out infinite;
}

@keyframes pulse {
  0%, 100% { opacity: 1; box-shadow: 0 0 6px var(--accent); }
  50%       { opacity: 0.4; box-shadow: none; }
}

/* Section heading accent ──────── */
.section-heading {
  font-family: 'Bebas Neue', sans-serif;
  font-size: 2rem;
  letter-spacing: 0.06em;
  color: var(--text);
  margin: 2rem 0 0.25rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}
</style>

<!-- HERO HEADER -->
<div class="hero-wrapper">
  <div class="ticker">
    <span class="ticker-dot"></span>
    <span>SYSTEM LIVE</span>
    <span>·</span>
    <span>VIEGA INTELLIGENCE v2.0</span>
    <span>·</span>
    <span>MARKET SCAN READY</span>
  </div>
</div>
""", unsafe_allow_html=True)

# -------------------------
# SIDEBAR
# -------------------------
st.sidebar.markdown("""
<div style="padding:0.5rem 0 1rem;">
  <div style="font-family:'Bebas Neue',sans-serif;font-size:1.6rem;
              background:linear-gradient(90deg,#00ffe0,#ff3cac);
              -webkit-background-clip:text;-webkit-text-fill-color:transparent;
              letter-spacing:0.05em;">CONTROL PANEL</div>
  <div style="font-size:0.6rem;letter-spacing:0.2em;color:#5a5a78;text-transform:uppercase;">
    Signal Intelligence System
  </div>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("""<hr style="border:none;border-top:1px solid rgba(255,255,255,0.06);margin:0.5rem 0 1rem;">""", unsafe_allow_html=True)

gen_button = st.sidebar.button("🚀 Generate Signals", use_container_width=True)
run_button = st.sidebar.button("🧠 Run AI Engine", use_container_width=True)

st.sidebar.markdown("""
<div style="margin-top:1.5rem;margin-bottom:0.4rem;
            font-size:0.6rem;letter-spacing:0.2em;color:#5a5a78;
            text-transform:uppercase;border-left:2px solid #00ffe0;padding-left:0.6rem;">
  Filters
</div>
""", unsafe_allow_html=True)

if "df" in st.session_state:
    domain_options = st.session_state["df"]["domain"].unique().tolist()
else:
    domain_options = []

domain_filter = st.sidebar.multiselect("Domain", domain_options)
impact_filter = st.sidebar.slider("Min Impact", 0.0, 1.0, 0.5)

# -------------------------
# HEADER
# -------------------------
st.title("🏭 Viega AI Market Intelligence")
st.markdown("""
<div style="font-family:'IBM Plex Mono',monospace;font-size:0.85rem;
            color:#5a5a78;letter-spacing:0.06em;margin-bottom:1.5rem;">
  Turning signals into <span style="color:#00ffe0;">product decisions</span>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# -------------------------
# GENERATE SIGNALS
# -------------------------
if gen_button:
    signals = generate_signals(30)
    df = pd.DataFrame(signals)
    st.session_state["df"] = df

# -------------------------
# EMPTY STATE
# -------------------------
if "df" not in st.session_state:
    st.markdown("""
    <div style="
      text-align:center;padding:4rem 2rem;
      background:linear-gradient(135deg,rgba(0,255,224,0.03),rgba(255,60,172,0.03));
      border:1px solid rgba(255,255,255,0.06);border-radius:16px;margin-top:2rem;">
      <div style="font-family:'Bebas Neue',sans-serif;font-size:3rem;
                  color:rgba(255,255,255,0.08);letter-spacing:0.1em;">
        AWAITING SIGNAL INPUT
      </div>
      <div style="font-family:'IBM Plex Mono',monospace;font-size:0.78rem;
                  color:#5a5a78;letter-spacing:0.1em;margin-top:0.5rem;">
        ← Generate signals from the sidebar to begin
      </div>
    </div>
    """, unsafe_allow_html=True)
    st.stop()

df = st.session_state["df"]

# Apply filters
if domain_filter:
    df = df[df["domain"].isin(domain_filter)]

df = df[df["impact_score"] >= impact_filter]

# -------------------------
# KPI ROW
# -------------------------
st.markdown("""<div class="section-label">— Key Performance Indicators</div>""", unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)

c1.metric("Signals", len(df))
c2.metric("High Impact", len(df[df["impact_score"] > 0.7]))
c3.metric("Companies", df["company"].nunique())
c4.metric("Avg Impact", round(df["impact_score"].mean(), 2))

# -------------------------
# CHARTS
# -------------------------
st.markdown("---")
st.markdown("""<div class='section-heading'>📊 Intelligence Overview</div>
<div class='section-label'>— Signal distribution and type breakdown</div>""", unsafe_allow_html=True)

CHART_COLORS = ["#00ffe0","#ff3cac","#ffe600","#00c8ff","#7b61ff","#ff6e3c","#00ff80"]

CHART_TEMPLATE = dict(
    template="plotly_dark",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(family="IBM Plex Mono", color="#8888aa", size=11),
    margin=dict(l=16, r=16, t=36, b=16),
)

col1, col2 = st.columns(2)

with col1:
    fig1 = px.histogram(
    df, x="company", color="domain",
    color_discrete_sequence=CHART_COLORS,
)
    fig1.update_layout(
        bargap=0.15,
        xaxis=dict(gridcolor="rgba(255,255,255,0.04)", title_font=dict(size=10)),
        yaxis=dict(gridcolor="rgba(255,255,255,0.04)", title_font=dict(size=10)),
        legend=dict(font=dict(size=9), bgcolor="rgba(0,0,0,0)"),
    )
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    fig2 = px.pie(
        df, names="signal_type", hole=0.6,
        color_discrete_sequence=CHART_COLORS,
        
    )
    fig2.update_traces(
        textfont=dict(family="IBM Plex Mono", size=10, color="white"),
        marker=dict(line=dict(color="#050507", width=2))
    )
    st.plotly_chart(fig2, use_container_width=True)

# -------------------------
# TIMELINE
# -------------------------
st.markdown("---")
st.markdown("""<div class='section-heading'>📈 Trend Analysis</div>
<div class='section-label'>— Impact score over time by company</div>""", unsafe_allow_html=True)

df["timestamp"] = pd.to_datetime(df["timestamp"])

fig_time = px.line(
    df.sort_values("timestamp"),
    x="timestamp", y="impact_score", color="company",
    markers=True,
    color_discrete_sequence=CHART_COLORS,
    
)
fig_time.update_traces(line=dict(width=1.5), marker=dict(size=5))
fig_time.update_layout(
    xaxis=dict(gridcolor="rgba(255,255,255,0.04)"),
    yaxis=dict(gridcolor="rgba(255,255,255,0.04)"),
    legend=dict(font=dict(size=9), bgcolor="rgba(0,0,0,0)"),
)
st.plotly_chart(fig_time, use_container_width=True)

# -------------------------
# TREEMAP
# -------------------------
st.markdown("---")
st.markdown("""<div class='section-heading'>🌳 Market Structure</div>
<div class='section-label'>— Domain and company weight by impact</div>""", unsafe_allow_html=True)

fig_tree = px.treemap(
    df, path=["domain", "company"], values="impact_score",
    color_discrete_sequence=CHART_COLORS,
    
)
fig_tree.update_traces(
    textfont=dict(family="IBM Plex Mono", size=11),
    marker=dict(line=dict(width=1, color="#050507"))
)
st.plotly_chart(fig_tree, use_container_width=True)

# -------------------------
# DATA TABLE
# -------------------------
with st.expander("📥 Raw Data"):
    st.dataframe(df.sort_values("impact_score", ascending=False), use_container_width=True)

# -------------------------
# RUN AI ENGINE
# -------------------------
if run_button:

    results = run_pipeline(df.to_dict(orient="records"))

    st.markdown("---")
    st.markdown("""<div class='section-heading'>⚔️ Persona Debate</div>
    <div class='section-label'>— Multi-agent perspective synthesis</div>""", unsafe_allow_html=True)

    p1, p2, p3 = st.columns(3)

    with p1:
        st.markdown("""<div style="font-family:'Syne',sans-serif;font-weight:700;
                    font-size:0.85rem;text-transform:uppercase;letter-spacing:0.12em;
                    color:#00ffe0;margin-bottom:0.5rem;">🧠 Portfolio</div>""", unsafe_allow_html=True)
        st.info(results["portfolio"])

    with p2:
        st.markdown("""<div style="font-family:'Syne',sans-serif;font-weight:700;
                    font-size:0.85rem;text-transform:uppercase;letter-spacing:0.12em;
                    color:#00ff80;margin-bottom:0.5rem;">💰 Invest</div>""", unsafe_allow_html=True)
        st.success(results["investment"])

    with p3:
        st.markdown("""<div style="font-family:'Syne',sans-serif;font-weight:700;
                    font-size:0.85rem;text-transform:uppercase;letter-spacing:0.12em;
                    color:#ffe600;margin-bottom:0.5rem;">🚫 Ignore</div>""", unsafe_allow_html=True)
        st.warning(results["ignore"])

    # -------------------------
    # DECISION MATRIX
    # -------------------------
    st.markdown("---")
    st.markdown("""<div class='section-heading'>🧮 Decision Matrix</div>
    <div class='section-label'>— Weighted scoring across decision axes</div>""", unsafe_allow_html=True)

    scores = {
        "BUILD":  df["impact_score"].mean() * 100,
        "INVEST": len(df[df["impact_score"] > 0.7]) * 10,
        "IGNORE": len(df[df["impact_score"] < 0.4]) * 10
    }

    score_df = pd.DataFrame({
        "Decision": list(scores.keys()),
        "Score":    list(scores.values())
    })

    fig_score = px.bar(
        score_df, x="Decision", y="Score",
        color="Decision",
        color_discrete_map={"BUILD": "#00ffe0", "INVEST": "#00ff80", "IGNORE": "#ff3cac"},
        
    )
    fig_score.update_traces(marker_line_width=0)
    fig_score.update_layout(
        showlegend=False,
        xaxis=dict(gridcolor="rgba(255,255,255,0.04)"),
        yaxis=dict(gridcolor="rgba(255,255,255,0.04)"),
    )
    st.plotly_chart(fig_score, use_container_width=True)

    # -------------------------
    # FINAL DECISION
    # -------------------------
    st.markdown("---")
    st.markdown("""<div class='section-heading'>🏁 Final Recommendation</div>
    <div class='section-label'>— AI-synthesized market decision</div>""", unsafe_allow_html=True)

    decision = results["final"]
    decision_upper = decision.upper()

    base_confidence = df["impact_score"].mean() * 100

    if "feedback_log" in st.session_state:
        avg_rating = pd.DataFrame(st.session_state["feedback_log"])["rating"].mean()
        confidence = round(base_confidence * (avg_rating / 3))
    else:
        confidence = round(base_confidence)

    urgency = "HIGH" if confidence > 70 else "MEDIUM" if confidence > 40 else "LOW"

    urgency_color = {"HIGH": "#ff3cac", "MEDIUM": "#ffe600", "LOW": "#00ffe0"}[urgency]

    colA, colB = st.columns(2)

    with colA:
        if "BUILD" in decision_upper:
            st.success(f"### {decision}")
        elif "INVEST" in decision_upper:
            st.info(f"### {decision}")
        else:
            st.error(f"### {decision}")

    with colB:
        st.metric("Confidence", f"{confidence}%")
        st.metric("Urgency", urgency)

    # -------------------------
    # WHY THIS MATTERS
    # -------------------------
    st.markdown("---")
    st.markdown("""<div class='section-heading'>💡 Why This Matters</div>
    <div class='section-label'>— Contextual signal interpretation</div>""", unsafe_allow_html=True)

    key_domain = df['domain'].mode()[0]
    st.markdown(f"""
    <div style="
      background:linear-gradient(135deg,rgba(0,255,224,0.04),rgba(255,60,172,0.03));
      border:1px solid rgba(255,255,255,0.07);border-radius:12px;padding:1.5rem 2rem;
      font-family:'IBM Plex Mono',monospace;font-size:0.82rem;line-height:2;color:#c8c8e0;">
      <span style="color:#00ffe0;">▸</span> <strong style="color:#e8e8f0;">{len(df)}</strong> signals analyzed across <strong style="color:#e8e8f0;">{df['domain'].nunique()}</strong> domains<br>
      <span style="color:#ff3cac;">▸</span> <strong style="color:#e8e8f0;">{df['company'].nunique()}</strong> competitors active in market<br>
      <span style="color:#ffe600;">▸</span> Key trend domain: <strong style="color:#ffe600;">{key_domain}</strong><br>
      <span style="color:{urgency_color};">▸</span> Market activity suggests <strong style="color:{urgency_color};">{urgency.lower()}</strong> urgency response
    </div>
    """, unsafe_allow_html=True)

    # -------------------------
    # ACTION PLAN
    # -------------------------
    st.markdown("---")
    st.markdown("""<div class='section-heading'>🚀 Suggested Actions</div>
    <div class='section-label'>— Tactical next steps</div>""", unsafe_allow_html=True)

    if "BUILD" in decision_upper:
        actions = [
            ("00ffe0", "Expand product portfolio in high-growth domain"),
            ("00c8ff", "Prioritize high-impact signals"),
            ("7b61ff", "Launch internal R&D sprint"),
        ]
    elif "INVEST" in decision_upper:
        actions = [
            ("00ffe0", "Partner with universities and startups"),
            ("00c8ff", "Allocate R&D budget to new tech"),
            ("7b61ff", "Monitor competitors"),
        ]
    else:
        actions = [
            ("5a5a78", "No immediate action required"),
            ("5a5a78", "Continue monitoring signals"),
        ]

    action_html = "".join([
        f'<div style="display:flex;align-items:center;gap:0.75rem;padding:0.6rem 0;'
        f'border-bottom:1px solid rgba(255,255,255,0.04);">'
        f'<span style="color:#{c};font-size:1rem;">→</span>'
        f'<span style="font-family:\'IBM Plex Mono\',monospace;font-size:0.82rem;color:#c8c8e0;">{a}</span>'
        f'</div>'
        for c, a in actions
    ])
    st.markdown(f"""
    <div style="background:var(--surface2,#13131c);border:1px solid rgba(255,255,255,0.06);
                border-radius:12px;padding:1rem 1.5rem;">
      {action_html}
    </div>
    """, unsafe_allow_html=True)

    # -------------------------
    # HUMAN FEEDBACK LOOP
    # -------------------------
    st.markdown("---")
    st.markdown("""<div class='section-heading'>🧑‍💼 Human Feedback Loop</div>
    <div class='section-label'>— Continuous model improvement via analyst input</div>""", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        rating = st.slider("How useful is this recommendation?", 1, 5, 3)
        agreement = st.selectbox(
            "Do you agree?",
            ["Agree", "Partially Agree", "Disagree"]
        )

    with col2:
        feedback_text = st.text_area("Why? (Optional)")

    if st.button("Submit Feedback"):

        feedback_entry = {
            "rating":    rating,
            "agreement": agreement,
            "comment":   feedback_text,
            "decision":  decision
        }

        if "feedback_log" not in st.session_state:
            st.session_state["feedback_log"] = []

        st.session_state["feedback_log"].append(feedback_entry)

        st.success("✅ Feedback recorded!")

# -------------------------
# FEEDBACK ANALYTICS
# -------------------------
if "feedback_log" in st.session_state:

    st.markdown("---")
    st.markdown("""<div class='section-heading'>📊 Feedback Insights</div>
    <div class='section-label'>— Analyst sentiment and rating analytics</div>""", unsafe_allow_html=True)

    fb_df = pd.DataFrame(st.session_state["feedback_log"])

    colA, colB = st.columns(2)

    with colA:
        st.metric("Avg Rating", round(fb_df["rating"].mean(), 2))

        agree_count = fb_df["agreement"].value_counts()

        fig_fb = px.pie(
            names=agree_count.index,
            values=agree_count.values,
            hole=0.5,
            color_discrete_sequence=["#00ffe0", "#ffe600", "#ff3cac"],
            
        )
        fig_fb.update_traces(
            textfont=dict(family="IBM Plex Mono", size=10),
            marker=dict(line=dict(color="#050507", width=2))
        )
        st.plotly_chart(fig_fb, use_container_width=True)

    with colB:
        st.markdown("""<div style="font-family:'Syne',sans-serif;font-weight:700;
                    font-size:0.85rem;text-transform:uppercase;letter-spacing:0.1em;
                    color:#5a5a78;margin-bottom:0.75rem;">Recent Feedback</div>""", unsafe_allow_html=True)
        st.dataframe(fb_df.tail(5), use_container_width=True)