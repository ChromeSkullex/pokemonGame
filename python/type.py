
def get_type(type_id):
    if type_id == 1:
        return "fire"
    if type_id == 2:
        return "ice"
    if type_id ==  3:
        return "water"
    if type_id ==  4:
        return "ground"
    if type_id ==  5:
        return "fly"
typetable = [
    [1,1,1,1,1,1],
    [1,0.5,2,0.5,1,1],
    [1,0.5,0.5,1,1,2],
    [1,2,1,0.5,2,1],
    [1,2,1,1,2,0],
    [1,1,0.5,1,1,1]
]

def get_effect(type_atk,type1,type2):
    base_effect = typetable[type_atk][type1] * typetable[type_atk][type2]
    if base_effect >= 2:
        print("It's super effective!")
    elif base_effect ==1:
        print("normal effective.")
    elif base_effect == 0:
        print("no effective")
    else:
        print("Not Very Effective")
    return base_effect



