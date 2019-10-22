#create a map with folium and Leaflet.js
import folium
import pandas
import os

def color_producer(elevation):
      if elevation < 1000:
            return 'green'
      elif elevation<2000:
            return 'orange'
      else:
            return 'red'

volcanoesFilePath = 'Volcanoes.txt'
populationFilePath = 'world.json'
if os.path.exists(volcanoesFilePath):
      data = pandas.read_csv(volcanoesFilePath)
else:
      print ('File {} not found'.format(volcanoesFilePath))
      quit()
if os.path.exists(populationFilePath)==False:
      print ('File {} not found'.format(populationFilePath))
      quit()
#read the data into a dataframe with pandas
#convert the LAT series of the dataframe read into a list of latitudes
#same goes for the longitude list

lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
html = """<h4>Volcano information:</h4>
Height: %s m
"""

map = folium.Map(location=[38.58,-99.09], zoom_start=5, tiles="Stamen Terrain")
#add markers

#map.add_child(folium.Marker(location=[38.2,-99.1], popup="Hi I am a Marker", icon=folium.Icon(color='green')))
fgv = folium.FeatureGroup(name="Volcanoes")

#we use zip function to iterate through two or three lists in for
for lt, ln, el in zip(lat, lon, elev):
      iframe = folium.IFrame(html=html % str(el), width=200, height=100)
      fgv.add_child(folium.CircleMarker(#fg.add_child(folium.Marker(
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
fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open(populationFilePath,'r',encoding='utf-8-sig').read(),
style_function=lambda x:
{'fillColor':'green' if x['properties']['POP2005']<10000000
else 'orange' if 1000000<= x['properties']['POP2005']<20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")
