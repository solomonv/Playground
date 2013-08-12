from random import random

#Choose random object in list
def choose(x):
	if not isinstance(x, list):
		print "Wrong type, bro."
	else:
		choice = int(random()*len(x))
		return x[choice]

def utf8Toascii(text):
    s = ""
    for c in text:
        if (ord(c)) > 127:
            s += '.'
        else:
            s += c
    return s