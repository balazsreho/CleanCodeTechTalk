#! /usr/bin/env/python
# coding=utf-8

# Custom imports
import clp

__author__ = "Balazs Reho"
__copyright__ = "Copyright 2017, Balazs Reho"
__credits__ = ["Balazs Reho"]
__license__ = "MIT license"
__version__ = "0.1.0"
__maintainer__ = "Balazs Reho"
__email__ = "reho.balazs@gmail.com"


if __name__ == '__main__':
    clp = clp.CommandLineProgram.for_terminal()
    clp.name_bank("RapidLab")
    clp.run()
