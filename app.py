import streamlit as st


st.title("Neural Lab Internal Categorization Testing API")

m_form = st.form(key = 'form1')

title = m_form.text_input("Enter the Title of Article")

body = m_form.text_area("Enter the Body of Article")

submit = m_form.form_submit_button(label = "Get Categories")

if submit:
    st.subheader("dasdasd")