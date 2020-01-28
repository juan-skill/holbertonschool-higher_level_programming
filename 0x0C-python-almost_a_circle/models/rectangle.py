#!/usr/bin/python3
"""
Define a Rectangle class.
"""
from models.base import Base


class Rectangle(Base):
    """Define a Rectangle class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a Rectangle instance."""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def integer_validator(self, name, value):
        """Validate value."""
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0 and (name == 'width' or name == 'height'):
            raise ValueError('{} must be > 0'.format(name))
        if value < 0 and (name == 'x' or name == 'y'):
            raise ValueError('{} must be >= 0'.format(name))

    @property
    def width(self):
        """Get the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width."""
        self.integer_validator('width', value)
        self.__width = value

    @property
    def height(self):
        """Get the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height."""
        self.integer_validator('height', value)
        self.__height = value

    @property
    def x(self):
        """Get x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set x."""
        self.integer_validator('x', value)
        self.__x = value

    @property
    def y(self):
        """Get y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set y."""
        self.integer_validator('y', value)
        self.__y = value

    def area(self):
        """area of rect"""
        return self.width * self.height

    def display(self):
        """ Display of rect."""
        print('\n' * self.y, end='')
        for i in range(self.height):
            print('{}{}'.format(self.x * ' ', '#' * self.width))

    def __str__(self):
        """ Overriding the __str__ method so that it returns"""
        return ("[{}] ({:d}) {:d}/{:d} - {:d}/{:d}".
                format(type(self).__name__, self.id, self.x,
                       self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """ Assigns an argument to each attribute."""
        arg = len(args)

        if arg:
            for c, value in enumerate(args, 1):
                if c == 1:
                    self.id = value
                if c == 2:
                    self.width = value
                if c == 3:
                    self.height = value
                if c == 4:
                    self.x = value
                if c == 5:
                    self.y = value
        else:
            for key, item in kwargs.items():
                setattr(self, key, item)

    def to_dictionary(self):
        """ Returns the dictionary representation of rectangle."""

        d_object = {}
        for a in ["id", "width", "height", 'x', 'y']:
            d_object[a] = getattr(self, a)

        return d_object
