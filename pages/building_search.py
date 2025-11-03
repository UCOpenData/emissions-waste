import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sidebar import init_sidebar
from thefuzz import fuzz
from pages.simplified_data import select_data


init_sidebar()

@st.cache_data
def load_data():
    return pd.read_csv('./datasets/energy_benchmark.csv')

def run_search(data, query):
    departments = pd.DataFrame({"NAME": [x.upper() for x in data]})

    departments['SCORE'] = [fuzz.ratio(query.upper(), name) +
                                 2 * fuzz.partial_ratio(query.upper(), name) for name in departments['NAME']]
    # st.dataframe(departments[['NAME', 'SCORE']])
    
    departments_sorted = departments.sort_values(by = "SCORE", ascending = False)
    
    threshold = 150+ 10*len(query)
    
    departments_filtered = departments_sorted[departments_sorted['SCORE'] > threshold]

    st.write(f"### Found {len(departments_filtered)} Departments")

    for _, row in departments_filtered.iterrows():
        department_url = f"/Department_Data?department_name={row['NAME']}"
        st.markdown(f"{row['NAME']}")
        st.link_button(label = "see more", url = department_url)



building_data = select_data(load_data())

building_data = building_data.dropna(subset=['Property Name'])

buildings_list = sorted(building_data["Property Name"].unique())

search_query = st.text_input("Enter a building's name:", None)

if search_query is not None:
    run_search(buildings_list, search_query)



# s = ['yellow', 'red', 'blue']
# run_search(s, 'yell')

