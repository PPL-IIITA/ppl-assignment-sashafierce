"""
utility class for gifting between a couple
"""
import math
import csv
from Utility import MatchMaker
from Model import Couple, Girl, Boy

"""
method for performing gifting between couple as per logic specified
arguments : gift_list consisting of randomly generated gifts of each kind 
"""
def gift_exchange(gift_list):
    infile = open("girls_test.csv", "rb")
    girl_list = []
    try:
        reader = csv.reader(infile)
        for row in reader:
            girl_list.append(Girl.Girl(row[0], row[1], row[2], row[3], row[4]))
    finally:
        infile.close()

    infile = open("boys_test.csv", "rb")
    boy_list = []
    try:
        reader = csv.reader(infile)
        for row in reader:
            boy_list.append(Boy.Boy(row[0], row[1], row[2], row[3], row[4], row[5]))
    finally:
        infile.close()
        couple_list = MatchMaker.make_couples(girl_list , boy_list)

    for couple in couple_list:
        tcost = 0
        luxval = 0
        tvalue = 0
        g = 0
        for gift in gift_list:
            if couple.boy_type == "genereous" or couple.boy_type== "geek":
                if int(gift.cost) + tcost <= int(couple.budget):
                    if gift.type == "luxury" :
                        luxval += int(gift.value)
                    else :
                        tvalue += int(gift.value)
                    tcost += int(gift.cost)
                    g += 1
                else :
                    break
            else :
                if couple.boy_type == "miser":
                    if int(gift.cost) + tcost <= int(couple.maintenance) :
                        tcost += int(gift.cost)
                        if gift.type == "luxury":
                            luxval += int(gift.value)
                        else:
                            tvalue += int(gift.value)
                        g += 1
                    else :
                        tcost += int(gift.cost)
                        if gift.type == "luxury":
                            luxval += int(gift.value)
                        else:
                            tvalue += int(gift.value)
                        break
        if g == 0 :
            couple.budget = gift_list[0].cost
            g += 1
            tcost += int(gift_list[0].cost)
            if gift.type == "luxury" :
                luxval += int(gift.value)
            else :
                tvalue += int(gift.value)
        if couple.girl_type == "choosy" :
            girl_happiness = 2*luxval + math.log10(tcost)
        else :
            if couple.girl_type == "normal":
                girl_happiness = tcost + tvalue
            else :
                try:
                    girl_happiness = math.exp(tcost)
                except OverflowError:
                    girl_happiness = int(1000)

        if couple.boy_type == "miser":
            boy_happiness = int(couple.budget) - tcost
        else :
            if couple.boy_type == "generous" :
                boy_happiness = girl_happiness
            else : boy_happiness = couple.g_intelligence
        couple.happiness = int(boy_happiness) + int(girl_happiness)
        print( couple.boy + " gave " + couple.girl + " " + str(g) + " gifts of total cost : " + str(tcost) + " and total value " + str(tvalue)+"\n")

    return couple_list

