import requests
from time import time


def timeit(func):
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()

        print(f"[ INFO ] Time taken to execute :-> \t {end - start}")
        return result
    return wrapper


def get_urls():
    urls = []
    for i in range(1, 11):
        magic_url = f"https://swapi.dev/api/people/{i}"
        urls.append(magic_url)
    return urls


@timeit
def main():
    names = []
    urls = get_urls()
    for url in urls:
        response = requests.get(url)
        data = response.json()
        name = data.get("name")
        names.append(name)
    return names


if __name__ == "__main__":
    main()
