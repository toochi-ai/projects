import json

cyrillic_data = {
    'Ключ': 'значение',
}

print(json.dumps(cyrillic_data, indent=4, ensure_ascii=False))
