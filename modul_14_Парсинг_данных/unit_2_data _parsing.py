import requests

response = requests.get(
    'https://catfact.ninja/fact',
    headers={
        'accept': 'application/json'
    }
)

print(response.text)
print(type(response.text))
