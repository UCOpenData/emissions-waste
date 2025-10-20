import streamlit as st

def init_sidebar():
    st.sidebar.page_link('pages/building_map.py', label='Building Map')
    st.sidebar.page_link('pages/building_search.py', label='Building Search')
    st.sidebar.page_link('pages/building_charts.py', label='Misc Charts')