#!/usr/bin/python3
"""Contains the MyList class."""


class MyList(list):
    """Class MYList that inherits from list."""

    def print_sorted(self):
        """Prints the list in ascending sorted order."""
        print(sorted(self))
