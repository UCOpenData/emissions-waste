import streamlit as st
import pandas as pd
import seaborn as sns

original = pd.read_csv('./datasets/energy_benchmark.csv')

st.dataframe(original)

correct_longitudes = original[original['Longitude'].between(-87.606995, -87.590376)]
correct_longitudes
       
   
