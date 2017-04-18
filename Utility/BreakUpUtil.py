"""
utility class for performing break up of k least happy couples
"""
from random import randint
from Model import Couple, Girl

"""
method for performing breakup between couple as per logic specified
arguments : couple_list consiting of couples formed so far
"""
def breakup(couple_list):

	
	couple_list.sort(key=lambda x: x.happiness, reverse=False)
	print "Performing break-up of the following k least happy couples \n"
	girl_list = []
	for couple in couple_list:
    	print (couple.girl + " and " + couple.boy + "\n")
    	girl = Girl.Girl(couple.girl , randint(1, 10), couple.g_intelligence, couple.maintenance , couple.girl_type )
    	girl_list.append(girl)   

    return girl_list

