"""
This module generates the random numbers. We can specify the limit how many random number we want in between range
"""

import random


class ProduceNum:
    def __init__(self, start, end, limit):
        self.start = start
        self.end = end
        self.limit = limit

    def __iter__(self):
        counter_ = self.start
        while counter_ <= self.limit:
            yield random.randint(self.start, self.end)
            counter_ += 1
