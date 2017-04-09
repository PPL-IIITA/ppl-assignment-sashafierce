"""

model class for Girl

"""
class Girl:
    

    """

    constructor to initialize a girl with associated attributes

    """
    status = "single"
    def __init__(self, name, attractiveness, intelligence, maintenance, type):
        self.name = name
        self.attractiveness = attractiveness
        self.intelligence = intelligence
        self.maintenance = maintenance
        self.type = type
        self.happiness = 0

    """

    setter method  for attributes of girl

    """
    def __set__(self, instance, value):
        self.instance = value

    """

     getter method  for attributes of girl

    """
    def __get__(self, instance):
        return self.instance

