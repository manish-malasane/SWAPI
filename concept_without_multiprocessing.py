from time import time


def timeit(func):
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()

        print(f"[ INFO ] Time taken to execute :-> \t {end - start}")
        return result
    return wrapper


def get_urls(range_):
    return [i**3 for i in range(range_)]


@timeit
def main():
    ranges = [1000001, 1000002, 10000003, 10000004, 10000005]
    for i in ranges:
        get_urls(i)


if __name__ == "__main__":
    main()
    breakpoint()
