import streamlit as st
st.set_page_config(page_title="Home")
st.sidebar.header("Home")
st.title("🎈 My new app")



st.write(f"Streamlit version: {st.__version__}")
st.title("Welcome to the Physics Practice Tool")

st.write("""
Select a problem type from the sidebar to begin practicing.
""")

