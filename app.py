import streamlit as st

# Set up the main page tabs
st.set_page_config(page_title="My Personal Platform", layout="wide")

# Main navigation tabs
tab1, tab2, tab3, tab4 = st.tabs(["Profile", "YouTube Videos", "Simulations", "Contact me"])

# Profile Page
with tab1:
    st.title("About Me")
    st.markdown("""
    ## Mr. JEGR JABBAR
    Hi, I’m Jegr Jabbar, a physics teacher. I’m always curious about how things work, which is why I’ve started diving into coding and exploring how I can use technology in new and creative ways. Recently, I participated in a training with Mr. Hawkar, I learned so much and gained skills that I can’t wait to put into practice in my classroom.
    
    - **Hobbies**: Programming, teaching, and exploring new technologies
    """)

# YouTube Videos Page
with tab2:
    st.title(" YouTube Videos")
    st.markdown("""
    Here are some of my favorite YouTube videos:
    
    1. [Streamlit Basics](https://www.youtube.com/watch?v=ZihywtixUYo&pp=ygUObWFwIG9mIHBoeXNpY3M%3D)
    2. [Python Programming](https://www.youtube.com/watch?v=gCA5pU0RxK0&pp=ygUUZXNjYXBlIEVBUlRIIE1PUkdBTiA%3D)
    3. [Data Visualization](https://www.youtube.com/watch?v=7KYTJ8tBoZ8&pp=ygUsaGlzdG9yeSBvZiB0aGUgdW5pdmVyc2UgbmVpbCBkZWdyYXNzZSB0eXNvbiA%3D)
    """)

# Simulations Page
with tab3:
    st.title("Simulations")
    st.markdown("This page will contain interactive simulations in the future.")
    st.markdown("Stay tuned for updates!")

