import json
from collections import defaultdict

with open('practice_file_2.json', 'r') as f:
    practice_data = json.loads(f.read())
result_dict = defaultdict(dict)
for item in practice_data:
    result_dict[item['category']]['income'] = (
            result_dict[item['category']].get('income', 0) + item['price'])
    extras = item.get('extras', {})
    result_dict[item['category']]['avg_meal'] = (
        result_dict[item['category']].get('avg_meal', []) + extras['meals'])
    result_dict[item['category']]['services_count'] = (
        result_dict[item['category']].get('services_count', 0) +
        len(extras['services']))

result = []
for k, v in result_dict.items():
    result.append(
        {
            'category': k,
            'income': v['income'],
            'avg_meal': sum(v['avg_meal'])/len(v['avg_meal']),
            'services_count': v['services_count'],
        }
    )

with open('practice_file_2.json', 'w') as f:
    f.write(json.dumps(result, indent=4))
