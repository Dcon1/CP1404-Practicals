class Guitar:

    def __init__(self, name="", year="", cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "Guitar : {:>20} ({}), worth ${:10,.2f}".format( self.name, self.year, self.cost)

    def get_age(self):
        return 2017 - self.year

    def is_vintage(self, age):
        if age > 50:
            return True