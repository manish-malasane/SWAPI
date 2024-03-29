"""
This module specially dedicated for resource base classes where we have to implement all the functions defined under
this module
"""


class ResourceBase(object):
    """
    Base class representing required methods to be implemented by all resource classes
    """

    resources = ["people", "planets", "starships", "vehicles", "films", "species"]

    def __init__(self):
        self.home_url = "https://swapi.dev/"

    def get_count(self):
        raise NotImplementedError

    def get_resource_urls(self):
        raise NotImplementedError

    def get_sample_data(self):
        raise NotImplementedError
