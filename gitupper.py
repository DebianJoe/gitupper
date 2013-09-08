#!/usr/bin/env python
import sys
import os
import ConfigParser
from sys import argv

Config = ConfigParser.ConfigParser()
Config.read(os.path.expanduser('~/gitupper/repos'))
script, first = argv

#this will print a listing of all sections.

def listing():
    options = Config.items('repos')
    for option in options:
        i = 0
        print option[i]
        i += 1

def upping():
    ### Needs functional working ###
    options = Config.items('repos')
    for option in options:
        i = 0
        repo = Config.get('repos', option[i])
        print repo
        i += 1

def ConfigSectionMap(section):
    dict(Config.items('repos'))
if first == "-ls":
    listing()
elif first == "-up":
    upping()
