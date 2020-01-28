#!/usr/bin/python3
"""
Collection of tests for Base class.
"""


import unittest
import json
from models.base import Base


from models.rectangle import Rectangle
from models.square import Square


class BaseTest(unittest.TestCase):
    """Test Base methods."""

    def test_docstring(self):
        """ Test if it has docstring."""
        self.assertIsNotNone(Base.__doc__)

    def test_type(self):
        """Test type."""
        obj1 = Base()
        self.assertTrue(type(obj1) == Base)

    # ====================================================

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_id(self):
        """ Test id."""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(98)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 98)

    def test_a_passing_args(self):
        """ Test passing in args."""
        obj1 = Base(15)
        obj2 = Base(20)
        obj3 = Base(-5)
        obj4 = Base(9.1)
        self.assertEqual(obj1.id, 15)
        self.assertEqual(obj2.id, 20)
        self.assertEqual(obj3.id, -5)
        self.assertEqual(obj4.id, 9.1)

    def test_a_init(self):
        """test if init works with no args"""
        obj1 = Base()
        self.assertEqual(obj1.id, 1)
        obj2 = Base()
        self.assertEqual(obj2.id, 2)

    def test_string_input(self):
        """ Test if string input."""
        obj = Base("hello")
        self.assertEqual(obj.id, "hello")

    def test_none_input(self):
        """ Test if None input."""
        obj = Base(None)
        self.assertEqual(obj.id, 1)

    def test_tuple_input(self):
        """ Test if structures (python) input."""
        obj = Base((1,))
        obj2 = Base([1, 98, 3])
        obj3 = Base({"hello": "world"})
        self.assertEqual(obj.id, (1,))
        self.assertEqual(obj2.id, [1, 98, 3])
        self.assertEqual(obj3.id, {"hello": "world"})

    # ====================================================

    def test_unknown(self):
        """ Test object unknow."""
        with self.assertRaises(NameError):
            Base(obj)

    def test_id_two_args(self):
        """ Test if two inputs."""
        with self.assertRaises(TypeError):
            b3 = Base(98, 1337)

    def test_nb(self):
        """ Test if error attributtes."""
        b = Base(3)
        with self.assertRaises(AttributeError):
            str(b.nb_objects)
        with self.assertRaises(AttributeError):
            str(b.__nb_objects)

    # ====================================================


    def test_json_dictionary(self):
        """ Test if disctionary does return"""
        t1 = Rectangle(10, 7, 2, 8, 1)
        dic = t1.to_dictionary()
        new_json_dic = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        json_dic = Base.to_json_string([dic])
        self.assertEqual(dic, new_json_dic)
        self.assertEqual(type(dic), dict)
        self.assertEqual(type(json_dic), str)

    def test_json_dictionary_empty(self):
        """ Test if disctionary is empty"""
        dic = Base.to_json_string([])
        self.assertEqual(dic, "[]")

    def test_json_file_created(self):
        """ Test if file is created with Json string"""
        obj = Rectangle(10, 7, 2, 8, 1)
        Rectangle.save_to_file([obj])
        with open("Rectangle.json", "r") as f:
            self.assertEqual([obj.to_dictionary()], json.load(f))

    def test_json_file_empty(self):
        """ Test if file is created with empty"""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual([], json.load(f))

    def test_json_file_empty(self):
        """ Test if file is created with still empty"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual([], json.load(f))

    def test_from_json_string(self):
        """ Test if json string converts back."""
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(type(json_list_input), str)
        self.assertEqual(type(list_output), list)
        self.assertEqual(list_output, list_input)

    def test_create_rectangle(self):
        """ Test making rectangle."""
        obj = Rectangle(3, 5, 1)
        obj_dictionary = obj.to_dictionary()
        t2 = Rectangle.create(**obj_dictionary)
        self.assertNotEqual(obj, t2)

    def test_create_square(self):
        """ Test creating square."""
        obj = Square(3, 5, 1)
        obj_dictionary = obj.to_dictionary()
        t2 = Rectangle.create(**obj_dictionary)
        self.assertNotEqual(obj, t2)

    def test_load_from_file_rectangle(self):
        """ Test if file load rectangle. """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertNotEqual(list_rectangles_input, list_rectangles_output)

    def test_load_from_file_square(self):
        """ Test if file load square."""
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        self.assertNotEqual(list_squares_input, list_squares_output)


if __name__ == '__main__':
    unittest.main()
