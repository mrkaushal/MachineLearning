import streamlit as st



def prlist():
    st.write("Home")
# st.write("1. [Practical 1](https://kaushalpatel.info)")
    col1, col2 = st.columns(2)

    with col1:
        st.title("Practicals")
        st.write("Practical 1")

    with col2:
        st.title("Click to open")
        if st.button("Click me", key="pr1"):
            # open kaushalpatel.info
