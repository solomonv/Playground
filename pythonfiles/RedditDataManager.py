from xml.dom.minidom import parseString
from sols_utils import utf8Toascii
from Reddit import *
import urllib2
import urllib

class RedditDataManager(object):

	def __init__(self, _subReddit):
		dom = parseString(self.readSubreddit(_subReddit))
		lChannelDom = dom.getElementsByTagName("channel")#list of channels
		dom_channel = lChannelDom[0]#first channel
		self.lItemDom = dom_channel.getElementsByTagName("item")

	def readSubreddit(self, subredditName):
		subReddit = Reddit(subredditName)
		hdr = {'User-Agent' : 'Firefox'}
		req = urllib2.Request(subReddit.getSubredditRssUrl(), headers=hdr)
		html = urllib2.urlopen(req).read()#opens and reads the info we grab from the subreddit
		return html

	def getTitlefromItem(self, dom_item):
	    lTitleDom = dom_item.getElementsByTagName("title")
	    dom_title = lTitleDom[0]
	    return dom_title.firstChild.data

	def getTitles(self):
		titleList = []
		for dom_item in self.lItemDom:
			title = self.getTitlefromItem(dom_item)
			titleList.append(utf8Toascii(title))
		return titleList
	
	def getDescriptionsfromItem(self, dom_item):
		lDescriptionDom = dom_item.getElementsByTagName("description")
		dom_description = lDescriptionDom[0]
		return dom_description.firstChild.data

	def getDescriptions(self):
		descriptionList = []
		for dom_item in self.lItemDom:
			description = self.getDescriptionsfromItem(dom_item)
			description = utf8Toascii(description)
			description = self.parseDescription(description)
			descriptionList.append(description)
		return descriptionList

	def parseDescription(self, description):
		firstParsedDesc = str(description).split("[link]")
		s = firstParsedDesc[0]
		linkIndex = s.rfind("http")
		#print linkIndex, s
		return s[linkIndex:-2]


if __name__ == "__main__":
	rdm = RedditDataManager("tiltshift");
	rdm2 = RedditDataManager("aww")
	#print rdm.getTitles()
	#print rdm2.getTitles()
	# for item in rdm.getDescriptions():
	# 	print "==========================\n" + item
	#print rdm.parseDescriptions()
	num = 0
	for item in rdm.getDescriptions():
		if item.find("jpg") > 0:
			urllib.urlretrieve(item, str(num)+".jpg")
			num += 1
			print item, num
			