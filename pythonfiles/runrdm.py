from RedditDataManager import *
import os

def gimmie(input):
	rdm = RedditDataManager(input)
	num = 0
	photoFile = "./"+input+"/"
	if not os.path.exists(photoFile): os.makedirs(photoFile)
	for item in rdm.getDescriptions():
		if item.find("jpg") > 0:
			urllib.urlretrieve(item, photoFile+str(num)+".jpg")
			num += 1
			print item, num

gimmie(raw_input("Enter Subreddit: "))