from basemove import *
from basepm import *
from playpm import *
from type import *



def pm_atk(atker, defer,move_id):
    #the move user selected
    sl_move = movelist[move_id]
    if sl_move[4] == 0:
        dmg = sl_move[3] + atker[0][3] - defer[0][4]
    else:
        dmg = sl_move[3] + atker[0][5] - defer[0][6]
    return dmg * get_effect(sl_move[2],defer[0][8],defer[0][9])



def get_pm(user_pm_id,user_id):
    user = get_user(user_id)
    return user[4+user_pm_id]

def get_user(user_id):
    for i in range(len(total_player_list)):
        if total_player_list[i][0] == user_id:
            return total_player_list[i]

def switch_pm(user_id,pm1,pm2_set_num):
    print("change pokemon")
    user = get_user(user_id)
    pm2 = user[pm2_set_num+4]
    if pm2[0][2] == 0 or pm2_set_num == 1:
        pm2_set_num = int(input("select the currect one"))
        switch_pm(user_id,pm1,pm2_set_num)
    else:
        user[pm2_set_num+4] = pm1
        user[5] = pm2
        total_player_list[user_id] = user
        print(total_player_list[user_id])