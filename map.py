import folium

# ! create map object

# m = folium.Map(location=[42.3702, 21.1483], zoom_start=22)

# m = folium.Map(location=[42.37, 21.1483], zoom_start=22, tiles='Stamen Toner')

m = folium.Map(location=[42.37, 21.1483],
               zoom_start=22, tiles='Stamen Terrain')

m.save('index.htm')
