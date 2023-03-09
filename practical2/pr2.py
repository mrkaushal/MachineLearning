import streamlit as st
from matplotlib import pyplot as plt
import plotly.express as px
from streamlit_echarts import st_echarts
import pandas as pd
import numpy as np
import seaborn as sns 
import pickle  # To save the ML model to create pre-trained model
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

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
    data = pd.read_csv("./csv_files/Cars_Data.csv")
    # df.drop(['New_Price'], axis=1, inplace=True)
    # save the model to disk
    # df.to_csv("./csv_files/Cars_Data.csv", index=False)
    st.dataframe(data, use_container_width=True)
    st.write("<h4>Cars CSV Describe</h4>", unsafe_allow_html=True)
    st.write(data.describe())

    #Initializing the variables
    X = data['Power'].values.reshape(-1,1)
    y = data['Engine'].values.reshape(-1,1)

    #Ploting a graph to see the points
    df = pd.DataFrame({'Power': X.flatten(), 'Engine': y.flatten()})

    # create the scatter chart using plotly
    fig = px.scatter(df, x='Power', y='Engine')

    # display the chart using streamlit
    st.write("<h4>Scatter Plot</h4>", unsafe_allow_html=True)
    st.plotly_chart(fig)

    # convert X into integer and remove bhp from the values
    X = X.astype(int)
    X = X/1000
    #Splitting our dataset to Training and Testing dataset
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=45)

    #Fitting Linear Regression to the training set
    reg = LinearRegression()
    reg.fit(X_train, y_train)

    # Predicting the Test set result
    y_pred = reg.predict(X_test)

    df = pd.DataFrame({'Actual': y_test.flatten(), 'Predicted': y_pred.flatten()})

    # create the scatter chart using plotly
    fig = px.scatter(df, x='Actual', y='Predicted')

    # display the chart using streamlit
    st.write("<h4>Scatter Plot</h4>", unsafe_allow_html=True)
    st.plotly_chart(fig)