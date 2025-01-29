# Define the City class
class City:
    def __init__(self, name, pop):
        self.name = name  # Name of the city
        self.pop = pop  # Population of the city

#sicily.add(City("Catania", pop=300_000))
#sicily.add(City("Palermo", pop=600_000))
#calabria.add(City("Reggio Calabria", pop=170_000))

# Define the Country class
class Country:
    def __init__(self, name):
        self.name = name  # Add name of the country
        # italy = Country("Italy")
        self.regions = []  # List to store regions in the country

    def add(self, region):
            self.regions.append(region)# Add a region to the country
            # italy.add(sicily)
            # italy.add(calabria)

    @property
    def pop(self):
                return sum(region.pop for region in self.regions) # Calculate the total population of the country
                # assert italy.pop == 1_070_000

    @property
    def most_populuous_city(self):
        #script di veronica
        # max_pop = 0
            # most_populuous_city = None
            # for region in self.regions:
            # for city in region.cities:
                # if city.pop > max_pop
                    # most_populuous_city = city
                    #return most_populuous_city

        # Find the city with the largest population in the country
        all_cities = [city for region in self.regions for city in region.cities]
        #for all region(in self.region) looking for the each city(in region.cities)
        return max(all_cities, key=lambda city: city.pop) if all_cities else None
        #lambda funtion says to max() compare cities by population (city.pop)
        #If there are no cities in all_cities, returns None.

        #assert italy.most_populuous_city.name == "Palermo"

# Define the Region class
class Region:
    def __init__(self, name):
        self.name = name  # Name of the region
        # sicily = Region("Sicily")
        # calabria = Region("Calabria")
        self.cities = []  # List to store cities in the region

    def add(self, city):
        # Add a city to the region
        self.cities.append(city) #qui nei metodi è meglio non dare return
        # italy.add(sicily)

    @property
    def pop(self):
                return sum(city.pop for city in self.cities if city.pop is not None) # Calculate the total population of the region
                # assert sicily.pop == 900_000 %proprietà
