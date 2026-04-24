import streamlit as st
import pandas as pd
import plotly.express as px

from signal_engine import generate_signals
from pipeline import run_pipeline

st.set_page_config(page_title="Viega AI Decision Engine", layout="wide")

st.title("🏭 Viega AI Market Intelligence System")

# -------------------------
# GENERATE SIGNALS
# -------------------------
if st.button("Generate Signals"):

    signals = generate_signals(12)
    df = pd.DataFrame(signals)

    st.session_state["df"] = df

    st.subheader("📡 Raw Market Signals")
    st.dataframe(df, use_container_width=True)

    # -------------------------
    # CHART 1: Company distribution
    # -------------------------
    fig1 = px.histogram(
        df,
        x="company",
        title="Signals by Company"
    )
    st.plotly_chart(fig1, use_container_width=True)

    # -------------------------
    # CHART 2: Signal types
    # -------------------------
    fig2 = px.pie(
        df,
        names="signal_type",
        title="Signal Type Distribution"
    )
    st.plotly_chart(fig2, use_container_width=True)

    # -------------------------
    # CHART 3: Domain activity
    # -------------------------
    fig3 = px.histogram(
        df,
        x="domain",
        title="Domain Coverage"
    )
    st.plotly_chart(fig3, use_container_width=True)


# -------------------------
# RUN AI ENGINE
# -------------------------
if st.button("Run AI Decision Engine"):

    if "df" not in st.session_state:
        st.warning("Generate signals first")
        st.stop()

    signals = st.session_state["df"].to_dict(orient="records")

    results = run_pipeline(signals)

    st.subheader("🧠 Portfolio Persona")
    st.write(results["portfolio"])

    st.subheader("💰 Investment Persona")
    st.write(results["investment"])

    st.subheader("🚫 Ignore Persona")
    st.write(results["ignore"])

    st.subheader("🏁 FINAL DECISION")
    st.success(results["final"])


# -------------------------
# BONUS: Impact Score Chart
# -------------------------
if "df" in st.session_state:

    st.subheader("📊 Impact Score Analysis")

    fig4 = px.bar(
        st.session_state["df"],
        x="company",
        y="impact_score",
        color="signal_type",
        title="Impact Score by Company"
    )

    st.plotly_chart(fig4, use_container_width=True)