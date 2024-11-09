import streamlit as st

# Set up the main page tabs
st.set_page_config(page_title="My Personal Platform", layout="wide")

# Main navigation tabs
tab1, tab2, tab3 = st.tabs(["Profile", "YouTube Videos", "Simulations"])

# Profile Page
with tab1:
    st.title("About Me")
    st.markdown("""
    ## Your Name
    Welcome to my personal platform! I am a beginner in Streamlit and GitHub.
    Here is my biography:
    
    - **Role**: Instructor in the Department of Architecture
    - **Research Interest**: Comparative studies in architecture and seismic analysis
    - **Hobbies**: Programming, teaching, and exploring new technologies
    """)

# YouTube Videos Page
with tab2:
    st.title("My YouTube Videos")
    st.markdown("""
    Here are some of my favorite YouTube videos:
    
    1. [Streamlit Basics](https://www.youtube.com/watch?v=JwSS70SZdyM)
    2. [Python Programming](https://www.youtube.com/watch?v=_uQrJ0TkZlc)
    3. [Data Visualization](https://www.youtube.com/watch?v=JLz5YJWJQig)
    """)

# Simulations Page
with tab3:
    st.title("Simulations")
    st.markdown("This page will contain interactive simulations in the future.")
    st.markdown("Stay tuned for updates!")

