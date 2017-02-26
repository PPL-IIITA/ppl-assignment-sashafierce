from Utility import LogUtil
from Model import Couple


def calc_compatibility(girl  , boy):
    a = abs(int(girl.intelligence) - int(boy.intelligence) )
    b = abs(int(girl.attractiveness)- int(boy.attractiveness) )
    return a + b + abs(int(girl.maintenance) - int(boy.budget))


def make_couples(girls, boys):
    couples = 0
    couple_list = []
    for girl in girls:
        for boy in boys:
            if boy.status == "single" and boy.budget >= girl.maintenance and boy.minreq <= girl.attractiveness:
                couples += 1
                boy.status = "committed"
                couple_list.append(Couple.Couple(girl.name , boy.name,girl.type , boy.type, boy.budget, girl.maintenance, girl.intelligence ,calc_compatibility(girl, boy)))
                LogUtil.log_events("couple formed", girl.name + " got committed with " + boy.name)
                break
    print(str(couples) + " couples formed successfully\n")
    return couple_list




