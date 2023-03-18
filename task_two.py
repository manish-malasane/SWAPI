"""
This module we can use as a CLI
This module returns the only names of resources as a list of str which works in film - 1.
In this module we are also returning the data of film - 1 in output.txt file
"""

import json
import argparse
from typing import Dict, List
from pprint import pprint
import requests
from utils.fetch_data import hit_url
from utils.time import timeit


URL = "https://swapi.dev/api/films/1/"


def first_task() -> Dict:
    """
    Fetches the data of URL which is mentioned above in module
    """
    response = requests.get(URL)
    result = response.json()
    return result


def write_data_in_file(data: Dict):
    """
    Writes a film - 1 data in output.txt file
    """
    with open("output.txt", "w") as foo:
        foo.write(json.dumps(data))


@timeit
def main_task(data: Dict) -> List:
    """
    Returns the only names of the passed resource from film - 1
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-r",
        "--resource",
        choices=["characters", "films", "planets", "starships", "vehicles"],
        default="characters",
        help="Pull out the data for passed resource",
    )
    argument = parser.parse_args()
    print(f"Passed arguments are : {argument}")
    response_data = data.get(argument.resource)
    resources = [element for element in response_data]

    names = []
    for resource in resources:
        resource_data = hit_url(resource)
        resource_data = resource_data.json()
        names.append(resource_data.get("name"))

    return names


if __name__ == "__main__":
    first = first_task()
    write_data_in_file(first)
    final_result = main_task(first)
    pprint(final_result)


# 'REFERENCE CODE'

# def second_task(data):
#     characters = data.get("characters")
#     names = []
#
#     for character in characters:
#         character_data = hit_url(character)
#         character_data = character_data.json()
#         names.append(character_data.get("name"))
#
#     return names
#
#
# def third_task(data):
#     planets = data.get("planets")
#     names = []
#
#     for planet in planets:
#         planet_data = hit_url(planet)
#         planet_data = planet_data.json()
#         names.append(planet_data.get("name"))
#
#     return names
#
#
# def fourth_task(data):
#     vehicles = data.get("vehicles")
#     names = []
#
#     for vehicle in vehicles:
#         vehicle_data = hit_url(vehicle)
#         vehicle_data = vehicle_data.json()
#         names.append(vehicle_data.get("name"))
#
#     return names
#
#
# @timeit
# def main():
#     first = first_task()
#     write_data_in_file(first)
#     second = second_task(first)
#     pprint(second)
#     third = third_task(first)
#     pprint(third)
#     fourth = fourth_task(first)
#     pprint(fourth)
