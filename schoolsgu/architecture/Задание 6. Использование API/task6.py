import json

from requests import get

params = {'apikey': '09ca753d-60dc-426c-a50b-a92981f66d17',
          'geocode': input('Введите адрес или координаты объекта:\n'),
          'sco': 'latlong',
          'format': "json"}
response = get('http://geocode-maps.yandex.ru/1.x/', params=params)
if response.status_code == 200:
    response_json = response.json()
    with open('response.json', 'w', encoding='utf-8') as file:
        json.dump(response_json, file, ensure_ascii=False, indent=2)
    found_objects = response_json['response']['GeoObjectCollection']['featureMember']
    if found_objects:
        geo_object = found_objects[0]['GeoObject']
        address = geo_object['metaDataProperty']['GeocoderMetaData']['Address']
        try:
            geo_object_address = f"{address['formatted']}, {address['postal_code']}"
        except KeyError:
            geo_object_address = address['formatted']
        longitude, latitude = geo_object['Point']['pos'].split()
        geo_object_coordinates = f'{latitude}, {longitude}'
        print(f'Адрес объекта: {geo_object_address}\n'
              f'Координаты объекта: {geo_object_coordinates}')
        params = {'ll': f'{longitude},{latitude}',
                  'spn': '0.01,0.01',
                  'l': 'map'}
        response = get('https://static-maps.yandex.ru/1.x/', params=params)
        with open('map.png', 'wb') as file:
            file.write(response.content)
    else:
        print('Не найдено ни одного объекта.')
else:
    print(f'{response.status_code} {response.reason}')
