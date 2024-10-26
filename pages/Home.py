import streamlit as st
from modules.navbar import navbar

st.set_page_config(page_title="Home")
st.sidebar.header("Home")

st.write(f"Streamlit version: {st.__version__}")
st.title("Welcome to the Physics Practice Tool")

st.write("""
Select a problem type from the sidebar to begin practicing.
""")

def main():
    navbar()
    st.title(f'Home')

if __name__ == '__main__':
    main()