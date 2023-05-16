import streamlit as st
import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randn(500,2) / [50,50] + [37.76,-122.4]).columns(['lat','lot'])
st.map(df)
