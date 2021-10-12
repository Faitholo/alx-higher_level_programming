#!/usr/bin/python3
import json
"""
function that creates an Object from a "JSON file".
"""


def load_from_json_file(filename):
    '''module load_from_json_file
       returns corresponding Python object
    '''
    with open(filename, 'r') as f:
        return json.loads(f.read())
