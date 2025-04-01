import streamlit as st
from add_update import add_update_tab
from analytics_by_category import analytics_tab

st.title("Expense Management System")
tab1, tab2  = st.tabs(["Add/Updates", "Analytics By Category"])

with tab1:
    add_update_tab()

with tab2:
    analytics_tab()



