from calculate import *


def get_t_id(user_id):
    pm_num = int(input("select traning pm 1,2,3"))
    if(pm_num > 0 and pm_num < 3):
        get_t_goal(user_id,pm_num)
    else:
        get_t_id(user_id)

def get_t_goal(user_id,pm_num):
    tranning_goal = int(input("select traning goal atk to speed 0-5"))
    if(tranning_goal > 0 and tranning_goal < 6):
        tranning_pm(pm_num,user_id,tranning_goal)
    else:
        get_t_goal(user_id,pm_num)

def tranning_pm(pm_num,user_id,tranning_goal):
    total_player_list[user_id][4+pm_num][0][3+tranning_goal] += 2000

random_pm_for_npc(0)

user = total_player_list[0]
print(user[:5])
print(user[5])
print(user[6])
print(user[7])
get_t_id(0)
user = total_player_list[0]
print(user[:5])
print(user[5])
print(user[6])
print(user[7])