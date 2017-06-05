import CSCrawler

def main():
    crawler = CSCrawler.CSCrawler("cookies.txt")
    
    # crawler.getCidadeList(["Sao Paulo"], "1_sp.csv")
    crawler.loadCidadeList("1_sp.csv")
    for cidade in crawler.cidades:
        crawler.getHostList(cidade, per_page=300)

    crawler.loadHostList("hosts.csv")
    crawler.getReviewsThreaded()
    crawler.initSQLITE("reviews.db")
    crawler.storeReviewsSqlite()
    

    crawler = CSCrawler.CSCrawler("cookies.txt")
    # crawler.getCidadeList(["Rio de Janeiro"], "2_rio.csv")
    crawler.loadCidadeList("2_rio.csv")
    
    for cidade in crawler.cidades:
        crawler.getHostList(cidade, per_page=300)

    crawler.loadHostList("hosts.csv")
    crawler.getReviewsThreaded()
    crawler.initSQLITE("reviews.db")
    crawler.storeReviewsSqlite()


    crawler = CSCrawler.CSCrawler("cookies.txt")
    # crawler.getCidadeList(["New York City"], "3_nyc.csv")
    crawler.loadCidadeList("3_nyc.csv")
    for cidade in crawler.cidades:
        crawler.getHostList(cidade, per_page=300)

    crawler.loadHostList("hosts.csv")
    crawler.getReviewsThreaded()
    crawler.initSQLITE("reviews.db")
    crawler.storeReviewsSqlite()


    crawler = CSCrawler.CSCrawler("cookies.txt")
    # crawler.getCidadeList(["Boston"], "4_bos.csv")
    crawler.loadCidadeList("4_bos.csv")
    for cidade in crawler.cidades:
        crawler.getHostList(cidade, per_page=300)

    crawler.loadHostList("hosts.csv")
    crawler.getReviewsThreaded()
    crawler.initSQLITE("reviews.db")
    crawler.storeReviewsSqlite()

    crawler = CSCrawler.CSCrawler("cookies.txt")
    # crawler.getCidadeList(["Las Vegas"], "5_lv.csv")
    crawler.loadCidadeList("5_lv.csv")
    for cidade in crawler.cidades:
        crawler.getHostList(cidade, per_page=300)

    crawler.loadHostList("hosts.csv")
    crawler.getReviewsThreaded()
    crawler.initSQLITE("reviews.db")
    crawler.storeReviewsSqlite()

    # crawler = CSCrawler.CSCrawler("cookies.txt")
    
    # crawler.getCidadeList(["Sao Paulo", "Rio de Janeiro", "New York City", "Boston", "Las Vegas"], "cidades_3.csv")
    # crawler.getCidadeList(["Las Vegas"], "cidades_2.csv")
    # crawler.loadCidadeList("cidades_2.csv")

    # for cidade in crawler.cidades:
    #     crawler.getHostList(cidade, per_page=300)

    


if __name__ == '__main__':
    main()
