import streamlit as st
import requests

# Set page config (optional)
st.set_page_config(page_title="Data Management Bot", page_icon="🤖", layout="centered")

# Title of the main app
st.title("Interactive NLP & Profile Tool")

# Create three buttons on main page
st.subheader("Choose an action:")

# Define navigation-like behavior using session state
if "page" not in st.session_state:
    st.session_state.page = "home"

# Callback functions to change pages
def go_to_nlp():
    st.session_state.page = "nlp"

def go_to_run_profile():
    st.session_state.page = "run_profile"

def go_to_all_profiles():
    st.session_state.page = "all_profiles"

# Display buttons
if st.session_state.page == "home":
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("1️⃣ Chat with NLP"):
            go_to_nlp()
    with col2:
        if st.button("2️⃣ Run a Profile"):
            go_to_run_profile()
    with col3:
        if st.button("3️⃣ Get all Profile Details"):
            go_to_all_profiles()

# Page 1: Chat with NLP
elif st.session_state.page == "nlp":
    st.header("🗨️ Chat with NLP")
    user_input = st.text_area("Enter your query in natural language:")
    if st.button("Submit"):
        if user_input.strip():
            # Call N8N webhook with the user's input
            webhook_url = "https://dmgmt.app.n8n.cloud/webhook-test/chat-agent"  # Replace with actual N8N webhook
            payload = {"text": user_input}
            try:
                response = requests.post(webhook_url, json=payload)
                if response.status_code == 200:
                    st.success("✅ NLP query sent successfully!")
                    st.json(response.json())  # Show the response from N8N
                else:
                    st.error(f"❌ Error from webhook: {response.status_code}")
            except Exception as e:
                st.error(f"⚠️ Failed to connect to webhook: {e}")
        else:
            st.warning("Please enter a query before submitting.")

    # Back to home
    if st.button("🔙 Back to Home"):
        st.session_state.page = "home"

# Page 2: Run a Profile
elif st.session_state.page == "run_profile":
    st.header("⚙️ Run a Profile")
    st.info("This section can be extended to trigger profile execution logic.")
    if st.button("🔙 Back to Home"):
        st.session_state.page = "home"

# Page 3: Get all Profile Details
elif st.session_state.page == "all_profiles":
    st.header("📂 Get All Profile Details")
    st.info("This section can be extended to fetch and display profile data.")
    if st.button("🔙 Back to Home"):
        st.session_state.page = "home"
