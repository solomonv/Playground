from Website import *

class Reddit(object):
	def __init__(self, subReddit):
		self.subReddit = subReddit		

	def getSubredditRssUrl(self):
		reddit = Website("www.reddit.com/")
		return reddit.getUrl() + "r/" + self.subReddit + "/.rss"

if __name__ == "__main__":
	tiltshift = Reddit("tiltshift")
	print tiltshift.getSubredditUrl()

