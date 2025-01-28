# Define the City class
class City:
    def __init__(self, name, pop):
        self.name = name  # Name of the city
        self.pop = pop  # Population of the city

# Define the Region class
class Region:
    def __init__(self, name):
        self.name = name  # Name of the region
        self.cities = []  # List to store cities in the region

    def add(self, city):
        # Add a city to the region
        self.cities.append(city)

    @property
    def pop(self):
                return sum(city.pop for city in self.cities) # Calculate the total population of the region

# Define the Country class
class Country:
    def __init__(self, name):
        self.name = name  # Add name of the country
        self.regions = []  # List to store regions in the country

    def add(self, region):
            self.regions.append(region)# Add a region to the country

    @property
    def pop(self):
                return sum(region.pop for region in self.regions) # Calculate the total population of the country

    @property
    def most_populuous_city(self):
        # Find the city with the largest population in the country
        all_cities = [city for region in self.regions for city in region.cities]
        return max(all_cities, key=lambda city: city.pop) if all_cities else None

