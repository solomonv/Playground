from xml.dom.minidom import parseString
from sols_utils import utf8Toascii
from Reddit import *
import urllib2

 #-------------------------------
def readSubreddit(subredditName):
	#change to access specific subreddit
	subReddit = Reddit(subredditName)
	#What the website thinks we're using as a browser
	hdr = {'User-Agent' : 'Firefox'}
	#rss url of reddit subreddit
	req = urllib2.Request(subReddit.getSubredditRssUrl(), headers=hdr)
	#opens and reads the info we grab from the subreddit
	html = urllib2.urlopen(req).read()
	return html

def getTitlefromItem(dom_item):
    lTitleDom = dom_item.getElementsByTagName("title")
    dom_title = lTitleDom[0]
    return dom_title.firstChild.data

#loops through the list of dom_item and passes them to printTitlefromItem
def printTitles():
    for dom_item in lItemDom:
        print utf8Toascii(getTitlefromItem(dom_item))

#----------------------------------------------------
dom = parseString(readSubreddit("halifax")) #Change subreddit here

lChannelDom = dom.getElementsByTagName("channel")#list of channels
dom_channel = lChannelDom[0]#first channel
lItemDom = dom_channel.getElementsByTagName("item")#list of Items in channel 1

printTitles()