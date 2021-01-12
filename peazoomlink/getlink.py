import requests
from bs4 import BeautifulSoup
import re
import json


# make it False if you  want to enter email aand password each time
# True if you're lazy just update email and password in loginInfo.json 
useJsonLogin = True


url  ="https://pea.edu.np/login"

if useJsonLogin == True:
	login_data = json.load(open('loginInfo.json'))
else:
	login_data={
	'email' : input("email: "),
	'password' : input("password: ")
	}

headers = {
"User-Agent": "Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"
}

client = requests.session()
soup = BeautifulSoup(client.get(url).content,'html.parser')
csrftoken = soup.find('input', dict(name='_token'))['value']


login_data["_token"] = csrftoken
r = client.post(url, data=login_data, headers=headers)


soup  = BeautifulSoup(r.content,'html.parser')
try:
	alert = soup.find('div',class_="alert")
	print(" ".join(alert.get_text().split()[:-1]))
except Exception:
	inf = soup.find_all("a",class_="btn-warning")
	for each in inf:
		print(each['href'])


