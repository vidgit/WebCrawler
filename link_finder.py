from HTMLParser import HTMLParser
from urlparse import urlparse
from urlparse import urljoin
class LinkFinder(HTMLParser):
	def __init__(self,base_url,page_url):
		self.base_url=base_url
		self.page_url=page_url
		self.links=set()
	def error(self,message):
		pass
	def handle_starttag(self,tag,attrs):
		if tag=='a':
			for (attribute,value) in attrs:
				if attribute=='href':
					url=urljoin(self.base_url,value)
					self.links.add(url)
				#print 'Start Tag:',tag
	def handle_endtag(self,tag):
		print 'End Tag:',tag
	def handle_data(self,data):
		print 'Data:',data
	def page_links(self):
		return self.links

		