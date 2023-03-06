# Задание №1
# import requests
# from pprint import pprint
# import json
# url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
# response = requests.get(url)
# all_heroes_list = response.json()
# # pprint(all_heroes_list)
# # pprint(response.json())
# heroes_list = ['Hulk', 'Captain America', 'Thanos']
# heroes_dict = {}
# for name in all_heroes_list:
#     if name['name'] in heroes_list:
#         heroes_dict[name['name']] = name['powerstats']['intelligence']
# print(heroes_dict)
# res = max(heroes_dict, key = heroes_dict.get)
# print(f"Самый умный из супергероев {res}")

# Задание №2

import requests
import json
from pprint import pprint

with open('tokenyandex.txt', 'r') as file_object:
    token = file_object.read().strip()
class YaUploader:
    def __init__(self, token: str):
        self.token = token


    def upload(self, file_path: str):
        file_list = 'testing.txt'
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        params = {"path": file_path, "overwrite": "true"}
        headers = {'Content-Type': 'application/json', 'Authorization': token}
        response = requests.get(upload_url, headers=headers, params=params)
        json_resp = response.json()
        href = json_resp.get('href')
        resp = requests.put(url=href, data=open(file_list, 'rb'))
        # resp.raise_for_status()
        pprint(resp.status_code)

if __name__ == '__main__':
# Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = ('lessons/test.txt')
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)

# задание 3
# url = "https://api.stackexchange.com/2.2/questions"
# params = {'site':'stackoverflow.com', 'sort':'creation', 'fromdate':'2023-03-03', 'todate':'2023-03-05', 'tagget':'Python' }
# response = requests.get(url, params=params)
# res = response.json()
# # pprint(response)
# # pprint(res)
