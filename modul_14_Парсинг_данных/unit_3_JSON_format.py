import json

with open('cars.json', 'r') as cars_file:  # Открыл файл
    cars_data = cars_file.read()  # Прочитали файл
    cars_data = json.loads(cars_data)  # Десериализовали данные

response_data = []
for car_item in cars_data:
    response_data.append({
        'car_name': f"{car_item.get('brand', '')} {car_item.get('name', '')}",
        'transmission': car_item.get('transmission'),
        'engine_volume': car_item.get('engine', {}).get('volume'),
    })

with open('cars_restructured.json', 'w') as cars_file:
    response_data = json.dumps(response_data, indent=4)
    cars_file.write(response_data)


print(response_data)

cyrillic_data = {
    'Ключ': 'значение',
}

print(json.dumps(cyrillic_data, indent=4, ensure_ascii=False))
