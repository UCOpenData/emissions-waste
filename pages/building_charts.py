import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from sidebar import init_sidebar

init_sidebar()

# @st.cache_data
# def load_building_data():
#     return pd.read_csv('./datasets/energy_benchmark.csv')

# def year_slider():
#     year = st.slider("Select year",
#                      min_value = 2021,
#                      max_value = 2024,
#                      value = 2021,
#                      step = 1)
#     return year

# def by_construction_year(data):
#     fig, ax = plt.subplots(figsize=(5, 6))
#     ax.set_title("Energy Use by Construction Year")
#     ax.set_xlabel("Year of Construction")
#     ax.set_ylabel("Energy Use Intensity (kBtu / sq ft)")
#     sns.scatterplot(y = data["Source EUI (kBtu/sq ft)"], x = data["Year Built"])
#     st.pyplot(fig)

# buildings = load_building_data()

# date = year_slider()

# by_construction_year(buildings)