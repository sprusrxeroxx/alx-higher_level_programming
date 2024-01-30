#!/usr/bin/python3
"Defines a rectangle class"


class Rectangle:
    """Represents a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes a new rectangle

        Args:
            width (int): The width of the new rectangle
            height (int): The height of the new rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Set the width of a rectangle"""

        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """Set the height of a rectangle"""

        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
