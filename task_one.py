import argparse

import requests

from utils.time import timeit
from utils.randgen import ProduceNum


def get_url(resource: str, resource_id: int) -> str:
    f"""

    Args:
        resource: "https://swapi.dev/api/people/1/"(like this)
        resource_id: integer

    Returns: url of star_warsAPI
            "https://swapi.dev/api/{resource}/{resource_id}/"

    """
    home_url = "https://swapi.dev"
    relative_url = "/api/{}/{}/"
    absolute_url = home_url + relative_url.format(resource, resource_id)
    return absolute_url


@timeit
def main() -> list:
    parser = argparse.ArgumentParser(
        prog="Fetching data from star_warsAPI",
        usage="To pull out the names of resources as a list",
        description="Display the data from star_warsAPI"
    )

    parser.add_argument("-c", "--count",
                        default=15,
                        type=int,
                        help="Generates the data for this number of resources from star_warsAPI"
                        )
    parser.add_argument("-s", "--start",
                        default=1,
                        type=int,
                        help="Generates the resource data from this resource_id"
                        )

    parser.add_argument("-e", "--end",
                        default=83,
                        type=int,
                        help="Generates the resource data up to this resource_id"
                        )

    parser.add_argument("-r", "--resource",
                        default="people",
                        type=str,
                        choices=["people",
                                 "films",
                                 "starships",
                                 "vehicles",
                                 "species",
                                 "planets",
                                 "root"]
                        )

    argument = parser.parse_args()
    print(f"Passed arguments are : {argument}")

    obj = ProduceNum(argument.start, argument.end, argument.count)

    resources_ids = [element for element in obj]
    print(f"[ INFO ] fetching data for following ids :{resources_ids}")

    content = []
    for resource_id in resources_ids:
        print(f"[ INFO ] fetching data for resource id number : {resource_id}")

        url = get_url(argument.resource, resource_id)

        response = requests.get(url)
        if response.status_code == 200:

            result = response.json()
            content.append(result.get("name"))

    return content


if __name__ == "__main__":
    print(main())
