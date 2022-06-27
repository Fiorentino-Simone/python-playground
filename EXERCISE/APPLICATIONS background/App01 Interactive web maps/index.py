import folium;

#usiamo folium come libreria per creare una mappa
#folium inoltre va a gestire la creazione dei file html, css, JS per la creazione della mappa
#inizializziamo una mappa
#tiles = "Stamen Terrain" oppure quello di default

map = folium.Map(location = [45.696054, -121.848331], zoom_start=10) #costruttore per creare la mappa
#adding a marker on this map
#usiamo la feature group per creare una lista di marker
fg = folium.FeatureGroup(name="Prova marker")
#per aggiungere un marker
fg.add_child(folium.Marker(location=[44.696054, 7.848331], popup="My Home", icon=folium.Icon(color='red')))
#per aggiungere una linea
fg.add_child(folium.PolyLine(locations=[[44.696054, 7.848331], [23.696054, 14.848331]], color='red'))
#per aggiungere una poligono
fg.add_child(folium.Polygon(locations=[[44.696054, 7.848331], [23.696054, 14.848331], [60.696054, 21.848331]], color='red'))
#aggiungiamo la feature group alla mappa

#proviamo ad utilizzare un for loop
for coordinates in [[38.2, -99.1], [37.2, -95.1], [41.2, -97.1]]:
    fg.add_child(folium.Marker(location=coordinates, popup="My Home", icon=folium.Icon(color='red')))

#map.add_child(fg) #aggiungiamo la feature group alla mappa cosi da rendere più ordinato il codice

#ricordo usare sempre la help in caso non ci ricordassimo cosa fa quel costruttore o funzione
#ex: help(folium.Map())

#andiamo adesso a prendere marker dal file csv volcanoes.csv
#per farlo usiamo la libreria pandas
import pandas
#per prendere i dati dal file csv
data = pandas.read_csv("Volcanoes.csv")
#per prendere le coordinate dal file csv
lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])
location = list(data["LOCATION"])
elev = list(data["ELEV"])

fg_vulcanos = folium.FeatureGroup(name="Volcanoes")


def extractColor(elev):
    if(elev > 0 and elev < 1000):
        return 'green'
    elif(elev >= 1000 and elev < 3000):
        return 'orange'
    elif(elev >= 3000):
        return 'red'

#zip permette di creare una lista di coppie di elementi tra due liste
for i , j, name, loc, elev in zip(lat, lon, name, location, elev):
    htmlString = """
        <h4>Volcano name: """ +  name + """ <h4> 
        <p>Location: """ + loc + """ </p>
        <p>Height: """ + str(elev) + """ </p> 
    """
    fg_vulcanos.add_child(folium.CircleMarker(location=[i , j], radius=10, popup=htmlString, fill_color=extractColor(elev), color='grey', fill_opacity=0.7));

fg_population = folium.FeatureGroup(name="Population")
#lui va a leggere il file json e va a modificare la mappa con la tiipologia inserita in type del json
fg_population.add_child(folium.GeoJson(data = open('world.json', 'r', encoding='utf-8-sig').read(), 
    style_function  = lambda x: {
        'fillColor':'green' if x['properties']['POP2005'] < 10000000 
        else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 
        else 'red'
    }))

#add a layer control to the map
map.add_child(fg)
map.add_child(fg_vulcanos)
map.add_child(fg_population)
map.add_child(folium.LayerControl())
map.save("index.html") #salva la mappa in un file html


