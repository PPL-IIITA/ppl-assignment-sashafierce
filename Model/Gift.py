"""

model class for Gift

"""
class Gift:
    

    """

    constructor to initialize a gift with associated attributes

    """
    def __init__(self, id, cost, value, type):
        self.id = id
        self.cost = cost
        self.value = value
        self.type = type

    """

    setter method  for attributes of gift

    """
    def __set__(self, instance, value):
        self.instance = value

    """

     getter method  for attributes of gift

    """
    def __get__(self, instance):
        return self.instance

