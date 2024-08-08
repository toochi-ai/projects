import requests
import json

response = requests.get(
    'https://catfact.ninja/fact',
    headers={
        'accept': 'application/json'
    }
)

print(response.text)
print(type(response.text))
print('---')

response = requests.get(
    'https://catfact.ninja/fact',
    headers={
        'accept': 'application/xml'
    }
)

response_text = json.loads(response.text)
print(response_text)
print(type(response_text))
print('-----')
print(response_text['fact'])
print(response_text.keys())
