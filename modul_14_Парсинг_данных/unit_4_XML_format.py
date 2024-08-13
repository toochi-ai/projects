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
            'name': 'sugar',
            'price': 45,
            'type': 'cane',
            'count': 73,
            'weight': 50
        },
        'salt': {
            'name': 'salt',
            'price': 33,
            'count': 65,
            'weight': 50
        },
        'pepper': {
            'name': 'pepper',
            'price': 56,
            'type': 'black',
            'count': 78,
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

tree = ET.parse('items_new.xml')
root = tree.getroot()

for item in root:
    item.remove(item.find('type'))
    price = int(item.find('price').text)
    count = int(item.find('availability').find('count').text)
    weight = int(item.find('availability').find('weight').text)
    item.find('price').text = str(price * count * weight)
    full_weight = ET.SubElement(item, 'full_weight')
    full_weight.text = str(count * weight)
    item.remove(item.find('availability'))
    item.find('price').tag = 'full_price'

tree = ET.ElementTree(root)
ET.indent(tree)
tree.write('items_new1', encoding='unicode')
