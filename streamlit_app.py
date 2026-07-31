import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/ask"

st.set_page_config(
    page_title="Support Knowledge Copilot",
    page_icon="🤖",
    layout="wide"
)

# ---------- Sidebar ----------
with st.sidebar:
    st.title("🤖 Support Copilot")

    st.markdown("### Sample Questions")

    samples = [
        "How do I reset my password?",
        "Explain OAuth authentication.",
        "How do refunds work?",
        "What does Error 401 mean?",
        "How can I onboard a new employee?"
    ]

    for q in samples:
        if st.button(q, use_container_width=True):
            st.session_state.prompt = q

    st.divider()

    if st.button("🗑 Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# ---------- Chat History ----------
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("💬 Support Knowledge Copilot")

st.caption("Ask questions about your documentation.")

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

        if message["role"] == "assistant":

            with st.expander("📚 Sources"):

                for source in message["sources"]:
                    st.write(f"• {source}")

# ---------- Chat Input ----------

prompt = st.chat_input("Ask anything about your documentation...")

if "prompt" in st.session_state:
    prompt = st.session_state.prompt
    del st.session_state.prompt

if prompt:

    st.session_state.messages.append(
        {
            "role":"user",
            "content":prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        with st.spinner("Searching..."):

            response = requests.post(
                API_URL,
                json={
                    "question":prompt
                }
            )

            data = response.json()

            answer = data["answer"]
            sources = data["sources"]

            st.markdown(answer)

            with st.expander("📚 Sources"):

                for source in sources:
                    st.write(f"• {source}")

    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":answer,
            "sources":sources
        }
    )