import streamlit as st
def navbar():
    # builds the sidebar menu
    with st.sidebar:
        st.page_link('pages/Home.py', label='Home')
        st.page_link('pages/Forces.py', label='Forces')
