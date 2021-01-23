import os
from conf import *

lastlink = open('lastlink.txt').read()
print("be sure to replace episode num with")
if lastlink.strip() == '':
	url = input('url: ')
	with open('lastlink.txt','w') as file:
		file.write(url)
else:
	print(f"lastlink: {lastlink}")
	choice = input(f'use lastlink??(y/n): ').lower()
	if choice == "y":
		url = lastlink
	else:
		url = input('url: ')

def getDownloadUrl(ep):

	ep = f"{ep:02d}"
	# print(f"{1:02d}")
	dlurl = url.replace('*9#',ep)
	return dlurl

def askInput():
	startFrom = int(input('start from; '))
	to = int(input('ep; '))
	return startFrom,to

def download(ep):
	dlurl = getDownloadUrl(ep)
	os.system(f'wget {dlurl}')
	print("---downloaded---")


vayo = False
while not vayo:
	try:
		startFrom,to = askInput()
		vayo=True
	except Exception as e:
		print("provide integer value")


for i in range(startFrom,to+1):
	download(i)
