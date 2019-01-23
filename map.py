import folium
import os
import json

#Create a map Object
m = folium.Map(location=[42.3601, -71.0589], zoom_start=12)

#Global Tooltip
tooltip = "Click for more info"

#Create custom icon
logoIcon = folium.features.CustomIcon('favicon.png', icon_size=(50,50))

#Vega data
vis = os.path.join('data','vis.json')

# Geojson data
overlay = os.path.join('data', 'overlay.json')


#Create Markers
folium.Marker([42.363600, -71.099500],
              popup='<strong>Location One</strong>',
              tooltip=tooltip).add_to(m),
folium.Marker([42.333600, -71.109500],
              popup='<strong>Location Two</strong>',
              tooltip=tooltip,
              icon=folium.Icon(icon='cloud',color='red')).add_to(m),
folium.Marker([42.375140, -71.032450],
              popup='<strong>Location Three</strong>',
              tooltip=tooltip,
              icon=logoIcon).add_to(m),
folium.Marker([42.315140, -71.072450],
              popup=folium.Popup(max_width=450).add_child(folium.Vega(json.load(open(vis)),
                                                                      width=450, height=250))).add_to(m)

# Circle Marker
folium.CircleMarker(
    location=[42.466470, -70.942110],
    radius=50,
    popup='New Circled Loc',
    color='#428bca',
    fill=True,
    fill_color='#428bca'
).add_to(m)

# Geojson Overlay
folium.GeoJson(overlay, name='cambridge').add_to(m)
#Generate map
m.save('map.html')