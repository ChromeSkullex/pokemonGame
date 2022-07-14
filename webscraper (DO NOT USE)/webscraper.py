from bs4 import BeautifulSoup, SoupStrainer
import httplib2
import json
import lxml

"""
Gets the pokemon stats from the website, this then parse the data into a json which is created in the web scraper
folder. 
link: link of the pokemon pages
Returns: Json of Pokemon information
"""


def get_poke_stats(link):
    pokemon_full_stats = {}  # Returns
    http = httplib2.Http()
    #  html BeautifulSoup things
    html_link_poke = link
    status, response = http.request(html_link_poke)
    soup = BeautifulSoup(response, "lxml")
    poke_type_html = soup.find('table', 'vitals-table').find_all('a', 'type-icon')

    # Web Scraper
    poke_name = soup.find('h1').text  # Gets Name
    poke_title = link.split("/")[-1]  # Gets Pokemon Link name (eg. Venusaur -> venusaur-f)
    # print(poke_name)
    poke_type = {}  # Stores the type of pokemon, some can have up to two
    poke_img_link = ""  # Stores the image link to be used later

    # For loop to append type
    for type_ in poke_type_html:
        poke_type.update({str(type_.contents[0].lower()):str(type_.contents[0])})

    # Getting image link
    poke_img_tag = soup.find('table', 'data-table sprites-table sprites-history-table').find_all('img',
                                                                                                 'img-fixed '
                                                                                                 'img-sprite-v11')
    if poke_img_tag:
        poke_img_link = poke_img_tag[0]['src']
    else:
        print("Issue with " + poke_name)
    # print(poke_img_link)

    # Getting Def type (Although this can be moved to just move set table DB)
    table_tag = soup.find_all('table', 'type-table type-table-pokedex')
    json_poke_dict = {}
    for i in range(2):
        type_def = table_tag[i].find_all('td')
        for type_ in type_def:
            type_name = type_['title'].split(" →")[0]
            type_sen = type_['title'].split(" = ")[1]
            type_num = type_.text
            type_float = 0
            if type_num == "":
                type_float = 1
            elif type_num == "½":
                type_float = 0.5
            elif type_num == "¼":
                type_float = 0.25
            elif type_num == '&frac18;' or type_num == '⅛':
                type_float = 0.125
            else:
                type_float = float(type_num)
            json_poke_dict.update({type_name.lower(): {"title": type_name, "effect": type_float, "sentence": type_sen}})
    # print(json_poke_dict)

    # Scrapes the allowed moves (SET TO ONLY BY LEVEL)
    move_table = soup.find('div', 'grid-col span-lg-6').find('table', 'data-table').find_all('tr')
    allowed_moves = {}
    for move in move_table:
        move_tag = move.find('a', 'ent-name')
        move_text = ""
        if move_tag:
            move_text = move_tag.text
        if move_text:
            allowed_moves.update({move_text.lower().replace(" ", "_"):move_text})
    # print(allowed_moves)

    # Scrapes the Base Stats (ONLY BASE STATS)
    stat_table = soup.find('div', 'grid-col span-md-12 span-lg-8').find('table', 'vitals-table').find_all('tr')
    stat_json = {}
    for stat in stat_table:
        if stat.find('th').text.lower().replace(" ", "_") != "total":
            stat_title = stat.find('th').text.lower().replace(" ", "_")
            stat_num = float(stat.find('td', 'cell-num').text)
            stat_json.update({stat_title: {"title": stat.find('th').text, "base_num": stat_num}})
    # print(stat_json)
    pokemon_full_stats.update({poke_title: {"title": poke_name, "img": poke_img_link, "type":poke_type, "efficiency": json_poke_dict,
                                            "allowed_moves": allowed_moves,
                                            "base_stat": stat_json}})
    return pokemon_full_stats


def create_pokemon_json():
    http = httplib2.Http()
    html_link_main = "https://pokemondb.net/pokedex/stats/gen1"
    status, response = http.request(html_link_main)
    soup = BeautifulSoup(response, "lxml")
    poke_link = []
    poke_arr = {}
    for link in soup.find_all('a', 'ent-name'):
        poke_link.append("https://pokemondb.net" + link['href'])

    for link in poke_link:
        poke_arr.update(get_poke_stats(link))

    with open('../RAWDATA/pokemon.json', 'w') as f:
        json.dump(poke_arr, f, indent=4)


def create_moveset_json():
    http = httplib2.Http()
    html_link_main = "https://pokemondb.net/move/generation/1"
    status, response = http.request(html_link_main)
    soup = BeautifulSoup(response, "lxml")
    moveset_json = {}
    move_list = soup.find('table', id='moves').find_all('tr')
    for move_set in move_list:
        move_set_json = {}
        """{
            "absorb":{
                "title":"Absorb",
                "type": "grass", 
                "move_stat":{
                    "power":20,
                    "acc":100,
                    "pp":25
                },
                "effect": "sentence"
            }
        
        }"""
        if move_set.find('td', 'cell-name'):
            move_name = move_set.find('td', 'cell-name').find('a').text
            move_type = move_set.find('td', 'cell-icon').find('a', 'type-icon').text
            move_cat = move_set.find('td', 'cell-icon text-center').find('img')['title']
            move_stats = move_set.find_all('td', 'cell-num')
            move_eff = move_set.find('td', 'cell-long-text').text

            move_power = 0
            move_acc = 0
            move_pp = 0
            for i in range(3):
                if move_stats[i].text == '—' and i == 0:
                    move_power = 0
                elif i == 0:
                    move_power = float(move_stats[i].text)
                if move_stats[i].text == '—' and i == 1:
                    move_acc = 0
                elif move_stats[i].text == '∞' and i == 1:
                    move_acc = float('inf')
                elif i == 1:
                    move_acc = float(move_stats[i].text)
                if move_stats[i].text == '—' and i == 2:
                    move_pp = 0
                elif i == 2:
                    move_pp = float(move_stats[i].text)
            move_stat_json = {'power': move_power, 'acc': move_acc, 'pp': move_pp}
            moveset_json.update({move_name.lower().replace(" ", "_"): {'title': move_name, 'type': move_type.lower(),
                                                                        'cat': move_cat.lower(), 'stats': move_stat_json
                                                                    , 'effect': move_eff}})
    with open('../RAWDATA/moveset.json', 'w') as f:
        json.dump(moveset_json, f, indent=4)

if __name__ == '__main__':
    create_pokemon_json()


"""
DO NOT DELETE
html_link = "https://pokemondb.net/pokedex/bulbasaur"
soup = BeautifulSoup(response, "lxml")

poke_type_html = soup.find('table', 'vitals-table').find_all('a', 'type-icon')
poke_type = []
for type_ in poke_type_html:
    poke_type.append(str(type_.contents[0]))

"""
