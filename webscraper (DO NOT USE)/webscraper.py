from bs4 import BeautifulSoup, SoupStrainer
import httplib2
import json
import lxml


def get_poke_stats(link):
    pokemon_full_stats = {}
    html_link_poke = link
    status, response = http.request(html_link_poke)
    soup = BeautifulSoup(response, "lxml")
    poke_type_html = soup.find('table', 'vitals-table').find_all('a', 'type-icon')
    poke_name = soup.find('h1').text
    poke_title = link.split("/")[-1]
    #print(poke_name)
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
    #print(poke_img_link)

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
    #print(json_poke_dict)
    move_table = soup.find('div', 'grid-col span-lg-6').find('table', 'data-table').find_all('tr')
    allowed_moves = []
    for move in move_table:
        move_tag = move.find('a', 'ent-name')
        move_text = ""
        if move_tag:
            move_text = move_tag.text
        if move_text:
            allowed_moves.append(move_text.lower().replace(" ", "_"))
    #print(allowed_moves)
    stat_table = soup.find('div', 'grid-col span-md-12 span-lg-8').find('table', 'vitals-table').find_all('tr')
    stat_json = {}
    for stat in stat_table:
        if stat.find('th').text.lower().replace(" ", "_") != "total":
            stat_title = stat.find('th').text.lower().replace(" ", "_")
            stat_num = float(stat.find('td', 'cell-num').text)
            stat_json.update({stat_title: {"title": stat.find('th').text, "base_num": stat_num}})
    #print(stat_json)
    pokemon_full_stats.update({poke_title: {"title": poke_name, "img": poke_img_link, "allowed_moves": allowed_moves,
                                            "base_stat": stat_json}})
    return pokemon_full_stats


if __name__ == '__main__':
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
    json_object = json.dumps(poke_arr, indent=4)
    print(json_object)

"""
DO NOT DELETE
html_link = "https://pokemondb.net/pokedex/bulbasaur"
soup = BeautifulSoup(response, "lxml")

poke_type_html = soup.find('table', 'vitals-table').find_all('a', 'type-icon')
poke_type = []
for type_ in poke_type_html:
    poke_type.append(str(type_.contents[0]))

"""
