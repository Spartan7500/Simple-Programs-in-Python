import os
import shutil
import getpass
import time
from os.path import expanduser


#rudamentary program that will walk through a user's home directory, find photos,
#and then move them to the folder called "Pictures." This was developed on a Windows
#machine, so it hasn't been tested with any other OS.

#TODO: have the program exclude folders 'Program Files' and 'Program Files (x86)'
#Purposely leaving this undone so someone else can contribute for Hacktoberfest!
#Original author: Spartan7500
userHome= expanduser("~")
photoExtensions = {".jpg", ".jpeg", ".png", ".gif", ".TIF", ".raw"}
def movePics():
	os.chdir(os.path.expanduser("~"))
	for root, dirs, files in os.walk("G:/"): #os.getcwd()
		files= [f for f in files if not f[0] == '.']
		dirs[:]= [d for d in dirs if not d[0]=='.']
		for name in files:
			print(name)
			if name.endswith((".jpg", ".JPG", ".jpeg", ".JPEG", ".png", ".PNG", ".gif", ".GIF" ".TIF", ".raw", ".RAW")):
				shutil.move(os.path.join(root,name), os.path.join(os.path.expanduser('~')+"/Pictures", name))

movePics()

