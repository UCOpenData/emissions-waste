import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sidebar import init_sidebar
import folium 
from streamlit_folium import st_folium
import geopandas as gpd

init_sidebar()

hyde_park_map = folium.Map(location=[41.7943, -87.5907], zoom_start=15, tiles = "cartodb positron")


folium.Marker(location= [41.78898211, -87.6009439], tooltip = 'Cobb Hall', icon= folium.Icon(color = 'red', icon= ' ')).add_to(hyde_park_map)


gdf = gpd.read_file('https://data.cityofchicago.org/resource/syp8-uezg.geojson')
gdf
st.write(gdf.dtypes)
gdf2 = gdf.drop(columns = ['qc_date', 'edit_date', 'condition_', 'bldg_activ', 'bldg_creat', 'bldg_end_d', 'demolished'])
folium.GeoJson(gdf2).add_to(hyde_park_map)
st_folium(hyde_park_map)
# try:
#     params = st.query_params["lobbyist_id"]
#     activity = pd.read_csv('./datasets/LD_Lobbying_Activity.csv')
#     gifts = pd.read_csv('./datasets/LD_Gifts.csv')
#     lobby_data = pd.read_csv('./datasets/LD_Lobbyists.csv')

#     person_id = int(params)

#     activity_subset = activity[activity["LOBBYIST_ID"] == person_id]
#     gift_subset = gifts[gifts["LOBBYIST_ID"] == person_id]
#     lobbyist_subset = lobby_data[lobby_data["LOBBYIST_ID"] == person_id]

#     if (len(activity_subset) > 0):
#         first_name = activity_subset["LOBBYIST_FIRST_NAME"].iloc[0]
#         last_name = activity_subset["LOBBYIST_LAST_NAME"].iloc[0]
#         st.write(first_name + " " + last_name)
#         if (len(gift_subset) > 0):

#             st.dataframe(gift_subset)

        

#         st.dataframe(activity_subset)

#         activity_by_department(activity_subset)
#     else:
#         first_name = lobbyist_subset["FIRST_NAME"].iloc[0]
#         last_name = lobbyist_subset["LAST_NAME"].iloc[0]
#         st.write(first_name + ' ' + last_name)
#         st.write("No lobbying activity found for this lobbyist")
# except:
#     st.write("Please find a lobbyist in Lobbyist Search")
