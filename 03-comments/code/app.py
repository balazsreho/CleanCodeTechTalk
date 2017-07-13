#! /usr/bin/env/python
# coding=utf-8
import clp

__author__ = "Balazs Reho"
__copyright__ = "Copyright 2017, Balazs Reho"
__credits__ = ["Balazs Reho"]
__license__ = "MIT license"
__version__ = "0.1.0"
__maintainer__ = "Balazs Reho"
__email__ = "reho.balazs@gmail.com"

if __name__ == '__main__':
    clp.CommandLineProgram.for_terminal().name_bank("RapidLab").run()