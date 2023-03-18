"""
Module returns total number of each resource, URL`s, and validate data
Also this module we can use as a CLI
"""
from flask import Blueprint
from task_three import (
    films_data,
    planets_data,
    species_data,
    starships_data,
    vehicles_data,
    characters_data,
)
from utils.randgen import ProduceNum
from utils.fetch_data import hit_url


taskthree = Blueprint("taskthree", __name__, url_prefix="/api")


@taskthree.route("/task_three/<resource>/")
def task_three(resource, start=1, end=8, limit=3):
    starship_data = []
    film_data = []
    vehicle_data = []
    specie_data = []
    character_data = []
    planet_data = []

    obj = ProduceNum(start, end, limit-1)
    resources = [element for element in obj]

    for item in resources:
        if resource == "starships":
            print(f"Generating the data for {resource} id :-> {item}")
            response_url = hit_url(starships_data()[item])
            data = response_url.json()
            starship_data.append(data)

        if resource == "films":
            print(f"Generating the data for {resource} id :-> {item}")
            response_url = hit_url(films_data()[item])
            data = response_url.json()
            film_data.append(data)

        if resource == "vehicles":
            print(f"Generating the data for {resource} id :-> {item}")
            response_url = hit_url(vehicles_data()[item])
            data = response_url.json()
            vehicle_data.append(data)

        if resource == "species":
            print(f"Generating the data for {resource} id :-> {item}")
            response_url = hit_url(species_data()[item])
            data = response_url.json()
            specie_data.append(data)

        if resource == "planets":
            print(f"Generating the data for {resource} id :-> {item}")
            response_url = hit_url(planets_data()[item])
            data = response_url.json()
            planet_data.append(data)
        else:
            print(f"Generating the data for {resource} id :-> {item}")
            response_url = hit_url(characters_data()[item])
            data = response_url.json()
            character_data.append(data)

    if resource == "films":
        return film_data
    elif resource == "characters":
        return character_data
    elif resource == "species":
        return specie_data
    elif resource == "starships":
        return starship_data
    elif resource == "vehicles":
        return vehicle_data
    elif resource == "planets":
        return planet_data
