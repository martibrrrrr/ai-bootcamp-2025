

class Country:
    def __init__(self, name):
        self.name=name
        self.regions= []
    def add(self,region): #method. A function defined in a class
        if isinstance(region,Region):
            self.regions.append(region)
        else:
            raise ValueError

    @property #to evaluate something
    def pop(self):
        """The total population of this country"""
        for region in self.region:
            region.pop += 1
    """ def most_populous_city(self):
        for region in self.regions:
            for city in region.cities:
                cities = city
"""


class Region:
    def __init__(self,name):
        self.name = name
        self.cities = []
    def add(self,city):
        if isinstance(city,City):
            self.cities.append(city)
        else:
            raise ValueError

    @property
    def pop(self):
        for city in self.cities:
            city.pop += 1
class City:
    """A city"""

    def __init__(self, name, pop=None):
        self.name=name
        self.pop = 0
