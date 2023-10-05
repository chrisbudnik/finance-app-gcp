import streamlit as st
import pandas as pd
import numpy as np

# app - super simple version for tests
def main():
    st.title("Personal Finance Tracker")

    # Input for monthly income and expenses
    income = st.number_input("Enter your monthly income", min_value=0.0)
    expenses = st.number_input("Enter your monthly expenses", min_value=0.0)

    # Calculate savings and display
    savings = income - expenses
    st.write(f"Your savings for this month: ${savings:.2f}")

    if savings < 0:
        st.write("Looks like you've overspent this month. Consider revising your expenses.")
    elif savings == 0:
        st.write("You've broken even this month.")
    else:
        st.write("Good job on saving!")

if __name__ == "__main__":
    main()
