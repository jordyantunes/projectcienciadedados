from http import cookiejar
import urllib
from bs4 import BeautifulSoup

class Host:
	def __init__(self, nome, endereco):
		self.nome = nome
		self.endereco = endereco
		self.review = []

# carregar cookies
cookies = cookiejar.MozillaCookieJar("cookies.txt")
cookies.load()
cookieProcessor = urllib.request.HTTPCookieProcessor(cookies)
opener = urllib.request.build_opener(cookieProcessor)

# fetch pagina web
r = opener.open("https://www.couchsurfing.com/members/hosts/2?city=Curitiba&country=Brazil&latitude=-25.4244287&longitude=-49.2653819&perPage=10&region=south-america&search_query=Curitiba%2C+Brazil").read()

soup = BeautifulSoup(r, "html.parser")

hosts_soup = soup.find_all("h3", "-name")
hosts = []

enderecos = open("enderecos.txt", "w")
pagina = open("pagina.html", "wb")

for host in hosts_soup:
	h = Host(host.a.string, host.a['href'])
	hosts.append(h)
	enderecos.write("http://www.couchsurfing.com" + h.endereco + "\n")

for host in hosts:
	url = "http://www.couchsurfing.com" + host.endereco + "/references"
	print(url)
	opener = urllib.request.build_opener(cookieProcessor)
	r = opener.open(url).read()
	pagina.write(r)
	soup = BeautifulSoup(r, "html.parser")
	break

enderecos.close()
pagina.close()