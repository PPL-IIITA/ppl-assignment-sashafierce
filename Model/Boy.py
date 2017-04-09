"""
model class for boy
"""
class Boy:
    

    
    """ 

    constructor to initialize a boy with associated attributes


    """
    status = "single"
    def __init__(self, name, attractiveness, intelligence, budget, minreq, type):
        self.name = name
        self.attractiveness = attractiveness
        self.intelligence = intelligence
        self.budget = budget
        self.type = type
        self.happiness = 0
        self.minreq = minreq

    """ 
    setter method  for attributes of boy
    """
    def __set__(self, instance, value):
       self.instance = value

    """ 
    getter method  for attributes of boy
    """
    def __get__(self, instance):
        return self.instance


