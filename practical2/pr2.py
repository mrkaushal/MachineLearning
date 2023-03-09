import streamlit as st
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns 
import pickle  # To save the ML model to create pre-trained model
import os

def pr2():
    st.title("Practical 2")
    with st.expander("AIM"):
        st.write("""
        Linear Regression
          Select the Dataset of your choice and respond to following questions.
          - Why do you want to apply regression on selected dataset? Discuss the
          full story behind the dataset.
          - How many total observations in data?
          - How many independent variables?
          - Which is dependent variable?
          - Which are most useful variable in estimation? Prove using correlation.
          - Implement linear regression using OLS method.
          - Implement linear regression using Gradient Descent from scratch.
          - Implement linear regression using sklearn API.
          - Quantify goodness of your model and discuss steps taken for
          improvement (RMSE, SSE, R2Score).
          - Discuss comparison of different methods.
          - Prepare presentation for this work in group of 5
        """)
