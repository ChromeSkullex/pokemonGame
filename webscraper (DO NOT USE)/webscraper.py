from bs4 import BeautifulSoup, SoupStrainer
import httplib2
import lxml
http = httplib2.Http()

html_link = "https://pokemondb.net/pokedex/bulbasaur"
status, response = http.request(html_link)

#print(response)

soup = BeautifulSoup(response, "lxml")

poke_type_html = soup.find('table', 'vitals-table').find_all('a', 'type-icon')
poke_type = []
for type_ in poke_type_html:
    poke_type.append(str(type_.contents[0]))

