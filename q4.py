"""
file containing source code for performing breakup of the least k happy couples and assigning new boyfriends to the corresponding girls.
"""
import csv
from random import randint
from csv import reader
from Model import Gift , Girl , Boy
from Utility import TestUtil , GetCouplesUtil , BreakupUtil , MatchMaker


no_of_gifts = randint(100, 1000)
file_gifts = TestUtil.random_gifts(no_of_gifts)
infile = open(file_gifts,"rb")
clist = []
try:
    reader = reader(infile)
    for row in reader:
        clist.append(Gift.Gift(row[0], row[1], row[2], row[3]))
finally:
    infile.close()    
clist.sort(key=lambda x: x.cost)

couple_list = GetCouplesUtil.getCouples(clist)

girl_list = BreakupUtil.breakup(couple_list)
infile = open("boys_test.csv", "rb")
boy_list = []
try:
	reader = csv.reader(infile)
    	for row in reader:
    		boy_list.append(Boy.Boy(row[0], row[1], row[2], row[3], row[4], row[5]))
finally:
  	infile.close()
couple_list = MatchMaker.make_couples(girl_list , boy_list)

print "New couples after breakup are :\n"

for girl in girl_list:
	
	i = randint(1, 30)
	print (girl.name + " and Boy" + str(i)+ "\n" )


