"""
Module returns total number of each resource, URL`s, and validate data
Also this module we can use as a CLI
"""

import argparse
from pprint import pprint
from utils.randgen import ProduceNum
from utils.fetch_data import hit_url
from utils.time import timeit

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

film_urls = []
planet_urls = []
specie_urls = []
vehicle_urls = []
starship_urls = []
character_urls = []


def films_data() -> None:
    """

    Total number of films: (int),
            URL`s: (List[str]),
            Validate Data: (dict)

    """
    film_obj = RFilms()
    total_films = film_obj.get_count()
    print(f"Total number of films :\n {total_films}")

    film_data = film_obj.get_sample_data()
    film_data = Films(**film_data)
    pprint(f" Film data :- \n {film_data}")

    global film_urls
    film_urls = film_obj.get_resource_urls()
    pprint(f"Film URL`s :-> \n {film_urls}")


def planets_data() -> None:
    """

    Total number of planets: (int),
                URL`s: (List[str]),
                Validate Data: (dict)

    """
    planet_obj = RPlanets()
    total_planets = planet_obj.get_count()
    print(f"Total number of planets :\n {total_planets}")

    planet_data = planet_obj.get_sample_data()
    planet_data = Planets(**planet_data)
    pprint(f" Planet data :- \n {planet_data}")

    global planet_urls
    planet_urls = planet_obj.get_resource_urls()
    pprint(f"Planet URL`s :-> \n {planet_urls}")


def species_data() -> None:
    """

    Total number of species: (int),
                URL`s: (List[str]),
                Validate Data: (dict)

    """
    specie_obj = RSpecies()
    total_species = specie_obj.get_count()
    print(f"Total number of species :\n {total_species}")

    specie_data = specie_obj.get_sample_data()
    specie_data = Species(**specie_data)
    pprint(f" Specie data :- \n {specie_data}")

    global specie_urls
    specie_urls = specie_obj.get_resource_urls()
    pprint(f"Species URL`s :-> \n {specie_urls}")


def vehicles_data() -> None:
    """

    Total number of vehicles: (int),
                URL`s: (List[str]),
                Validate Data: (dict)

    """
    vehicle_obj = RVehicles()
    total_vehicles = vehicle_obj.get_count()
    print(f"Total number of vehicles :\n {total_vehicles}")

    vehicle_data = vehicle_obj.get_sample_data(4)
    vehicle_data = Vehicles(**vehicle_data)
    pprint(f" Vehicle data :- \n {vehicle_data}")

    global vehicle_urls
    vehicle_urls = vehicle_obj.get_resource_urls()
    pprint(f"Vehicle URL`s :-> \n {vehicle_urls}")


def characters_data() -> None:
    """

    Total number of characters: (int),
                URL`s: (List[str]),
                Validate Data: (dict)

    """
    character_obj = RCharacters()
    total_characters = character_obj.get_count()
    print(f"Total number of characters :\n {total_characters}")

    character_data = character_obj.get_sample_data()
    character_data = Characters(**character_data)
    pprint(f" Character data :- \n {character_data}")

    global character_urls
    character_urls = character_obj.get_resource_urls()
    pprint(f"Character URL`s :-> \n {character_urls}")


def starships_data() -> None:
    """

    Total number of starships: (int),
                URL`s: (List[str]),
                Validate Data: (dict)

    """
    starship_obj = RStarships()
    total_starships = starship_obj.get_count()
    print(f"Total number of starships :\n {total_starships}")

    starship_data = starship_obj.get_sample_data(2)
    starship_data = Starships(**starship_data)
    pprint(f" Starship data :- \n {starship_data}")

    global starship_urls
    starship_urls = starship_obj.get_resource_urls()
    pprint(f"Starship URL`s :-> \n {starship_urls}")


@timeit
def main():
    """
    Get all the data associated with resources
    Data like :-> number of films,
                  URL`s of resources,
                  validate data
    """
    starships_data()
    characters_data()
    species_data()
    vehicles_data()
    planets_data()
    films_data()


@timeit
def random_data():
    """
    Generating the data for any three singular
    resource URL`s of passed resource.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--limit", default=3, type=int)
    parser.add_argument("-s", "--start", default=1, type=int)
    parser.add_argument("-e", "--end", default=10, type=int)
    parser.add_argument(
        "-r",
        "--resource",
        default="people",
        choices=["films", "planets", "people", "starships", "species", "vehicles"],
    )
    argument = parser.parse_args()
    print(f"Passed arguments are -> {argument}")
    obj = ProduceNum(argument.start, argument.end, argument.limit)
    resources = [element for element in obj]

    for item in resources:
        if argument.resource == "starships":
            print(f"Generating the data for {argument.resource} id :-> {item}")
            response_url = hit_url(starship_urls[item])
            data = response_url.json()
            pprint(data)

        if argument.resource == "films":
            print(f"Generating the data for {argument.resource} id :-> {item}")
            response_url = hit_url(film_urls[item])
            data = response_url.json()
            pprint(data)

        if argument.resource == "vehicles":
            print(f"Generating the data for {argument.resource} id :-> {item}")
            response_url = hit_url(vehicle_urls[item])
            data = response_url.json()
            pprint(data)

        if argument.resource == "species":
            print(f"Generating the data for {argument.resource} id :-> {item}")
            response_url = hit_url(specie_urls[item])
            data = response_url.json()
            pprint(data)

        if argument.resource == "planets":
            print(f"Generating the data for {argument.resource} id :-> {item}")
            response_url = hit_url(planet_urls[item])
            data = response_url.json()
            pprint(data)

        else:
            print(f"Generating the data for {argument.resource} id :-> {item}")
            response_url = hit_url(character_urls[item])
            data = response_url.json()
            pprint(data)


if __name__ == "__main__":
    main()
    random_data()
