import CSCrawler

def main():
    crawler = CSCrawler.CSCrawler("cookies.txt")
    # crawler.getCidadeList(["Sao Paulo", "Rio de Janeiro", "New York City", "Boston", "Las Vegas"], "cidades_2.csv")
    # crawler.getCidadeList(["Las Vegas"], "cidades_2.csv")
    # crawler.loadCidadeList("cidades_2.csv")

    # for cidade in crawler.cidades:
    #     crawler.getHostList(cidade, per_page=300)

    crawler.loadHostList("hosts.csv")
    crawler.getReviews()
    crawler.initSQLITE("reviews.db")
    crawler.storeReviewsSqlite()

if __name__ == '__main__':
    main()
