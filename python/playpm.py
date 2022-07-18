from basepm import pmlist
from basemove import learnlist
from basemove import movelist
import random
MAX_PM = 3


#save players pmby,   id of player, name, number of location, current 6 status, move1-4
pm1=[]
pm2=[]
pm3=[]
#save user as id, name, img?,number of pm player has,numberof pm live, pm1-6

user = [0,"player1","img",0,0, pm1,pm2,pm3]

examplenpc = [1,"npc1","img",0,0, pm1,pm2,pm3]
examplenpc2 = [2,"npc2","img",0,0, pm1,pm2,pm3]
total_player_list = [user,examplenpc,examplenpc2]

#auto to full a npc
def random_pm_for_npc(npc_id):
    empty_loc = 5
    if total_player_list[npc_id][3] == 0:
        for i in range(MAX_PM):
            currpm = []
            pm_id = random.randint(0,len(pmlist)-1)

            #get base info
            currpm.append(pmlist[pm_id])
            #get skill
            currpm.append(getmoveid(pm_id))
            #add to empty set
            total_player_list[npc_id][empty_loc]=currpm
            #move to next set
            empty_loc+=1

    total_player_list[npc_id][3] = MAX_PM
    total_player_list[npc_id][4]=MAX_PM
   # print(examplenpc)

def getmoveid(pm_id):
    pmmovelist = []
    copy_move = learnlist[pm_id]
    lrange = len(copy_move)
    #let some pm only has 1 skill
    if lrange > 4:
        epmove = 4
    else:
        epmove = lrange
    for i in range(epmove):
            #print(copy_move)
        #get location of the move in the pm move list
        num_copy_move = random.randint(0,lrange-1)
            #print(copy_move[num_copy_move])
        #get the id of move in move list
        move_num = copy_move[num_copy_move]-1
        #pm learned this move
        pmmovelist.append(movelist[move_num])
            #print("learn" + str(movelist[move_num]))
        #let this move to the end make sure not repetitive learning
        copy_move.append(copy_move[num_copy_move])
        copy_move.remove(copy_move[num_copy_move])
        lrange-=1
    return pmmovelist


#you can use for loop to call this one to full random npc
#random_pm_for_npc(1)