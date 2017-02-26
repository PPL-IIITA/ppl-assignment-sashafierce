class Girl:
    status = "single"

    def __init__(self, name, attractiveness, intelligence, maintenance, type):
        self.name = name
        self.attractiveness = attractiveness
        self.intelligence = intelligence
        self.maintenance = maintenance
        self.type = type
        self.happiness = 0

    def __set__(self, instance, value):
        self.instance = value

    def __get__(self, instance):
        return self.instance

