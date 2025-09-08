import streamlit as st

st.set_page_config(
   page_title="Kerem's app",
   page_icon="🧊",
   layout="wide",
   initial_sidebar_state="expanded",
)

main = st.Page("main.py", title="Hjem") # Creates a page with the main.py as its contents
rsa = st.Page("rsa.py", title="RSA-kryptering") # Creates a page with other.py as its contents

pg = st.navigation([main, rsa]) # Creates a side-navigation bar
pg.run() # Runs the side-navigation bar