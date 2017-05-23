from CSCrawler import CSCrawler

crawler = CSCrawler("cookies.txt")
crawler.getCidadeList(["Curitiba", "Recife"])
crawler.loadCidadeList("cidades.csv")

for cidade in crawler.cidades:
	crawler.getHostList(cidade, output="usuarios_{}.csv".format(cidade.nome))