import requests
import xml.etree.ElementTree as ET

url = "http://www.lamma.rete.toscana.it/previ/ita/xml/comuni_web/dati/firenze.xml"
response = requests.get(url)
root = ET.fromstring(response.content)

city_desc_element = root.find(".//comune")
update_datetime_element = root.find(".//aggiornamento")
day_1_element = root.find(".//previsione[@idday='1']")
day_1_min_temp_element = day_1_element.find(".//temp[@temp_type='min']")
day_1_max_temp_element = day_1_element.find(".//temp[@temp_type='max']")

city_desc = city_desc_element.text
update_datetime = update_datetime_element.text
day_1_min_temp = int(day_1_min_temp_element.text)
day_1_max_temp = int(day_1_max_temp_element.text)

print(f"Meteo di {city_desc}\nAggiornato al {update_datetime}")
print(f"Temperatura massima: {day_1_max_temp} {'grado' if day_1_max_temp == 1 or day_1_max_temp == -1 else 'gradi'}")
print(f"Temperatura minima: {day_1_min_temp} {'grado' if day_1_min_temp == 1 or day_1_min_temp == -1 else 'gradi'}")


