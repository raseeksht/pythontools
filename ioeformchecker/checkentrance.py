import  json
import requests
from bs4 import BeautifulSoup
import os

url = "https://entrance.ioe.edu.np/Students/Review"
if os.getcwd() == '/home/raseek/Desktop/raseek/ioeformchecker':
	jsonFile = 'a/mydata.json'
else:
	jsonFile = "mydata.json"
f = open(jsonFile)

a = json.load(f)

requests = requests.session()
headers = {
"User-Agent": "Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"
}


if a["fileinput"] == True:
	data =  {
	"LastName":a["lastname"],
	"BirthDateBS":a['BirthDateBS'],
	"BirthDateAD":a["BirthDateAD"],
	"BirtDate":"on",
	"IdentificationNo":a['idNo'],
	"IsPrint":""
	}

else:
	data =  {
	"LastName":input("lastname: "),
	"BirthDateBS":input("BirthDateBS: "),
	"BirtDate":"on",
	"IdentificationNo":input("id no. "),
	"BirthDateAD":input("BirthDateAD: "),
	"IsPrint":""
	}


r = requests.post(url,data=data,headers=headers)
soup  = BeautifulSoup(r.content,'html.parser')
try:
	alld = soup.find("div",class_="status_info")
	res = alld.get_text()
	print(" ".join(res.split()))
	if 'congratulation' in res.lower():
		print('your form has been accepted')
		ch = input('download admission card?(y/n)')
		if ch.lower() =='y':
			data['IsPrint'] = 'True'
			# soup2 = BeautifulSoup(requests.post(url,data=data,headers=headers).content,'html.parser')
			dlLink = "https://entrance.ioe.edu.np/Students/Registration/ExportAdmitCard"
			print('downloading admit card.... this will be quick')
			cardName = 'ioe_admit_card.pdf'
			with open(cardName,'wb') as pdf:
				pdf.write(requests.post(dlLink,headers=headers).content)
			print('Done Downloding')
			print(f'Saved at: {os.getcwd()}/{cardName}')

except Exception as e:
	print("\nok try ma error ako le malai yaha dekhna paryo hai ;)")
	print("name,dob ki id no ko mistake pani huna sakxa hai... check it out\n")
