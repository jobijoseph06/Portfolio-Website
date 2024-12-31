

from send_email import send_email

import streamlit as st


st.header("Contact Me")
with st.form(key="email_form"):

    user_email = st.text_input("Enter Your Email", placeholder="user@example.com")
    user_message = st.text_area("Your Message", placeholder="Enter your message")

    message = f"""\
Subject: New email from {user_email}

From : {user_email}
{user_message}
"""
    submit_button = st.form_submit_button("Submit")
    if submit_button:
        send_email(message)
        st.info("Your email  was sent successfully")