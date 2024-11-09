import streamlit as st

# Set page configuration (MUST be the first Streamlit command)
st.set_page_config(page_title="My Personal Platform", layout="wide")

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

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Choose a page:", ["Profile", "YouTube Videos", "Simulations", "Contact Me"])

# Profile Page
if page == "Profile":
    st.title("👨‍🏫 About Me")
    col1, col2 = st.columns(2)

    with col1:
        # Replace the image URL with the direct link to your uploaded photo
st.image("https://github.com/JEGRPHY/my-streamlit-platform/blob/main/albert-einstein-wrong-theory-of-relativity-flaws-gravity-new-physics-pulsars-1535474.jfif")
        st.markdown("### Mr. JEGR JABBAR")

    with col2:
        st.markdown(
            """
            Hi, I’m Jegr Jabbar, a physics teacher. I’m always curious about how things work,
            which is why I’ve started diving into coding and exploring how I can use technology in new and creative ways.
            Recently, I participated in a training with Mr. Hawkar, gaining new skills to apply in my classroom.
            
            - **Hobbies**: Programming, teaching, and exploring new technologies
            """
        )


# YouTube Videos Page
elif page == "YouTube Videos":
    st.title("📹 YouTube Videos")
    st.markdown(
        """
        Here are some of my favorite YouTube videos:
        
        1. [MAP OF PHYSICS](https://www.youtube.com/watch?v=ZihywtixUYo)
        2. [MAP OF SCIENCE](https://www.youtube.com/watch?v=ohyai6GIRZg)
        3. [MAP OF BLACK HOLE](https://www.youtube.com/watch?v=Wf0uxjWGwPk)
        4. [ESCAPE EARTH](https://www.youtube.com/watch?v=gCA5pU0RxK0)
        5. [HISTORY OF THE UNIVERSE](https://www.youtube.com/watch?v=7KYTJ8tBoZ8)
        """
    )

# Simulations Page
elif page == "Simulations":
    st.title("📈 Simulations")

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
elif page == "Contact Me":
    st.title("✉️ Contact Me")
    st.markdown("Feel free to reach out to me at:")
    st.markdown("**Email**: jegrjebar@gmail.com")
    if st.button("Send Greetings"):
        st.success("Thank you for reaching out! I will get back to you soon.")

# Display some animations for fun
st.balloons()
st.snow()
