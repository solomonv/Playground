class Website(object):	
	def __init__(self, url):
		self.url = url

	def getUrl(self):
		prefix = "http://"
		return prefix + self.url

	# def getWebpageUrl(self, wpage):
	# 	if wpage[0] == "/":
	# 		return self.getUrl() + wpage
	# 	else:
	# 		return self.getUrl() + "/" + wpage

if __name__ == "__main__":
	reddit = Website("www.reddit.com")
	print reddit.getWebpageUrl("/r/tiltshift")


		



