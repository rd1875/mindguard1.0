import streamlit as st
from mindguard_agents.agent import root_agent
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="MindGuard", layout="centered")

st.title("🛡️ MindGuard - Emotional Safety Assistant")
st.markdown("Analyze your messages or journal entries for signs of overload or manipulation.")

if st.button("Open Dev UI"):
    st.markdown("[Click to open Dev UI](http://localhost:8000)", unsafe_allow_html=True)
