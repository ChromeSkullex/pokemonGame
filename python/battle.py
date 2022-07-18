from calculate import *

#first there has player and npc
for i in range(2):
    random_pm_for_npc(i)
player = total_player_list[0]
npc = total_player_list[1]
npc_id = 1
player_id = 0

#print(player[:5]),print(player[5]),print(player[6]),print(player[7])
ppm1 = player[5]
#print(npc[:5]),print(npc[5]),print(npc[6]),print(npc[7])
npm1=npc[5]

battle = True
#set the first player pm and npc pm data, you can just load on database
pmchange = True
nmchange = True
print(player)
while(battle):
   # print(total_player_list[0])
    #print(total_player_list[1])
    umturn = True
    nmturn = True
    if pmchange == True:
        #plyaer currentpm
        pminfo = ppm1[0]
        #status types
        ppmhp = pminfo[2]
        ppmatk = pminfo[3]
        ppmedf = pminfo[4]
        ppsatk = pminfo[5]
        ppmsdef = pminfo[6]
        ppmspeed = pminfo[7]
        ppmtype1 = pminfo[8]
        ppmtype2 = pminfo[9]
        #moves
        pmove = ppm1[1]
        pmchange = False
    if nmchange == True:
        #npc currentpm
        npminfo = npm1[0]
        #npc status types
        npmhp = npminfo[2]
        npmatk = npminfo[3]
        npmedf = npminfo[4]
        npsatk = npminfo[5]
        npmsdef = npminfo[6]
        npmspeed = npminfo[7]
        npmtype1 = npminfo[8]
        npmtype2 = npminfo[9]
        #npc moves
        npmove = ppm1[1]
        nmchange = False

    action = input("1 as move, 2 as change")
#    print(ppm1)
  #  print(npm1)
    if action == "1":
        print("move")
        #because we use button, so just 1-4
        move_select = int(input("select your move"))
        print(move_select)
        umove_id = pmove[move_select-1][0]
        print("your move id  " + str(umove_id))
        nmove_id = npmove[random.randint(0,3)][0]
        print("his move id " + str(nmove_id))
        if ppmspeed >= npmspeed:
            print("you fst")
            umturn = False
            npmhp -= pm_atk(ppm1,npm1,umove_id)
            if npmhp <= 0:
                print("he change")
                nmturn = False
                nmphp = 0
        if nmturn == True:
            print("he fst")
            nmturn = False
            ppmhp -= pm_atk(npm1,ppm1,nmove_id)
            if ppmhp <= 0:
                print("you change")
                umturn = False
                ppmhp = 0
        if umturn == True:
            umturn = False
            npmhp -= pm_atk(ppm1,npm1,umove_id)
            if nmphp <= 0:
                print("he change")
                nmturn = False
                nmphp = 0
    elif action == "2":
        sl_num = int(input("select the next one"))
        switch_pm(player_id,ppm1,sl_num)
        pmchange = True
        nmove_id = npmove[random.randint(0,3)][0]
        ppmhp  -= pm_atk(npm1,ppm1,nmove_id)
        if ppmhp <= 0:
            ppmhp = 0

    if ppmhp == 0:
        total_player_list[player_id][4] -=1
        total_player_list[player_id][5][0][2] = 0
        sl_num = int(input("select the next one"))
        if total_player_list[player_id][4] > 0:
            pmchange = True
            switch_pm(player_id,ppm1,sl_num)
        else:
            battle = False
            print("lose")
    elif npmhp == 0:
        total_player_list[npc_id][4] -=1
        total_player_list[npc_id][5][0][2] = 0
        if total_player_list[npc_id][4] > 0:
            nmchange = True
            print(total_player_list[npc_id][4])
            switch_pm(npc_id,npm1,total_player_list[npc_id][4]+1)
        else:
            battle = False
            print("Win")
    nmturn = True
    umturn = True







