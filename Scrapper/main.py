import requests
from bs4 import BeautifulSoup
import os

RESULT_PATH = './Resultados'
FILE_BASENAME = '_Scrap_Resultado'
COUNTER = 0
NAME_SEARCH = '_SiteG1_'

url = 'https://g1.globo.com/'
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}

site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, features="html.parser")
soupParse = str(soup)

if not os.path.exists(RESULT_PATH):
    os.mkdir(RESULT_PATH)

Files_List = os.listdir(RESULT_PATH)
file_Numbers = [int(file.split('_')[1]) for file in Files_List if file.startswith(FILE_BASENAME)]
if file_Numbers:
    COUNTER = max(file_Numbers) + 1

file_name = f"{NAME_SEARCH}{FILE_BASENAME}_{COUNTER}_.html"
file_path = os.path.join(RESULT_PATH, file_name)
with open(file_path, 'w', encoding='utf-8') as file:
    file.write(soupParse)

print(f'Resultado salvo em: {file_path}')
