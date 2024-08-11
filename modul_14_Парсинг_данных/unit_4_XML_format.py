import xmltodict
import xml.etree.ElementTree as ET


with open('animals.xml', 'r') as animals_file:
    animals_data = animals_file.read()
    parsed_data = xmltodict.parse(animals_data)
    print(parsed_data)

animals_dict = {
   'animals': {
       '@home_id': '822494',
       'cat': {
           'name': 'Boris',
           'breed': 'Siberian',
           'owner': 'Oleg',
           'age': '4'
       },
       'dog': {
           'name': 'Сhorizo',
           'breed': 'Dachshund',
           'owner': 'Elena',
           'age': '3'
       },
       'hamster': {
           'name': 'Arkadiy',
           'breed': 'Dzungarian',
           'owner': 'Elena',
           'age': '1'}
   }
}

with open('animals_new.xml', 'w') as animals_file:
    parsed_data = xmltodict.unparse(animals_dict, pretty=True)
    animals_data = animals_file.write(parsed_data)
