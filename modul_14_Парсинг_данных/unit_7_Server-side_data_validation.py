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
