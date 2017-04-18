"""
utility class for couple formation
"""
from Utility import LogUtil
from Model import Couple

"""
method for calculating compatibility of a girl and a boy based on the attributes :
intelligence , attractiveness and maintenance/ budget
"""
def calc_compatibility(girl  , boy):
    a = abs(int(girl.intelligence) - int(boy.intelligence) )
    b = abs(int(girl.attractiveness)- int(boy.attractiveness) )
    return a + b + abs(int(girl.maintenance) - int(boy.budget))

"""
method for couple formation from a list of girls and boys and logging the events
"""
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
    print("Total couples = " + str(couples) + " \n")
    return couple_list




