from http import cookiejar
import urllib
from bs4 import BeautifulSoup
import json

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
		try:
			r = self.opener.open(url).read()
			soup = BeautifulSoup(r, "html.parser")
			return soup
		except ExceptionI:
			print(ExceptionI)
			return None

	def getJson(self, url):
		return json.loads(self.opener.open(url).read())