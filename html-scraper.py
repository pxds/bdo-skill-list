from bs4 import BeautifulSoup
import requests
import json

def print_skill_info(soup):
	for tr in skill_list.find_all('tr'):
		td_skillname = tr.find('td',{'class':'skillname left'})
		if td_skillname:
			print(td_skillname.find('span').string,
				# for some reason it prints // with one character
				('http:/'+td_skillname.a.get('href')))
			pass

class_id = {"Warrior":"1", "Ranger":"5", "Sorceress":"9", "Berserker":"13", "Tamer":"17", 
			"Musa":"21", "Valkyrie":"25", "Maewha":"22", "Wizard":"29", "Witch":"32",
			"Witch":"32", "Kunoichi":"26", "Ninja":"27", "Dark Knight":" 28", "Striker":"20", "Mystic": "24"}

skill_modifiers = {
	"cc" : ["Stiffness", "Stun", "Knockdown", 
	        "Bound", "Knockback", "Floating", 
	        "Grapple", "Freezing"],
	"armor" : ["Forward Guard", "Super Armor", "Invincible"]
}
# first_skill_id = 1
# last_skill_id = 2773

# populate class skill list
url = "https://www.invenglobal.com/blackdesertonline/skill/"

response = requests.get(url+class_id["Valkyrie"])
soup = BeautifulSoup(response.text, features="html.parser")

skill_list = soup.main.find("div", {"class":"content skillList"})

print_skill_info(skill_list)