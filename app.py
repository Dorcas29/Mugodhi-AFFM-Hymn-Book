# Core Pkgs
import streamlit as st
import streamlit.components.v1 as stc

# EDA Pkgs
import pandas as pd
import neattext as nt
import neattext.functions as nfx


# Data Viz Pkgs
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import altair as alt

def main():
    st.title("Mugodhi AFM Hymn Book")
    menu = ["Home","Hymn","About"]

    choice = st.sidebar.selectbox("Menu",menu)
    if choice == "Home":
        st.subheader("Favorite")
    elif choice == "Hymn":
        st.subheader("Hymn Retrieval")
    else:
        st.subheader("About")


if _name_ == '_main_':
    main()


