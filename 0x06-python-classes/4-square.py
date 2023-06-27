#!/usr/bin/python3
# 0-square.py by Amine Abbes
"""A module that defines square """


class Square:
    """A class represents a square"""

    def __init__(self, size=0):
        """Initialize square class
        Args:
            size:the size of the square defined
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    @property
    def size(self):
        """size of square"""

        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        area of the square
        Returns: The square of the size
        """

        return (self.__size ** 2)
