import csv
from DataFetcher import DataFetcher
from host import Host

def main():
	fetcher = DataFetcher("cookies.txt")
	data = fetcher.getItems("https://www.couchsurfing.com/members/hosts?utf8=%E2%9C%93&search_query=Curitiba%2C+Brazil&latitude=-25.4244287&longitude=-49.2653819&country=Brazil&region=south-america&date_modal_dismissed=true&arrival_date=&departure_date=&num_guests=1&has_references=1&can_host%5Baccepting_guests%5D=1&last_login=Anytime&join_date=Anytime&gender=All&min_age=&max_age=&languages_spoken=&interests=&smoking=No+Preference&radius=10&keyword=&host_sort=Best+Match&button=&perPage=100", "h3", className="-name")
	usuarios = [ Host(u.a.string, u.a['href'][len("/users/"):], u.a['href']) for u in data]

	arquivo = open("usuarios.csv", "w")
	arquivo_usuarios = csv.DictWriter(arquivo, fieldnames=["nome","id","endereco"], lineterminator='\n')
	arquivo_usuarios.writeheader()

	for user in usuarios:
		arquivo_usuarios.writerow({ 'nome' : user.nome, 'id' : user.id, 'endereco' : user.endereco.strip() })

	arquivo.close()

if __name__ == '__main__':
	main()