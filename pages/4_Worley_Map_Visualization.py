import streamlit as st
import folium
from folium import plugins
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from geopy.geocoders import Nominatim
from folium.plugins import Search
from streamlit_folium import st_folium
import branca
import base64
import io


from geopy.extra.rate_limiter import RateLimiter

geolocator = Nominatim(user_agent="applicator")
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=2)
m=folium.Map()
colors = [
    'red',
    'blue',
    'gray',
    'darkred',
    'lightred',
    'orange',
    'beige',
    'green',
    'darkgreen',
    'lightgreen',
    'darkblue',
    'lightblue',
    'purple',
    'darkpurple',
    'pink',
    'cadetblue',
    'lightgray',
    'black'
    'red',
    'blue',
    'gray',
    'darkred',
    'lightred',
    'orange',
    'beige',
    'green',
    'darkgreen',
    'lightgreen',
    'darkblue',
    'lightblue',
    'purple',
    'darkpurple',
    'pink',
    'cadetblue',
    'lightgray',
    'black'
]

ETlist = pd.read_excel('Worley_ET_Register.xlsx',sheet_name=None)
#
marker_cluster = folium.plugins.MarkerCluster().add_to(m)   
features={}
i=0

if i==0:
    for name1,sheet in ETlist.items():
        globals()[name1] = sheet
    #    globals()["marker_cluster%s"%i] = folium.plugins.MarkerCluster().add_to(m)   
        try:
            for index,row in globals()[name1].iterrows():
                #print(index,row["Project"])
                text = f"""
                <h1><b> {row.Project} </b></h1><br>
                <p style="text-align:left;">Customer: {row.Customer}</p>
                <p style="text-align:left;">Worley Services Provided: {row.Services}</p> 
                <p style="text-align:left;">Technology: {row.Technology}</p> 
                <p style="text-align:left;">Description: {row.Description}
                            """
                iframe = branca.element.IFrame(html=text, width=500, height=300)
                popup = folium.Popup(iframe,max_width=500)
                mark = folium.Marker(
                    location=[row["lat"],row["lon"]],
                    popup=popup,
                    tooltip = row["Project"],
                    icon=folium.Icon(color=colors[i]),
                    Name=row["Project"])
    #            mark.add_to(eval("marker_cluster%s"%i))
                mark.add_to(marker_cluster)
        except:
            pass


        
    #    features[name1] = folium.FeatureGroup(name=name1)
    #    features[name1].add_child(marker_cluster)
    #    features[name1].add_to(m)
    #    eval("marker_cluster%s"%i).add_to(m)        
        i+=1

servicesearch = Search(
        layer=marker_cluster,
        search_label="Name",
        placeholder='Search for a Project',
        collapsed=False,
        ).add_to(m)
    
folium.LayerControl().add_to(m)
    
draw = folium.plugins.Draw()
draw.add_to(m)

#st.set_page_config(layout="wide")

streamlit_style = """
			<style>
			@import url('https://fonts.googleapis.com/css2?family=Titillium+Web');
			html, body, [class*="css"]  {
			font-family: 'Titillium Web', sans-serif;
			}
			</style>
			"""
st.markdown(streamlit_style, unsafe_allow_html=True)

# Customize page title
st.title("*Global Visualization Tool for Asset Management*")
st.subheader("Institutionalising Disruptive Thinking & Breakthrough")


with st.sidebar:
    st.sidebar.image: st.sidebar.image("Worley_Logo_2019_RGB_large.png", use_column_width=True)
    st.sidebar.title("**About**")
    st.sidebar.write(
    """
    This multipage app details and demonstrates the functionality and technical requirements of the Worley Portfolio Management Framework.
    """
    )

markdown = """
The Global Visualization Tool for Asset Management is an application for the visualization of project and portfolio related assets - including production facilities, offices, supply and transportation networks, and project locations.

"""

st.markdown(markdown)


st_data = st_folium(m, width=1200,height=1500)
#m.save('WorleyET.html')
                