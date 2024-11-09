import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def run_simulation():
    st.header("Simple Sine Wave Simulation")

    # User input for frequency
    freq = st.slider("Select the frequency of the sine wave", 1, 20, 5)

    # Generate data for the sine wave
    x = np.linspace(0, 2 * np.pi, 500)
    y = np.sin(freq * x)

    # Plot the sine wave
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title(f"Sine Wave with Frequency {freq}")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")

    # Display the plot in Streamlit
    st.pyplot(fig)

# This is the main function for the simulation
if __name__ == "__main__":
    run_simulation()

