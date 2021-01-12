import pyperclip
import time
import platform
import os

def giveCommand(command):
	os.system(command)


if platform.system() == 'Windows':
	giveCommand('cls')
else:
	giveCommand('clear')

filename = "blackclover.txt"
print("""A tool to automate(partially) list making process.
Just copy text or anything that you want to add to the list(media file excluded)
you don't have to paste aything, i'll do it for you ;)
	""")

input('''if you have  something in clipboard that you don't want in list
then select something that you wanna add in the list
Enter to continue: ''')

temp=""
while True:
	clip = pyperclip.paste()
	if clip == temp:
		time.sleep(1)
	else:
		with open(filename,"a") as f:
			f.write(clip+"\n")
			print(clip+"\n")
		time.sleep(1)
		temp = clip

