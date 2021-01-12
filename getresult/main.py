import requests
from bs4 import BeautifulSoup
import sqlite3

url  ="https://linkhere.com/path-if-required"


headers = {
"User-Agent": "Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"
}
fromdb = True

def getResult(symbol):
	data  = {
	"symbol":symbol,
	# 'dob':""
	"submit1":""
	}

	#make post req and get html
	x = requests.post(url,data=data,headers=headers)
	soup = BeautifulSoup(x.content,'html.parser')

	# get desired info  change class and//or raag corespondingly
	a = soup.find("a", class_="contact-method")
	print(a.b.string)

if fromdb == True:
	conn = sqlite3.connect("students.db")
	c = conn.cursor()
	c.execute("select * from students")
	res = c.fetchall()
	for each in res:
		symbol = each[2]
		name = each[1]
		result = getResult(symbol)
		# do what  you  want with the data
else:
	symbol input("symbol: ")
	dob  = input("dob: ")
	result = getResult(symbol)
	# do whaat ever you  waant with this data



# # get  the html
# x = requests.post(url,data=data,headers=headers)
# soup = BeautifulSoup(x.content,'html.parser')

# # find the required tag  that has rrequired information





