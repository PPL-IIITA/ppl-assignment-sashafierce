"""
file containing source code for performing gifting t times a month and breakup of the least k happy couples .
"""
from random import randint
from csv import reader
from Model import Gift , Girl
from Utility import TestUtil , GiftUtil


no_of_gifts = randint(100, 1000)
file_gifts = TestUtil.random_gifts(no_of_gifts)
infile = open(file_gifts,"rb")
gift_list = []
try:
    reader = reader(infile)
    for row in reader:
        gift_list.append(Gift.Gift(row[0], row[1], row[2], row[3]))
finally:
    infile.close()
gift_list.sort(key=lambda x: x.cost)

t = randint(1, 30)
i = 0
print "Randomly generated value for t = " + str(t) +"\n"
while i < t :
	i+=1
	couple_list = GiftUtil.gift_exchange(gift_list)
	print "t = " + str(i) + "\n" + "Performing scheduled breakup of k least happy couple" 
	



