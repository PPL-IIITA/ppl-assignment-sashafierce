""" model class for Couple """
class Couple:

    """
     constructor to initialize a couple with associated attributes

     """
    def __init__(self, girl, boy, gtype , btype , budget,maintenance, gintelligence ,compatibility ):
        self.girl = girl
        self.boy = boy
        self.girl_type = gtype
        self.boy_type = btype
        self.budget = budget
        self.g_intelligence = gintelligence
        self.maintenance = maintenance
        self.happiness = 0
        self.compatibility = compatibility
