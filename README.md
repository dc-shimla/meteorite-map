# Meteorite Map

Meteorite Map is a web mapping application. It imports meteorite landings dataset from NASA’s open data portal via API endpoint. These landings are then cleaned, clustered based on geographical locations and then plotted on to a map.

# Getting Started

### Prerequisites

Packages:
* [requests](https://pypi.org/project/requests/)
* [pandas](https://pypi.org/project/pandas/) 
* [folium](https://pypi.org/project/folium/)  

### Installation

Download the .zip of the github repository. Open meteorite_cluster_map.html in your internet browsing application to see the generated map. 

### Running the application

To re-generate meteorite_cluster_map.html, save any changes made to import_data.py, clean_data.py and map_data.py. Then run map_data.py in the terminal using the following command:

```
python3 create_map.py
```
This will re-generate meteorite_cluster_map.html, reflecting any changes that have been made.

# Live Demo
http://www.mycloudcondo.com/projects/meteorite-map/meteorite_cluster_map.html

# Author
* Dhruv Chaudhary - www.mycloudcondo.com

# License
This project is licensed under the MIT License.
