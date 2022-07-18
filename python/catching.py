from calculate import *

i = 0
super_list = [5,6]
user = [0,"player1","img",0,0, pm1,pm2,pm3]
user_id = 0
current = user[3]
while(i<10):
    i+=1
    currpm = []
    pm_id = random.randint(0,len(pmlist)-1)
    currpm.append(pmlist[pm_id])
    currpm.append(getmoveid(pm_id))
    if(current < 3):
        print(currpm[0][1] + " appeard!")
        select_pm = int(input("do you want it? 0/1"))
        if(select_pm == 0):
            if(currpm[0][0] not in super_list):
                print("gacha")
                total_player_list[user_id][4+current] = currpm
                current+=1
            else:
                suc_rate = random.randint(0,255)
                if(suc_rate > 250):
                    print("gacha")
                    total_player_list[user_id][4+current] = currpm
                    current+=1
                else:
                    print(currpm[0][1] + " ran away")

