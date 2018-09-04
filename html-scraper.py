from bs4 import BeautifulSoup
import requests
import json

url = "https://www.invenglobal.com/blackdesertonline/skill/layer/"
skill_id = 1952

response = requests.get(url+str(skill_id))

json_data = json.loads(response.text)
html_data = json_data['data']

soup = BeautifulSoup(html_data)

print(soup.get_text())