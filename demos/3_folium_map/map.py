import folium.raster_layers
import streamlit as st
from streamlit_folium import st_folium
import folium
from folium.plugins import Draw
from data import data

st.set_page_config(layout='wide')
st.title("Folium Integration with Streamlit")

select_options = [None] + list(range(0, len(data['all_drawings'])))
selected_region = st.selectbox(label='Select region', options=select_options, index=len(data['all_drawings']))
data['selected_region'] = selected_region
data['regions_data'].setdefault(selected_region, {})

if selected_region is not None:
    name = data['regions_data'][selected_region].get('name', "")
    danger = data['regions_data'][selected_region].get('danger', 1)
    data['regions_data'][selected_region]['name'] = st.text_input('Name', value=name, key=f"text_input")
    data['regions_data'][selected_region]['danger'] = st.slider('Danger Level', 1, 100, value=danger, key=f"slider_input")

# Create a folium map object and add draw pluggin
map = folium.Map(location=[data.get('lat', 42.698334), data.get('lng', 23.319941)], zoom_start=data.get('zoom', 14))
draw = Draw(edit_options={'edit': False, 'remove': False}, draw_options={'polyline': False, 'circle': False, 'marker': False, 'circlemarker': False}).add_to(map)

# Add GeoJson selection
for index, drawing in enumerate(data['all_drawings']):
    tooltip_name = data['regions_data'].get(index, {}).get('name')
    tooltip_danger = data['regions_data'].get(index, {}).get('danger')
    tooltip = f"<string>{tooltip_name}</strong><br />{tooltip_danger}"
    if index == data['selected_region']:
        folium.GeoJson(drawing, style_function=lambda f: {'color': 'red'}, tooltip=tooltip, zoom_on_click=True).add_to(map)
    else:
        folium.GeoJson(drawing, style_function=lambda f: {'color': 'blue'}, tooltip=tooltip, zoom_on_click=True).add_to(map)

# Display the map in the Streamlit app
st.write("Select regions.")
map_data = st_folium(map, height=1000, use_container_width=True)
if map_data and map_data.get('all_drawings'):
    data['all_drawings'] += map_data['all_drawings']
    data['zoom'] = map_data['zoom']
    data['lat'] = map_data['center']['lat']
    data['lng'] = map_data['center']['lng']