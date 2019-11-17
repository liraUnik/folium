import folium

# ! create map object

m = folium.Map(location=[42.3702, 21.1483], zoom_start=22)

m.save('index.htm')
