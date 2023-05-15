# streamlit extras 

import streamlit as st
from streamlit_extras.stoggle import stoggle

stoggle("Here's a little Secret of Python!!","Streamlit-extras is so cool feature to test!!")

def strike(text:str):
    """ 
     Strikes input text 
    
     Args : text(str): Input Text 
    
    """
    return st.write(f"<del> {text}</del>",unsafe_allow_html=True)


strike("Java is the best programming language in the world!!")
