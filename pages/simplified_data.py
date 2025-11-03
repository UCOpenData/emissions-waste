import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

original = pd.read_csv('./datasets/energy_benchmark.csv')

st.dataframe(original)

correct_longitudes = original[original['Longitude'].between(-87.606995, -87.590376)]


correct_coordinates = correct_longitudes[correct_longitudes['Latitude'].between(41.784077, 41.795508)]

   
newest_years = correct_coordinates.groupby(by= 'Property Name')['Data Year'].max().reset_index()
st.write(len(newest_years))

target_rows= pd.merge(correct_coordinates,
         newest_years,
         on = ['Property Name', 'Data Year'],
         how = 'inner')
target_rows

st.scatter_chart(data = target_rows, x = 'Longitude', y = 'Latitude')

def select_data(df):
    correct_longitudes = df[df['Longitude'].between(-87.606995, -87.590376)]
    correct_coordinates = correct_longitudes[correct_longitudes['Latitude'].between(41.784077, 41.795508)]
    newest_years = correct_coordinates.groupby(by= 'Property Name')['Data Year'].max().reset_index()        
    target_rows= pd.merge(correct_coordinates,
         newest_years,
         on = ['Property Name', 'Data Year'],
         how = 'inner')
    return target_rows

test = select_data(original)
test
