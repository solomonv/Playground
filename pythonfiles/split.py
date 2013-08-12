descriptions = ["aksljd lkjsad kljf /br> <a href = ""www.stuff.com"" </a> [link]BLah jashfsafklj jksalfjhksaf  jkhasflk jsajklfsa"]

def splitAtlink(string):
	splitList = str(string).split("[link]")
	return splitList

lise = splitAtlink(descriptions)
print lise[0].split("/br>")

