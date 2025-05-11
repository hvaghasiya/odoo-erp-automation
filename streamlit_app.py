
import streamlit as st
import requests

# Set your N8n webhook URL here (ensure it's accessible, use ngrok for local testing if needed)
WEBHOOK_URL = "https://het-pragetx.app.n8n.cloud/webhook/09eea368-b78f-4209-9750-f28b706363c2/chat"

def get_chatbot_response(user_message):
    payload = {
        "sessionId": "7d010ad62c664800a02a346c8c101e9f",
        "action": "sendMessage",
        "chatInput": user_message
    }
    try:
        response = requests.post(WEBHOOK_URL, json=payload)
        if response.ok:
            response_json = response.json()
            return response_json.get("output", "No reply received"), payload, response_json
        else:
            return f"Error: {response.status_code} - {response.text}", payload, {}
    except Exception as e:
        return f"Request failed: {e}", payload, {}
 
# Main UI
def main():
    st.set_page_config(page_title="N8n Chatbot", layout="centered")
    st.title("Odoo ERP automation Interactive UI")
 
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
 
    # Chat message input
    user_input = st.chat_input("Type your message...")
 
    if user_input:
        # Store user message
        st.session_state.chat_history.append(("user", user_input))
 
        # Get response from chatbot
        reply, payload, full_response = get_chatbot_response(user_input)
 
        # Store bot response
        st.session_state.chat_history.append(("bot", reply))
 
    # Display the conversation
    for sender, message in st.session_state.chat_history:
        with st.chat_message("user" if sender == "user" else "assistant"):
            st.markdown(message)
 
if __name__ == "__main__":
    main()
