"""
1. TODO - import all resource classes here -> Done
2. TODO - get count of each resource       -> Done
3. TODO - get singular resource URL from each resource
    - for example,
    - hit plural URL of starships and that will list all starships data
    - iterate on each starship data and capture singular URLs
    - all_starship_data = data.get("results")
    - you will iterate on `all_starship_data`,
4. TODO - pull data from random 3 "singular" resource URLs
    - utilize`utils` package to produce random 3 numbers from resource ids
    - and pull data for them
5. TODO - convert the script into CLI application
6. TODO - pretty print output (from pprint import pprint)
"""
import argparse
from pprint import pprint
from task_one import get_url
from utils.randgen import ProduceNum
from utils.fetch_data import hit_url

# resource classes
from resources.r_films import RFilms
from resources.r_planets import RPlanets
from resources.r_species import RSpecies
from resources.r_vehicles import RVehicles
from resources.r_characters import RCharacters
from resources.r_starships import RStarships

# pydantic models
from models.datamodels.characters import Characters
from models.datamodels.films import Films
from models.datamodels.planets import Planets
from models.datamodels.vehicles import Vehicles
from models.datamodels.species import Species
from models.datamodels.starships import Starships


def films_data():
    film_obj = RFilms()
    total_films = film_obj.get_count()
    print(total_films)
    film_data = film_obj.get_sample_data()
    film_data = Films(**film_data)
    print(film_data)
    film_urls = film_obj.get_resource_urls()
    print(film_urls)


def planets_data():
    planet_obj = RPlanets()
    total_planets = planet_obj.get_count()
    print(total_planets)
    planet_data = planet_obj.get_sample_data()
    planet_data = Planets(**planet_data)
    print(planet_data)
    planet_urls = planet_obj.get_resource_urls()
    print(planet_urls)


def species_data():
    specie_obj = RSpecies()
    total_species = specie_obj.get_count()
    print(total_species)
    specie_data = specie_obj.get_sample_data()
    specie_data = Species(**specie_data)
    print(specie_data)
    specie_urls = specie_obj.get_resource_urls()
    print(specie_urls)


def vehicles_data():
    vehicle_obj = RVehicles()
    total_vehicles = vehicle_obj.get_count()
    print(total_vehicles)
    vehicle_data = vehicle_obj.get_sample_data(4)
    vehicle_data = Vehicles(**vehicle_data)
    print(vehicle_data)
    vehicle_urls = vehicle_obj.get_resource_urls()
    print(vehicle_urls)


def characters_data():
    character_obj = RCharacters()
    total_characters = character_obj.get_count()
    print(total_characters)
    character_data = character_obj.get_sample_data()
    character_data = Characters(**character_data)
    print(character_data)
    character_urls = character_obj.get_resource_urls()
    print(character_urls)


def starships_data():
    starship_obj = RStarships()
    total_starships = starship_obj.get_count()
    print(total_starships)
    starship_data = starship_obj.get_sample_data(2)
    starship_data = Starships(**starship_data)
    print(starship_data)
    starship_urls = starship_obj.get_resource_urls()
    print(starship_urls)


def main():
    starships_data()
    characters_data()
    species_data()
    vehicles_data()
    planets_data()
    films_data()


def random_data():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--limit",
                        default=3, type=int)
    parser.add_argument("-s", "--start",
                        default=1, type=int)
    parser.add_argument("-e", "--end",
                        default=82, type=int)
    parser.add_argument("-r", "--resource",
                        default="people",
                        choices=["films",
                                 "planets",
                                 "people",
                                 "starships",
                                 "species",
                                 "vehicles"])
    argument = parser.parse_args()
    print(f"Passed arguments are -> {argument}")
    obj = ProduceNum(argument.start, argument.end, argument.limit)
    resources = [element for element in obj]
    content = []
    for item in resources:
        print(f"Generating the data for id :-> {item}")
        response_url = get_url(argument.resource, item)
        data = hit_url(response_url)
        data = data.json()
        content.append(data)
        pprint(content)


if __name__ == "__main__":
    main()
    random_data()
