import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

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
    st.title("YouTube Videos")
    st.markdown("""
    Here are some of my favorite YouTube videos:
    
    1. [MAP OF PHYSICS](https://www.youtube.com/watch?v=ZihywtixUYo&pp=ygUObWFwIG9mIHBoeXNpY3M%3D)
    2. [MAP OF SCIENCE](https://www.youtube.com/watch?v=ohyai6GIRZg&pp=ygUObWFwIG9mIHNjaWVuY2U%3D)
    3. [MAP OF BLACK HOLE](https://www.youtube.com/watch?v=Wf0uxjWGwPk&pp=ygUSbWFwIG9mIGJsYWNrIGhvbGVz)
    4. [ESCAPE EARTH](https://www.youtube.com/watch?v=gCA5pU0RxK0&pp=ygUUZXNjYXBlIEVBUlRIIE1PUkdBTiA%3D)
    5. [HISTORY OF THE UNIVERSE](https://www.youtube.com/watch?v=7KYTJ8tBoZ8&pp=ygUsaGlzdG9yeSBvZiB0aGUgdW5pdmVyc2UgbmVpbCBkZWdyYXNzZSB0eXNvbiA%3D)
    """)

# Simulations Page
with tab3:
    st.title("Simulations")

    # Sub-tabs for different simulations
    sim_tab1, sim_tab2 = st.tabs(["Sine Wave Simulation", "Quadratic Equation Simulation"])

    # Sine Wave Simulation
    with sim_tab1:
        st.header("Simple Sine Wave Simulation")
        freq = st.slider("Select the frequency of the sine wave", 1, 20, 5)
        x = np.linspace(0, 2 * np.pi, 500)
        y = np.sin(freq * x)

        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.set_title(f"Sine Wave with Frequency {freq}")
        ax.set_xlabel("X-axis")
        ax.set_ylabel("Y-axis")
        st.pyplot(fig)

    # Quadratic Equation Simulation
    with sim_tab2:
        st.header("Quadratic Equation Simulation")
        a = st.slider("Select coefficient 'a'", -10, 10, 1)
        b = st.slider("Select coefficient 'b'", -20, 20, 0)
        c = st.slider("Select coefficient 'c'", -30, 30, 0)

        x = np.linspace(-10, 10, 500)
        y = a * x**2 + b * x + c

        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.set_title(f"Quadratic Equation: y = {a}x² + {b}x + {c}")
        ax.set_xlabel("X-axis")
        ax.set_ylabel("Y-axis")
        st.pyplot(fig)

# Contact Me Page
with tab4:
    st.title("Contact Me")
    st.markdown("Email: jegrjebar@gmail.com")
    st.markdown("Stay tuned for updates!")
