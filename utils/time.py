"""
This module is a decorater it shows how much time taken to execute our logic
"""


from time import time


def timeit(func):
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()

        print(f"[ INFO ] Time to execute ::- {end - start}")

        return result
    return wrapper
