import os
import streamlit as st
import requests
from streamlit_oauth import OAuth2Component
from dotenv import load_dotenv
load_dotenv()

CLIENT_ID = os.environ['GITHUB_CLIENT_ID']
CLIENT_SECRET = os.environ['GITHUB_CLIENT_SECRET']
REDIRECT_URI = "http://localhost:8501"


if "email" not in st.session_state:
  with st.spinner():
    authorize_endpoint = "https://github.com/login/oauth/authorize"
    token_endpoint = "https://github.com/login/oauth/access_token"
    api_endpoint =  "https://api.github.com"
    
    st.title("OAuth2 Authentication Demo")
    st.write("This is a demo feedback application for the Sofia Python MeetUp")
    
    # Create an OAuth2Component instance
    oauth2 = OAuth2Component(CLIENT_ID, CLIENT_SECRET, authorize_endpoint, token_endpoint)
    result = oauth2.authorize_button(
        name="Login with GitHub",
        icon="https://github.githubassets.com/favicons/favicon.png",
        redirect_uri=REDIRECT_URI,
        scope="user:email", 
        key="github_login",
        extras_params={"allow_signup": "true"},
        use_container_width=True,
    )
    
    if result:
        # Use the access token to fetch the user's GitHub primary email
        access_token = result["token"]["access_token"]
        headers = {"Authorization": f"Bearer {access_token}"}

        # Fetch emails
        email_response = requests.get(f"{api_endpoint}/user/emails", headers=headers)
        if email_response.status_code == 200:
            emails = email_response.json()
            primary_email = next((email['email'] for email in emails if email['primary']), "No primary email found")
            st.session_state["email"] = primary_email
            st.rerun()
else:
    st.sidebar.write(f"Welcome: {st.session_state['email']}")