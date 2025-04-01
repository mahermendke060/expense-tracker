import streamlit as st
from datetime import datetime
import requests

API_URL = "http://127.0.0.1:8000"


def add_update_tab():
    selected_date = st.date_input("Enter Date:", datetime(2024, 8, 1), label_visibility="collapsed")

    # Handle API request errors
    try:
        response = requests.get(f"{API_URL}/expenses/{selected_date}")
        if response.status_code == 200:
            existing_expenses = response.json()

        else:
            st.error("Failed to retrieve expenses")
            existing_expenses = []
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching expenses: {e}")
        existing_expenses = []

    categories = ["Rent", "Food", "Shopping", "Entertainment", "Other"]

    with st.form(key="expense_form"):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.subheader("Amount")
        with col2:
            st.subheader("Category")
        with col3:
            st.subheader("Notes")
        expenses=[]

        for i in range(5):
            # Retrieve values from existing expenses or set defaults
            if i < len(existing_expenses):
                amount = existing_expenses[i].get('amount', 0.0)  # Default to 0.0 if missing
                category = existing_expenses[i].get('category', 'Shopping')  # Default to 'Shopping'
                notes = existing_expenses[i].get('notes', " ")  # Default to empty space
            else:
                amount = 0.0
                category = 'Shopping'
                notes = " "

            col1, col2, col3 = st.columns(3)
            with col1:
                amount_input=st.number_input(label="amount", min_value=0.0, step=1.0, value=amount, key=f"amount_{i}")
            with col2:
                category_input=st.selectbox(label="category", options=categories, index=categories.index(category) if category in categories else 0, key=f"category_{i}")
            with col3:
                notes_input=st.text_input(label="notes", value=notes, key=f"notes_{i}")

            expenses.append({
            'amount':amount_input,
            'category':category_input,
            'notes':notes_input
            })
        submit_button = st.form_submit_button()
        if submit_button:
            filtered_expenses=[expense for expense in expenses if expense['amount']>0]
            requests.post(f"{API_URL}/expenses/{selected_date}",json=filtered_expenses)
            if response.status_code==200:
                st.success("Expense Updated Successfully!")
            else:
                st.error("Failed update expense.")
