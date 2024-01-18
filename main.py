import requests
import xml.etree.ElementTree as ET

url = "http://www.lamma.rete.toscana.it/previ/ita/xml/comuni_web/dati/firenze.xml"

response = requests.get(url)

root = ET.fromstring(response.content)

city_desc_element = root.find(".//comune")
update_datetime_element = root.find(".//aggiornamento")

city_desc_text = city_desc_element.text
update_datetime_text = update_datetime_element.text

print(f"Meteo di {city_desc_text}")
print(f"Aggiornato al {update_datetime_text}")
