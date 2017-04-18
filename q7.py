"""
file containing source code for returning girlfriends of listed boys
"""
from random import randint
from csv import reader
from Model import Gift , Girl , Boy
from Utility import TestUtil , GetCouplesUtil , MatchMaker
import retriever , random , csv


file_girls = TestUtil.random_girls(random.randint(10, 50))
infile = open(file_girls,"rb")
girl_list = []
try:
    reader = csv.reader(infile)
    for row in reader:
        girl_list.append(Girl.Girl(row[0], row[1], row[2], row[3], row[4]))
finally:
    infile.close()
file_boys = TestUtil.random_boys(random.randint(50, 100))
infile = open(file_boys,"rb")
boy_list = []
try:
    reader = csv.reader(infile)
    for row in reader:
        boy_list.append(Boy.Boy(row[0], row[1], row[2], row[3], row[4], row[5]))
finally:
    infile.close()
couple_list = MatchMaker.make_couples(girl_list , boy_list)
type = input("choose an implementation for retrieval of girl : \n1. Array \n2.Sorted Array \n3.Hash map\n")
boy_list =[]
r = randint(1 , len(couple_list)-1)
i = 0
while i < r :
	i += 1
	boy_list.append(couple_list[i].boy)
if type == 1 :	
	obj = retriever.ArrayMethod()
	obj.find(boy_list , couple_list)

elif type == 2 :
	obj = retriever.SortedArrayMethod()
	obj.find(boy_list , couple_list)

elif type == 3 :
	obj = retriever.HashMethod()
	obj.find(boy_list , couple_list)
elif type == "\n" :
	obj = retriever.ArrayMethod()
	obj.find(boy_list , couple_list)




