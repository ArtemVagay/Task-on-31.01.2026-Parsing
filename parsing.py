import requests
from bs4 import BeautifulSoup

st_accept = 'text/html'

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.1 Safari/605.1.15'

headers = {
    'Accept': st_accept,
    'User-Agent': user_agent
}
books = []
while True:
    ask = int(input("Библиотека - 1\nПоиск книги - 2\n"))
    if ask == 1:
        req = requests.get("https://books.toscrape.com", headers)
        src = req.text
        soup = BeautifulSoup(src, "html.parser")
        books = soup.find_all('article', attrs={"class": "product_pod"})
        for item in books:
            print(f"{item.find('h3').find('a')['title']}:")
            print("\t", item.find('p', attrs={"class": "price_color"}).text[1:])
            availability = item.find('p', attrs={"class": "availability"}).text.strip()
            if availability == 'In stock':
                print("\t", "В наличии")
            else:
                print("\t", "Нет в наличии")
            stars_count = item.find('p')["class"][1]
            stars = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
            print("\t", "рейтинг:", "* " * stars[stars_count])
            print()
    else:
        book_name = input("Введите название книги: ")
        if book_name:
            for book in books:
                if book.find('h3').find('a')['title'] == book_name:
                    link = book.find('a')['href']
                    req1 = requests.get(f"https://books.toscrape.com/{link}", headers)
                    src1 = req1.text
                    soup1 = BeautifulSoup(src1, "html.parser")
                    ps = soup1.find_all('p')
                    print("\tЦена:", ps[0].text[1:])
                    print("\tОписание:", ps[3].text, end="\n\n")
