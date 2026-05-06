import streamlit as st

st.title("Registration Form")

name = st.text_input("Name", key="name")
email = st.text_input("Email", key="email")
password = st.text_input("Password", type="password", key="password")

if st.button("Submit", key="submit"):
    if not name:
        st.write("Name is required")
    elif "@" not in email or "." not in email:
        st.write("Enter valid email")
    elif len(password) < 8:
        st.write("Password must be at least 8 characters")
    else:
        st.write("Registration Successful")