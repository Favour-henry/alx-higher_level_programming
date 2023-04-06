#!/usr/bin/python3
"""
Write a class Rectangle that defines a rectangle
"""


class Rectangle:
    """
    Class Rectangle validated privated instance attribute width and height
    """
    def __init__(self, width=0, height=0):
        """Constructor Function using property and setter"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Method recover the value Width Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Method Evaluate the value of width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Method recover the value Height Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Method Evaluate the value of heigth"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the calculated area of Rectangle instance"""
        return self.width * self.height

    def perimeter(self):
        """Returns the calculated perimeter of Rectangle instance"""
        if self.height == 0 or self.width == 0:
            return 0
        else:
            return (self.width + self.height) * 2
