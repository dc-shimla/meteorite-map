import folium
from folium import plugins
from folium.plugins import MarkerCluster
from clean_data import CleanData

met_df = CleanData()

m = folium.Map(zoom_start=4, tiles="OpenStreetMap")

cluster_map = MarkerCluster().add_to(m)

# Create an individual marker for each meteorite, adding it to a cluster
for coord in [tuple(x) for x in met_df.to_records(index=False)]:
    ID = coord[1]
    name = coord[0]
    year = coord[6]
    mass = coord[4]
    rec_class = coord[3]
    latitude = coord[7]
    longitude = coord[8]
    
    # Manually generate row index 
    #index = met_df[(met_df["reclat"] == latitude) & (met_df["reclong"] == longitude)].index.tolist()[0]    
    
    # Create custom marker icon | causes size increase of output html file 
    #meteorite_icon = folium.features.CustomIcon('Assets/meteorite.png', icon_size=(80,80))
    
    html = f"""
    <table border="1">
        <tr>
            <th> ID </th>
            <th> Name </th>
            <th> Year </th>
            <th> Mass(g) </th>
            <th> Class </th>
            <th> Latitude </th>
            <th> Longitude </th>
        </tr>
        <tr>
            <td> {ID} </td> 
            <td> {name} </td>
            <td> {year} </td>
            <td> {mass} </td>
            <td> {rec_class} </td>
            <td> {latitude} </td>
            <td> {longitude} </td>
        </tr>
    </table>"""
    iframe = folium.IFrame(html=html, width=375, height=125)
    popup = folium.Popup(iframe, max_width=375)

    folium.Marker(location=[latitude, longitude], popup=popup).add_to(cluster_map)

cluster_map.save("meteorite_cluster_map.html")
  