import streamlit as st

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from bokeh.plotting import figure
import plotly.figure_factory as ff
import seaborn as sns
import pydeck as pdk
import time

#loading data
@st.cache
def load_data(data_url):
    data = pd.read_csv(data_url, sep="|", parse_dates=['Date mutation'])
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data

def fillingEmptyCells(cols,med):
    val = cols[0]

    if(pd.isnull(val)):
        #the median
        return med
    else:
            return val

def fill_cols_with_med():
    pass

def plot_bar(X,Y,x_label,y_label,clr):
    fig , ax = plt.subplots()
    plt.bar(X , Y ,color=clr)
    # plt.rcParams["figure.figsize"] = (15,5)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    # plt.title(title)
    st.pyplot(fig)
