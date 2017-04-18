"""
file containing source code for performing making couples using the zig-zag logic!
"""
import csv
import random
from random import randint
from csv import reader
from Model import Gift , Girl , Boy
from Utility import TestUtil , GetCouplesUtil , BreakupUtil , MatchMaker


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

print "New couples formed using zig-zag method are :\n"
for couple in couple_list:
    print (couple.girl + " and " + couple.boy + "\n")


