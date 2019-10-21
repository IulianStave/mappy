#create a map with folium and Leaflet.js
import folium
import pandas

#read the data into a dataframe with pandas
data = pandas.read_csv('Volcanoes.txt')

#convert the LAT series of the dataframe read into a list of latitudes
#same goes for the longitude list

lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
#popupinfo = list(data[""])

html = """<h4>Volcano information:</h4>
Height: %s m
"""

def color_producer(elevation):
      if elevation < 1000:
            return 'green'
      elif elevation<2000:
            return 'orange'
      else:
            return 'red'
map = folium.Map(location=[38.58,-99.09], zoom_start=5, tiles="Stamen Terrain")
#add markers

#map.add_child(folium.Marker(location=[38.2,-99.1], popup="Hi I am a Marker", icon=folium.Icon(color='green')))
fg = folium.FeatureGroup(name="My map")
#for coordinates in [[38.2,-99.1],[37.2,-98.1]]:

#we use zip function to iterate through two lists
for lt, ln, el in zip(lat, lon, elev):
      iframe = folium.IFrame(html=html % str(el), width=200, height=100)
      fg.add_child(folium.CircleMarker(#fg.add_child(folium.Marker(
                            location=[lt, ln],
                            #popup=str(el)+" m",
                            popup=folium.Popup(iframe),
                            icon=folium.Icon(color=color_producer(el)),
                            radius=7,
                            fill_color=color_producer(el),
                            color='grey',
                            fill_opacity=0.7)
                            
            
            )
            #fg.add_child(folium.Polygon)

#load GeoJson data to add a polygon layer
#x represents Features in world.json
fg.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(), 
style_function=lambda x: 
{'fillColor':'green' if x['properties']['POP2005']<10000000 
else 'orange' if 1000000<= x['properties']['POP2005']<20000000 else 'red'}))



map.add_child(fg)
map.save("Map1.html")
