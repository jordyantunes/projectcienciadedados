from http import cookiejar
import urllib
from bs4 import BeautifulSoup

class DataFetcher:
	def __init__(self, cookieFile=None):
		if cookieFile is not None:
			cookies = cookiejar.MozillaCookieJar(cookieFile)
			cookies.load()
			cookieProcessor = urllib.request.HTTPCookieProcessor(cookies)
			self.opener = urllib.request.build_opener(cookieProcessor)
		else:
			cookies = None
			self.opener = urllib.request.build_opener()

	def getItems(self, url, identifier, className=None):
		r = self.opener.open(url).read()
		soup = BeautifulSoup(r, "html.parser")
		return soup.find_all(identifier, className)


	def getSoup(self, url):
		r = self.opener.open(url).read()
		soup = BeautifulSoup(r, "html.parser")
		return soup
