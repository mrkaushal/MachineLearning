import streamlit as st
from streamlit_option_menu import option_menu

# Practicals
from practical1.pr1 import pr1
from practical2.pr2 import pr2

st.set_page_config(
    page_title="Machine Lerning",
    # page_icon=im,
    layout="wide", # centered
    initial_sidebar_state="expanded", # collapsed
    menu_items={
        'Get Help': 'https://kaushalpatel.info',
        'Report a bug': "https://kaushalpatel.info",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

def main():
    with st.sidebar:
        selected = option_menu("Main Menu", 
                           options=["Home", "Practical-1", "Practical-2"],
                           icons=["🏠", "📖", "📞"],
                           default_index=2,
                           orientation="vertical",
                          )
    
    if selected == "Home":
        st.write("Home")
    elif selected == "Practical-1":
        pr1()
    elif selected == "Practical-2":
        pr2()


if __name__ == "__main__":
    main()