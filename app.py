import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Function to add a background image
def add_background_image():
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://your-image-url.com/background.jpg");
            background-size: cover;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Call the function to set the background image
add_background_image()

# Set up the main page tabs and configuration
st.set_page_config(page_title="My Personal Platform", layout="wide")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Choose a page:", ["Profile", "YouTube Videos", "Simulations", "Contact Me"])

# Profile Page
if page == "Profile":
    st.title("👨‍🏫 About Me")
    col1, col2 = st.columns(2)

    with col1:
        st.image("https://your-profile-image-url.com/photo.jpg", width=200)
        st.markdown("### Mr. JEGR JABBAR")

    with col2:
        st.markdown("""
        Hi, I’m Jegr Jabbar, a physics teacher. I’m always curious about how things work,
        which is why I’ve started diving
