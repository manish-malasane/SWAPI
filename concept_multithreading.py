import requests
from time import time
from multiprocessing.pool import ThreadPool


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


def fetch_data(url):
    response = requests.get(url)
    data = response.json()
    return data.get("name")


@timeit
def multithreading():
    """
        Returns:
        NOTE:
            ThreadPool object can be created with whatever number of threads
            we would like.
            For example, `pool = ThreadPool(100)`
            `pool` object has `map` method which distributes the collection elements
            across available threads in pool.
            `pool.map()` function returns a list object
        """
    urls = get_urls()
    pool = ThreadPool(10)
    result = pool.map(fetch_data, urls)
    print(result)


if __name__ == "__main__":
    multithreading()
    breakpoint()
