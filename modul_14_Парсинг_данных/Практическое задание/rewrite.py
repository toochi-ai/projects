import json

with open('practice_file_1.json', 'r') as f:
    practice_data = json.loads(f.read())
result = []
for item in practice_data:
    p_data = item.get('personal_data')
    result.append(
        {
            'surname': p_data.get('surname'),
            'phone': p_data.get('credentials', {}).get('phone')
        }
    )

with open('practice_resp_1.json', 'w') as f:
    f.write(json.dumps(result, indent=4))
