from bs4 import BeautifulSoup, SoupStrainer
import httplib2
import lxml


def get_poke_img(poke_name):
    html_link_poke = "https://pokemondb.net/pokedex/" + poke_name
    status, response = http.request(html_link_poke)
    soup = BeautifulSoup(response, "lxml")
    img_find = "https://img.pokemondb.net/sprites/x-y/normal/" + poke_name + ".png"
    poke_img_tag = soup.find('table', 'data-table sprites-table sprites-history-table').find_all('img',
                                                                                                  'img-fixed img-sprite-v11')
    if poke_img_tag:
        poke_img = poke_img_tag[0]['src']
        print(poke_img)
    else:
        print("Issue with "+ poke_name)


def get_poke_stats(link):
    html_link_poke = link
    status, response = http.request(html_link_poke)
    soup = BeautifulSoup(response, "lxml")
    poke_type_html = soup.find('table', 'vitals-table').find_all('a', 'type-icon')
    poke_name = soup.find('h1').text
    poke_type = []
    poke_img_link = ""
    for type_ in poke_type_html:
        poke_type.append(str(type_.contents[0]))

    poke_img_tag = soup.find('table', 'data-table sprites-table sprites-history-table').find_all('img',
                                                                                                 'img-fixed '
                                                                                                 'img-sprite-v11')
    if poke_img_tag:
        poke_img_link = poke_img_tag[0]['src']
    else:
        print("Issue with " + poke_name)
    print(poke_img_link)

if __name__ == '__main__':
    http = httplib2.Http()
    html_link_main = "https://pokemondb.net/pokedex/stats/gen1"
    status, response = http.request(html_link_main)
    soup = BeautifulSoup(response, "lxml")
    poke_link = []
    for link in soup.find_all('a', 'ent-name'):
        poke_link.append("https://pokemondb.net" + link['href'])

    for link in poke_link:
        get_poke_stats(link)

"""
DO NOT DELETE
html_link = "https://pokemondb.net/pokedex/bulbasaur"
soup = BeautifulSoup(response, "lxml")

poke_type_html = soup.find('table', 'vitals-table').find_all('a', 'type-icon')
poke_type = []
for type_ in poke_type_html:
    poke_type.append(str(type_.contents[0]))

"""
