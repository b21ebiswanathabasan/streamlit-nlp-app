import streamlit as st
import requests

# Set page config
st.set_page_config(page_title="Data Management App", page_icon="🤖", layout="centered")

st.title("Interactive NLP & Profile Tool")
st.subheader("Choose an action:")

# Page state logic
if "page" not in st.session_state:
    st.session_state.page = "home"

def go_to_nlp():
    st.session_state.page = "nlp"

def go_to_run_profile():
    st.session_state.page = "run_profile"

def go_to_all_profiles():
    st.session_state.page = "all_profiles"

# Home page buttons
if st.session_state.page == "home":
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("1️⃣ Chat using NLP"):
            go_to_nlp()
    with col2:
        if st.button("2️⃣ Run a Profile"):
            go_to_run_profile()
    with col3:
        if st.button("3️⃣ Get all Profile Details"):
            go_to_all_profiles()

# NLP chat page
elif st.session_state.page == "nlp":
    st.header("🗨️ Chat using NLP")
    user_input = st.text_area("Enter your query in natural language:")

    if st.button("Submit"):
        if user_input.strip():
            webhook_url = "https://dmgmt.app.n8n.cloud/webhook/chat-agent"  # Replace with actual N8N webhook
            payload = {"text": user_input}

            try:
                response = requests.post(webhook_url, json=payload)
                if response.status_code == 200:
                    st.success("✅ NLP query sent successfully!")

                    data = response.json()

                    # 🧾 Show heading for parsed response
                    st.markdown("### 📋 Your Response")

                    # 🎯 Nicely format the response
                    if isinstance(data, dict):
                        for key, value in data.items():
                            st.markdown(f"**{key}:** {value}")
                    elif isinstance(data, list):
                        for i, item in enumerate(data):
                            if isinstance(item, dict):
                                for k, v in item.items():
                                    st.markdown(f"- **{k}**: {v}")
                            else:
                                st.markdown(f"- {item}")
                    else:
                        st.markdown(f"{data}")
                else:
                    st.error(f"❌ Error from webhook: {response.status_code}")
            except Exception as e:
                st.error(f"⚠️ Failed to connect to webhook: {e}")
        else:
            st.warning("Please enter a query before submitting.")

    if st.button("🔙 Back to Home"):
        st.session_state.page = "home"


# Run Profile page
elif st.session_state.page == "run_profile":
    st.header("⚙️ Run a Profile")
    st.info("This section can be extended to trigger profile execution logic.")
    if st.button("🔙 Back to Home"):
        st.session_state.page = "home"

# All Profiles page
elif st.session_state.page == "all_profiles":
    st.header("📂 Get All Profile Details")
    st.info("This section can be extended to fetch and display profile data.")
    if st.button("🔙 Back to Home"):
        st.session_state.page = "home"
