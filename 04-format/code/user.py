#! /usr/bin/env/python
# coding=utf-8

__author__ = "Balazs Reho"
__copyright__ = "Copyright 2017, Balazs Reho"
__credits__ = ["Balazs Reho"]
__license__ = "MIT license"
__version__ = "0.1.0"
__maintainer__ = "Balazs Reho"
__email__ = "reho.balazs@gmail.com"


class User:
    """
    User entity which tracks
    """

    def __init__(self, name):
        self.name = name
        self.transactions = []

    def add_transaction(self, new_transaction):
        self.transactions.append(new_transaction)

    def get_transactions(self):
        for item in self.transactions:
            # We use yield because it will be used in loops.
            yield item
