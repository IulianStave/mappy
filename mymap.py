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


map = folium.Map(location=[38.58,-99.09], zoom_start=5, tiles="Stamen Terrain")
#add markers

#map.add_child(folium.Marker(location=[38.2,-99.1], popup="Hi I am a Marker", icon=folium.Icon(color='green')))
fg = folium.FeatureGroup(name="My map")
#for coordinates in [[38.2,-99.1],[37.2,-98.1]]:

#we use zip function to iterate through two lists
for lt, ln, el in zip(lat, lon, elev):
      iframe = folium.IFrame(html=html % str(el), width=200, height=100)
      fg.add_child(folium.Marker(
                            location=[lt, ln],
                            #popup=str(el)+" m",
                            popup=folium.Popup(iframe),
                            icon=folium.Icon(color='green')
                            )
            )
map.add_child(fg)



map.save("Map1.html")
