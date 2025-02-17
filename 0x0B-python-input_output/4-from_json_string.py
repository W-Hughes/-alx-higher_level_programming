#!/usr/bin/python3
"""Returns an object (Python data structure0 represented by a JSON."""
import json


def from_json_string(my_str):
    """Returns an object (Python data structure)
    represented by a JSON string.
    """
    return json.loads(my_str)
