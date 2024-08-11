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


animals_dict = {
   'cat': {
           'name': 'Boris',
           'breed': 'Siberian',
           'owner': 'Oleg',
           'age': '4'
       },
   'dog': {
           'name': 'Chorizo',

           'breed': 'Dachshund',
           'owner': 'Elena',
           'age': '3'
       },
   'hamster': {
           'name': 'Arkadiy',
           'breed': 'Dzungarian',
           'owner': 'Elena',
           'age': '1'
   }
}

root = ET.Element('animals', attrib={'home_id': '822494'})
for element, options in animals_dict.items():
    an_element = ET.SubElement(root, element)
    for key, option in options.items():
        opt_element = ET.SubElement(an_element, key)
        opt_element.text = option

tree = ET.ElementTree(root)
tree.write("animals_new_1.xml", encoding='unicode')
