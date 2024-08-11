import json

import requests
import xmltodict

response = requests.get(
    'https://catfact.ninja/fact',
    headers={
        'accept': 'application/json'
    }
)

print(response.text)
print(type(response.text))
print('---')

response = requests.get(
    'https://catfact.ninja/fact',
    headers={
        'accept': 'application/xml'
    }
)

response_text = json.loads(response.text)
print(response_text)
print(type(response_text))
print('-----')
print(response_text['fact'])
print(response_text.keys())
print('---')

car_data = """<car>
               <brand>Kia</brand>
               <color>White</color>
               <engineVolume>1.6</engineVolume>
               <name>Rio</name>
               </car>"""
parsed_data = xmltodict.parse(car_data)
print(parsed_data)
print('---')

car_data = """brand Kia
color white
engine volume 1.6
name Rio"""
parsed_data = {}
for row in car_data.split('\n'):
    row = row.rsplit(' ', 1)
    parsed_data[row[0]] = row[1]
print(parsed_data)
print('---')