from geopy.geocoders import Nominatim
from DataFetcher import DataFetcher
from host import Host
import csv
import pymysql.cursors
import sqlite3

class CSCrawler(DataFetcher):
	"""
		Implementa um crawler para o site Couchsurfing a fim de obter informações de usuários (reviews)
	"""

	def initDB(self, host, user, password, db):
		self.connection = pymysql.connect(host=host,
                             user=user,
                             password=password,
                             db=db,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

	def initSQLITE(self, filename):
		self.connection = sqlite3.connect(filename)


	def storeReviews(self):
		try:
		    with self.connection.cursor() as cursor:
		        # Create a new record
		        sql = "INSERT INTO `reviews` (`id_user`, `review`) VALUES (%s, %s)"

		        for host in self.hosts:
		        	for review in host.reviews:
		        		cursor.execute(sql, (host.id, review))

		    # connection is not autocommit by default. So you must commit to save
		    # your changes.
		    self.connection.commit()
		finally:
		    self.connection.close()

	def storeReviewsSqlite(self):
		try:
			cursor = self.connection.cursor()
			sql = "INSERT INTO `reviews` (`id_user`, `review`, `cidade`) VALUES (?,?,?)"
			for host in self.hosts:
				cursor.executemany(sql, [ (host.id, review, host.cidade) for review in host.reviews ])
		    # connection is not autocommit by default. So you must commit to save
		    # your changes.
			self.connection.commit()
		finally:
		    self.connection.close()

	def loadHostList(self, filename):
		"""
			Carrega um arquivo csv com dados de cidades
		"""
		with open(filename, "r") as arquivo:
			reader = csv.DictReader(arquivo)
			self.hosts = [ Host(row["nome"], row["id"], row["endereco"], row["cidade"]) for row in reader ]

	def getReviews(self):
		# out = open("html.html", "w")
		for host in self.hosts:
			data = self.getSoup(u"https://www.couchsurfing.com" + host.endereco + "/references")
			campo_reviews = data.find("div", { "class" : "box-content mod-ovh"})

			print("Pegando reviews de {}".format(host.nome))

			if campo_reviews is not None:
				reviews = [ r.find("p").text for r in campo_reviews.find_all("div", {"data-truncate-more" : "Read more"})]
				host.reviews = reviews

			print("Num de reviews {}".format(len(host.reviews)))

	def getHostList(self, cidade, kwargs={}, output="hosts.csv", per_page=100):
		"""
			Obtem uma lista de hosts de um local no expedia
		"""
		with open(output, "w", encoding='utf-8') as arquivo:
			arquivo_usuarios = csv.DictWriter(arquivo, fieldnames=["nome","id","endereco","cidade"], lineterminator='\n')
			arquivo_usuarios.writeheader()

			data = self.getItems(u"https://www.couchsurfing.com/members/hosts?utf8=%E2%9C%93&search_query={}&latitude={}&longitude={}&country=Brazil&region=south-america&date_modal_dismissed=true&arrival_date=&departure_date=&num_guests=1&has_references=1&can_host%5Baccepting_guests%5D=1&last_login=Anytime&join_date=Anytime&gender=All&min_age=&max_age=&languages_spoken=&interests=&smoking=No+Preference&radius=10&keyword=&host_sort=Best+Match&button=&perPage={}".format(cidade.nome, cidade.latitude, cidade.longitude, per_page), "h3", className="-name")
			for user in data:
				host = Host(user.a.string, user.a['href'][len("/users/"):], user.a['href'], cidade)
				print("{} {} {} {} ".format(host.nome, host.id, host.endereco, host.cidade.nome))
				arquivo_usuarios.writerow({"nome" : host.nome, "id" : host.id, "endereco" : host.endereco, "cidade" : host.cidade.nome})


	def __init__(self, cookiesFile=""):
		super().__init__(cookiesFile)

	def loadCidadeList(self, filename):
		"""
			Carrega um arquivo csv com dados de cidades
		"""
		with open(filename, "r") as arquivo:
			reader = csv.DictReader(arquivo)
			self.cidades = [ Cidade(row["cidade"], row["latitude"], row["longitude"], row["endereco"]) for row in reader ]

	def getCidadeList(self, cidades, output="cidades.csv"):
		"""
			Recebe uma lista de cidades e cria um arquivo csv com dados geograficos das cidades
		"""
		with open(output, "w") as arquivo:
			writer = csv.DictWriter(arquivo, fieldnames=["cidade","latitude","longitude", "endereco"], lineterminator='\n')
			writer.writeheader()

			for nome_cidade in cidades:
				cidade = CidadeFactory.getCidade(nome_cidade)
				writer.writerow({'cidade' : cidade.nome, 'latitude' : cidade.latitude, 'longitude' : cidade.longitude, 'endereco' : cidade.endereco})


class CidadeFactory:
	@staticmethod
	def getCidade(nome):
		geolocator = Nominatim()
		location = geolocator.geocode(nome)
		return Cidade(nome, location.latitude, location.longitude, location.address)

class Cidade:
	def __init__(self, nome, latitude, longitude, endereco):
		self.nome = nome
		self.latitude = latitude
		self.longitude = longitude
		self.endereco = endereco

def main():
	crawler = CSCrawler("cookies.txt")
	crawler.loadHostList("usuarios_Recife.csv")
	crawler.getReviews()
	# crawler.initDB("localhost", "root", "", db)
	crawler.initSQLITE("reviews.db")
	crawler.storeReviewsSqlite()

if __name__ == '__main__':
	main()