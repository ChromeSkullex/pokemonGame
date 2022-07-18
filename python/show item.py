from type import get_type


npc = [2, 'npc1', 'img', 3, 3,
       [[5, 'Azelf', 100, 100, 100, 100, 100, 100, 5, 1],
            [[8, 'move8', 3, 20], [2, 'move2', 2, 22], [9, 'move9', 2, 10], [4, 'move4', 4, 80]]],
       [[4, 'Aggron', 80, 150, 100, 50, 100, 20, 4, 1],
            [[6, 'move6', 1, 50], [10, 'move10', 4, 120], [2, 'move2', 2, 22], [9, 'move9', 2, 10]]],
       [[6, 'Articuno', 150, 120, 100, 130, 100, 100, 2, 4],
            [[4, 'move4', 4, 80], [8, 'move8', 3, 20], [3, 'move3', 5, 77], [1, 'move1', 3, 55]]]]



print("it is npc ID:" + str(npc[0]))
print("name:" + npc[1])
print("img:"+npc[2])
print("he has " + str(npc[3]) + " pokemons and " + str(npc[4]) + " live")
print("his first pokemon is " + npc[5][0][1] + " and learn")
print(npc[5][1])
print("the move " + str(npc[5][1][0][1]) +  " is type "  + get_type(npc[5][1][0][2]) + " and base dmg is " + str(npc[5][1][0][3]))

