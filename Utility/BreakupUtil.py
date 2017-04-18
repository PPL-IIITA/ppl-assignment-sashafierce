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
	k = randint(1, len(couple_list) - 1)
	i = 0
	print "Randomly generated value for k = " + str(k) 
	print "Performing break-up of the following " + str(k) + " least happy couples \n"
	girl_list = []
	while i < k : 		
		i += 1		
    		print (couple_list[i].girl + " and " + couple_list[i].boy + "\n")
    		girl = Girl.Girl(couple_list[i].girl , randint(1, 10), couple_list[i].g_intelligence, couple_list[i].maintenance ,couple_list[i].girl_type )
    		girl_list.append(girl) 
    		    	
    		
	return girl_list

