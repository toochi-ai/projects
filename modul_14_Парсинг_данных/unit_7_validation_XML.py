import xmlschema


print('---')
my_schema = xmlschema.XMLSchema('animals_2.xsd')
print(my_schema.is_valid('animals_2.xml'))
