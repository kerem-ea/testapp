import streamlit as st

st.set_page_config(
   page_title="Main",
   page_icon="🧊",
   layout="wide",
   initial_sidebar_state="expanded",
)

st.title("Kerem's app") #st.title creates a title, for the current page. It can be any datatype. Parameters: st.title(body, anchor=None, *, help=None, width="stretch")

st.badge("Test", color="violet") # Badge creates a tag. Parameters: st.badge(label, *, icon=None, color="blue", width="content")
st.caption("This is a caption") # st.caption(body, unsafe_allow_html=False, *, help=None, width="stretch")

st.header("Intro") # st.header creates a header. Parameters: st.header(body, anchor=None, *, help=None, divider=False, width="stretch")
st.subheader("Intro 1") # st.subheader creates a subheader. Parameters: st.subheader(body, anchor=None, *, help=None, divider=False, width="stretch")
st.write("This is an intro. ") # st.write writes text

code = """def function():
        print("This is a function-")"""
st.code(code, language="python") # st.code writes out code. Parameters: (body, language="python", *, line_numbers=False, wrap_lines=False, height="content", width="stretch")

def get_user_name():
    return 'John'

with st.echo(): # Shows and executes code. Parameters:  st.echo(code_location="above"). Either "above" or "below"
    # Everything inside this block will be both printed to the screen and executed.

    def get_punctuation():
        return '!!!'

    greeting = "Hi there, "
    user_name = get_user_name()
    punctuation = get_punctuation()

    st.write(greeting, user_name, punctuation)

st.latex( # Displays latex. Parameters: st.latex(body, *, help=None, width="stretch")
    r''' 
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''') 