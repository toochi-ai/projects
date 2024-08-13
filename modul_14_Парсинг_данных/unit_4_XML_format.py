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

root[0][0].text = 'Basil'
tree = ET.ElementTree(root)
ET.indent(tree)
tree.write("animals_new_1.xml", encoding='unicode')


sq = ET.SubElement(root, 'squirrel')
for k, v in {
    'name': 'Batareyka',
    'breed': 'Aberti',
    'owner': 'Dima',
    'age': '1'
}.items():
    opt = ET.SubElement(sq, k)
    opt.text = v
ET.indent(tree)
tree.write("animals_new_1.xml", encoding='unicode')

items = {
    'items': {
        'sugar': {
            'price': 45,
            'type': 'cane',
            'count': 73,
            'weight': 50
        },
        'salt': {
            'price': 33,
            'count': 65,
            'weight': 50
        }
    }
}

root = ET.Element('items')
for key, element in items['items'].items():
    an_element = ET.SubElement(root, key)
    for key_1, option in element.items():
        opt_element = ET.SubElement(an_element, key_1)
        opt_element.text = str(option)

tree = ET.ElementTree(root)
ET.indent(tree)
tree.write("items.xml", encoding='unicode')
