#!/usr/bin/python3
# 0-square.py by Amine Abbes
"""A module define a square """


class Square:
    """A class represents a square"""

    def __init__(self, size=0):
        """Initialize the square class
        Args:
            size: the size of the square defined
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size
