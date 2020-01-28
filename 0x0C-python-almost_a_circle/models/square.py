#!/usr/bin/python3

"""
This is a module for Square class.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """A square class."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize square class."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return string representation of class."""
        return("[{}] ({:d}) {:d}/{:d} - {:d}".
               format(type(self).__name__, self.id,
                      self.x, self.y, self.width))

    @property
    def size(self):
        """Get the size."""
        return self._Rectangle__width

    @size.setter
    def size(self, value):
        """Set the size."""
        self.integer_validator('width', value)
        self.integer_validator('height', value)
        self._Rectangle__width = value
        self._Rectangle__height = value

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute."""
        arg = len(args)

        if arg:
            for c, value in enumerate(args, 1):
                if c == 1:
                    self.id = value
                if c == 2:
                    self.size = value
                if c == 3:
                    self.x = value
                if c == 4:
                    self.y = value
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Returns the dictionary representation of square."""

        d_object = {}
        for a in ["id", "size", 'x', 'y']:
            d_object[a] = getattr(self, a)

        return d_object
