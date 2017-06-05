import CSCrawler

def main():
    crawler = CSCrawler.CSCrawler("cookies.txt")
    
    # crawler.getCidadeList(["Sao Paulo"], "1_sp.csv")
    crawler.loadCidadeList("1_sp.csv")
    for cidade in crawler.cidades:
        crawler.getHostList(cidade, per_page=10)

    crawler.loadHostList("hosts.csv")
    crawler.getReviewsThreaded()
    crawler.initSQLITE("reviews.db")
    crawler.storeReviewsSqlite()

if __name__ == '__main__':
    main()
