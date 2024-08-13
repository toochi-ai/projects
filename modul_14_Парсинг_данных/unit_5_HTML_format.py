import json
import requests
from bs4 import BeautifulSoup
from selenium import webdriver


def parse_html(html_text):
    link_soup = BeautifulSoup(html_text, 'html.parser')
    plant_dict = {'soil': None, 'size': None}
    table_about_plant = link_soup.find('div', class_='jn1ow0-0 bqYbNV')
    lines_with_tr = table_about_plant.find_all('tr')
    for tr in lines_with_tr:
        lines_with_th = tr.find('th').text
        if lines_with_th == 'Почва':
            plant_dict['soil'] = tr.find('td').text
        if lines_with_th == 'Размер':
            plant_dict['size'] = tr.find('td').text
    return plant_dict


result = {}
for page_num in range(1, 2):
    url = (f'https://leplants.ru/choose-plant/?utm_source=feature&utm_medium=choose&utm_campaign=share'
           f'&lfilter=type%3A7&page={page_num}&sort=-viewers')
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    for link in soup.find_all('a', class_='title'):
        link_response = requests.get(
            f'https://leplants.ru{link.get('href')}'
        )
        result[link.text] = parse_html(link_response.text)

print(json.dumps(result, indent=4, ensure_ascii=False))

url = ('https://leplants.ru/choose-plant/?utm_source=feature&utm_medium=choose&utm_campaign=share'
       '&lfilter=type%3A7&page=2&sort=-viewers')
driver = webdriver.Chrome()
driver.get(url)

print(driver.page_source)
driver.quit()

print('---')

response = requests.get(
    'https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html'
)
soup = BeautifulSoup(response.text, 'html.parser')
element = soup.find('section', id='io-tools-text-csv-hdf5')
element = element.find('tbody')
result = []
for tr_el in element.find_all('tr'):
    tds = tr_el.find_all('td')
    result.append(
        {
            'data': tds[1].text,
            'read': tds[2].text,
            'write': tds[3].text
        }
    )
with open('htmlfile.json', 'w') as file:
    file.write(json.dumps(result, indent=4))
