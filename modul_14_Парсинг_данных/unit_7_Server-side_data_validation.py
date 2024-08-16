from jsonschema import Draft202012Validator

json_data = {"name": "Oleg", "age": 30, "goods": ['apple', 'orange']}
schema = {
    'type': 'object',
    'required': [
        'name', 'goods'
    ],
    'properties': {
        'name': {'type': 'string'},
        'age': {'type': 'integer'},
        'goods': {
            'type': 'array',
            "minItems": 1,
            'prefixItems': [
                {'type': 'string'},
            ],
        },
    }
}

validator = Draft202012Validator(schema)
print(validator.is_valid(json_data))

for error in sorted(validator.iter_errors(json_data), key=str):
    print(error.message)
print('---')

schema = {
    'type': 'array',
    'prefixItems': [
        {
            'type': 'object',
            'required': [
                'room_id', 'room', 'price', 'category', 'extras'
            ],
            'properties': {
                'room_id': {'type': 'integer'},
                'room': {'type': 'string'},
                'price': {'type': 'integer'},
                'category': {'type': 'string'},
                'extras': {
                    'type': 'object',
                    'required': [
                        'meals', 'services'
                    ],
                    'properties': {
                        'meals': {
                            'type': 'array',
                            'prefixItems': [
                                {'type': 'integer'}
                            ]
                        },
                        'services': {
                            'type': 'array',
                            'prefixItems': [
                                {'type': 'integer'}
                            ]
                        }
                    }
                },
            }
        },
    ],
}

validator = Draft202012Validator(schema)
print(validator.is_valid(json_data))
