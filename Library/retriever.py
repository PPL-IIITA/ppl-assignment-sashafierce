"""
library classes for girlfriend name retriever
"""
from Utility import LogUtil
from random import randint
from Model import Couple

"""

"""
class Retriever:

	
	def getList( couple_list) :
		boy_list =[]
		r = randint(1 , len(couple_list)-1)
		i = 0
		while i < r :
			i += 1
			boy_list.append(couple_list[i].boy)
		return boy_list
	
	

class ArrayMethod(Retriever):
	
	
	def find(boy_list , couple_list) :
		l = len(couple_list)
		found = False
		i = 0
		for boy in boy_list :
			while found == False and i < len :
				if couple_list[i].boy == boy :
					found = True
					print boy + " has a girlfriend , " + couple_list[i].girl					
				i += 1
			if found == False :
				print boy + " is single " 
			found = False
	

class SortedArrayMethod(Retriever):


	def find(boy_list , couple_list) :
	
		couple_list.sort(key=lambda x: x.boy, reverse=False)
	
		l = len(couple_list)
		found = False
		i = 0
		for boy in boy_list :
			while found == False and i < len :
				if couple_list[i].boy == boy :
					found = True
					print boy + " has a girlfriend , " + couple_list[i].girl					
				i += 1
			if found == False :
				print boy + " is single " 
			found = False

class HashMethod(Retriever):

	def find(boy_list , couple_list) :
		l = len(couple_list)
		found = False
		i = 0
		for boy in boy_list :
			while found == False and i < len :
				if couple_list[i].boy == boy :
					found = True
					print boy + " has a girlfriend , " + couple_list[i].girl					
				i += 1
			if found == False :
				print boy + " is single " 
			found = False


	


