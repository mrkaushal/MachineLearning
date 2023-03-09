import streamlit as st
import numpy as np
import pandas as pd
from numpy.lib.shape_base import column_stack

def pr1():
    st.title("Practical 1")
    with st.expander("AIM"):
        st.write("""
        Numpy
            - Creating blank array, with predefined data, with pattern specific data
            - Slicing and Updating elements,
            - Shape manipulations
            - Looping over arrays.
            - Reading files in numpy
            - Use numpy vs list for matrix multiplication of 1000 X 1000 array and
            evaluate computing performance.
        """)
    # Blank Array Using Numpy
    arrblank = np.array([]) 
    st.write("<h4>Blank Array</h4>", unsafe_allow_html=True)
    st.write(arrblank)
    
    # Predefined Data Array Using Numpy
    a = np.array([[2, 2, 3], 
                [3, 4, 5], 
                [5, 6, 7]])
    st.write("<h4>Predefined Matrix A</h4>", unsafe_allow_html=True)
    st.write(a)

    # Pattern Specific Data Using Numpy
    a1d = np.array([1, 2, 3, 4])
    a2d = np.array([[1,2], [3, 4]])
    st.write("<h4>1D-Array</h4>", unsafe_allow_html=True)
    st.write(a1d)
    st.write("<h4>1D Array converted to 2D-Array</h4>", unsafe_allow_html=True)
    st.write(a2d)

    # Slicing In Numpy Array
    st.write("<h3>Slicing In Numpy Array</h3>", unsafe_allow_html=True)
    arr = np.array([1, 2, 3, 4, 5, 6, 7])
    st.write("<h4>Original Array</h4>", unsafe_allow_html=True)
    st.write(arr)
    st.write("<h4>Slicing</h4>", unsafe_allow_html=True)
    st.write(arr[-5:-1])
    st.write(arr[2: ])

    # Updating in Numpy Array
    st.write("<h3>Updating in Numpy Array</h3>", unsafe_allow_html=True)
    arr = np.array([1,2,3,4,5,6,7,8,9])
    st.write("<h4>Original Array</h4>", unsafe_allow_html=True)
    st.write(arr)
    arr[arr == 5] = 101
    st.write("<h4>Updated Array</h4>", unsafe_allow_html=True)
    st.write(arr)

    # Shape Manipulation Of Numpy Array
    st.write("<h3>Shape Manipulation Of Numpy Array</h3>", unsafe_allow_html=True)
    a = np.random.random((10))
    st.write("<h4>Original Array</h4>", unsafe_allow_html=True)
    st.write(a)
    A=a.reshape(2,5)
    st.write("<h4>Reshaped Array</h4>", unsafe_allow_html=True)
    st.write(A)

    # Performing Loop on Numpy 2D-Array
    st.write("<h3>Performing Loop on Numpy 2D-Array</h3>", unsafe_allow_html=True)
    arr = np.array([[8, 5, 9], [4, 5, 6]])
    st.write("<h4>Original Array</h4>", unsafe_allow_html=True)
    st.write(arr)
    st.write("<h4>Looping</h4>", unsafe_allow_html=True)
    for x in arr:
        st.write(x)

    with st.expander("Pandas"):
        st.write("""
        Pandas
            - Creating blank dataframe, with predefined data, with pattern specific data
            - Slicing and Updating elements,
            - Shape manipulations
            - Looping over dataframe.
            - Reading files in pandas
            - Use pandas vs list for matrix multiplication of 1000 X 1000 array and
            evaluate computing performance.
        """)

    # Creating Empty Frames
    st.write("<h3>Creating Empty Frames</h3>", unsafe_allow_html=True)
    df = pd.DataFrame()
    st.write(df)

    # Creating Frame With String and Integer Data
    st.write("<h3>Creating Frame With String and Integer Data</h3>", unsafe_allow_html=True)
    data = [10, 24, 27, 84, 33]
    df = pd.DataFrame(data, columns=['Numbers'])
    st.write("<h4>Integer Data Frame</h4>", unsafe_allow_html=True)
    st.write(df)

    list = ['Apple', 'Samsung', 'OnePlus', 'Oppo']
    df = pd.DataFrame(list, columns=['Brands'])
    st.write("<h4>String Data Frame</h4>", unsafe_allow_html=True)
    st.write(df)

    #Reading a csv file using pandas
    st.write("<h3>Reading a csv file using pandas TCS.NS</h3>", unsafe_allow_html=True)
    pd.options.display.max_rows = 8
    df = pd.read_csv('./csv_files/TCS.NS.csv')
    st.dataframe(df, use_container_width=True)

    # Slicing operations on row
    st.write("<h3>Slicing operations on row</h3>", unsafe_allow_html=True)
    list = [['Kaushal', 8.8], ['Keyur', 9.5], ['Karan', 9.32], ['Savan', 8.5]]
    df = pd.DataFrame(list, columns = ['Name', 'CGPA'])
    st.write('<h4>Result</h4>', unsafe_allow_html=True)
    st.dataframe(df, use_container_width=True)
    df1 = df.iloc[0:2]
    st.write('<h4>Sliced Result</h4>', unsafe_allow_html=True)
    st.dataframe(df1, use_container_width=True)

    # Slicing opertions on column
    st.write("<h3>Slicing opertions on column</h3>", unsafe_allow_html=True)
    list = [['Kaushal', 8.8, 22], ['Keyur', 9.5, 21], ['Karan', 9.32, 20], ['Savan', 8.5, 20]]
    df = pd.DataFrame(list, columns = ['Name', 'CGPA', 'Age'])
    st.write('<h4>Result</h4>', unsafe_allow_html=True)
    st.dataframe(df, use_container_width=True)
    df1 = df.iloc[:, 0:1]
    st.write('<h4>Sliced Result</h4>', unsafe_allow_html=True)
    st.dataframe(df1, use_container_width=True)

