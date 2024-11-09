import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def run_simulation():
    st.header("Quadratic Equation Simulation")

    # User input for coefficients
    a = st.slider("Select coefficient 'a'", -10, 10, 1)
    b = st.slider("Select coefficient 'b'", -20, 20, 0)
    c = st.slider("Select coefficient 'c'", -30, 30, 0)

    # Generate data for the quadratic equation
    x = np.linspace(-10, 10, 500)
    y = a * x**2 + b * x + c

    # Plot the quadratic equation
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title(f"Quadratic Equation: y = {a}x² + {b}x + {c}")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")

    # Display the plot in Streamlit
    st.pyplot(fig)

# This is the main function for the simulation
if __name__ == "__main__":
    run_simulation()

