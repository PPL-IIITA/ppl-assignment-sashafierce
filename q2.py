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

couple_list = GiftUtil.gift_exchange(gift_list)

couple_list.sort(key=lambda x: x.happiness, reverse=True)
print "The k happiest couples are :\n"
for couple in couple_list:
    print (couple.girl + " and " + couple.boy + "\n")

couple_list.sort(key=lambda x: x.compatibility, reverse=True)

print "The k most compatible couples are :\n"
for couple in couple_list:
    print (couple.girl + " and " + couple.boy + "\n")

