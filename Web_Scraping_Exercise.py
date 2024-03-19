import requests
import bs4

connect_url = requests.get("http://quotes.toscrape.com/")
soup = bs4.BeautifulSoup(connect_url.text,"lxml")
soup.select(".author")
authors = set()
for name in soup.select(".author"):
    authors.add(name.text)

print(authors)

quotes = []
for quote in soup.select(".text"):
    quotes.append(quote.text)
print(quotes)

for xtx in soup.select(".tag-item"):
    print(xtx.text)
##############################################

url = "http://quotes.toscrape.com/page/"
page_valid = True
author_set = set()
page = 1
while page_valid:
    page_url = url + str(page)
    res = requests.get(page_url)
    if "No quotes found!" in res.text:
        break
    else:
        soup = bs4.BeautifulSoup(res.text, "lxml")
        for name in soup.select(".author"):
            author_set.add(name.text)
    page += 1

print(f'{len(author_set)} Authos available as follows : {author_set}')