import streamlit as st
import requests
import pandas as pd

API_URL = "http://127.0.0.1:8000/ask"


# ---------------- UI CONFIG ----------------
st.set_page_config(
    page_title="AI Database Agent",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 AI Database Agent (LangGraph + PostgreSQL)")
st.caption("Ask questions in natural language and get SQL + answers instantly")


# ---------------- SESSION STATE ----------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# ---------------- INPUT ----------------
question = st.text_input("Ask your question:", placeholder="e.g. Top 5 customers by revenue")


col1, col2 = st.columns([1, 5])

with col1:
    ask = st.button("🚀 Ask")

with col2:
    clear = st.button("🧹 Clear Chat")


if clear:
    st.session_state.chat_history = []
    st.rerun()


# ---------------- CALL API ----------------
if ask and question:

    with st.spinner("Thinking... 🤖 Generating SQL & fetching data"):

        try:
            response = requests.post(
                API_URL,
                json={"question": question}
            )

            data = response.json()

            st.session_state.chat_history.append(data)

        except Exception as e:

            st.error(f"API Error: {e}")


# ---------------- CHAT DISPLAY ----------------
for chat in reversed(st.session_state.chat_history):

    st.markdown("---")

    st.markdown(f"### ❓ Question")
    st.write(chat.get("question"))

    st.markdown(f"### 🧠 Answer")
    st.success(chat.get("answer"))

    # SQL EXPANDER
    with st.expander("🔍 View SQL Query"):
        st.code(chat.get("sql"), language="sql")

    # ERROR HANDLING
    if chat.get("error"):
        st.error(chat.get("error"))

    # RESULT TABLE
    result = chat.get("result")

    if result:

        st.markdown("### 📊 Result")

        try:
            df = pd.DataFrame(result)
            st.dataframe(df, use_container_width=True)

        except Exception:
            st.write(result)