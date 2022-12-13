import streamlit as st
import pandas as pd
import numpy as np
import time

#loading data
@st.cache
def load_data(data_url):
    data = pd.read_csv(data_url, sep="|", parse_dates=['Date mutation'])
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data
