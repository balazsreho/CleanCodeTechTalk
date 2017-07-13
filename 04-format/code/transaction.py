#! /usr/bin/env/python
# coding=utf-8

# OS packages
import uuid
import datetime

__author__ = "Balazs Reho"
__copyright__ = "Copyright 2017, Balazs Reho"
__credits__ = ["Balazs Reho"]
__license__ = "MIT license"
__version__ = "0.1.0"
__maintainer__ = "Balazs Reho"
__email__ = "reho.balazs@gmail.com"


class Transaction:
    """
    Hold information about a user made transaction.
    """

    def __init__(self, amount):
        """
        Create a transaction with the current timestamp, and an unique ID.
        :param amount: Amount of money in transaction.
        """
        self.amount = amount
        current_date = datetime.datetime.now()
        self.timestamp = current_date.timestamp()
        self.uuid = uuid.uuid4()
