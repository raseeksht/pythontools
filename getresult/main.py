import requests
from bs4 import BeautifulSoup
from conf import *
import sqlite3
from os.path import exists

fromdb = True
# data to be sent along the post request
# sent the key and value accordingly
# <input name="email"> here email is the key and value will be the text you want to send for the key

def firstRun():
	conn2 = sqlite3.connect('result.db')
	c2 = conn2.cursor()
	c2.execute('create table if not exists students (`symbol` text,`name` text,`result` text)')
	return c2



def getDataForPostReq(arr):
	#data to send might differ, ccheck it out
	data ={
		'symbol':arr[2],
		'name':arr[1]
	}
	return data


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



if __name__ == '__main__':
	client = requests.session()
	if tokenRequired == True:
		token = BeautifulSoup(client.get(url,headers=headers).content,'html.parser').find('input',{'name':tokenName})['value']
		data[tokenName] = token
	
	if multipleUrl == True:
		finalUrl = url2
	else:
		finalUrl = url
		# soup = BeautifulSoup(client.post())

	if fromdb == True:
		conn = sqlite3.connect("students.db")
		c = conn.cursor()
		c.execute("select * from students")
		res = c.fetchall()
		for each in res:
			data = getDataForPostReq(each)
			soup = BeautifulSoup(client.post(finalUrl,data=data,headers=headers).content,'html.parser')
			# now use this to find your required content
			# filter the soup to get the result
			result = soup.something.something.string #change it once the result is out

			if not exists('result.db'):
				c2 = firstRun()
			else:
				c2 = sqlite3.connect('result.db').cursor()

			c2.execute(f"insert into students('{each[2]}','{each[1]}','{result}')")
			conn2.commit()
			print(each[1], " ==> ", result)
	






