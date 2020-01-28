#/usr/bin/python3
"""
Collection tests for Rectangle
"""


import unittest
import json
from models.rectangle import Rectangle
from models.base import Base


class RectangleTest(unittest.TestCase):
    """Test Rectangle methods """

    def setUp(self):
        self.obj1 = Rectangle(2, 4)
        self.obj2 = Rectangle(5, 10, 2)
        self.obj3 = Rectangle(3, 6, 2, 2)
        self.obj4 = Rectangle(10, 7, 1, 1, 7)

    def test_id(self):
        self.assertEqual(self.obj4.id, 7)

    def test_width(self):
        self.assertEqual(self.obj1.width, 2)
        self.assertEqual(self.obj2.width, 5)
        self.assertEqual(self.obj3.width, 3)
        self.assertEqual(self.obj4.width, 10)

    def test_height(self):
        self.assertEqual(self.obj1.height, 4)
        self.assertEqual(self.obj2.height, 10)
        self.assertEqual(self.obj3.height, 6)
        self.assertEqual(self.obj4.height, 7)

    def test_x(self):
        self.assertEqual(self.obj1.x, 0)
        self.assertEqual(self.obj2.x, 2)
        self.assertEqual(self.obj3.x, 2)
        self.assertEqual(self.obj4.x, 1)

    def test_y(self):
        self.assertEqual(self.obj1.y, 0)
        self.assertEqual(self.obj2.y, 0)
        self.assertEqual(self.obj3.y, 2)
        self.assertEqual(self.obj4.y, 1)

    def test_width_missing(self):
        with self.assertRaises(TypeError):
            obj10 = Rectangle()

    def test_width_TypeError(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            obj10 = Rectangle('five', 5)

    def test_width_ValueError(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            obj10 = Rectangle(-5, 5)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            obj10 = Rectangle(0, 2)

    def test_height_missing(self):
        with self.assertRaises(TypeError):
            obj10 = Rectangle(2, )

    def test_height_TypeError(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            obj10 = Rectangle(5, ['five'])

    def test_height_ValueError(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            obj10 = Rectangle(5, -5)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            obj10 = Rectangle(2, 0)

    def test_x_TypeError(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            obj10 = Rectangle(2, 3, "x")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            obj10 = Rectangle(1, 1, [[12]])

    def test_x_ValueError(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            obj10 = Rectangle(2, 3, -5)

    def test_y_TypeError(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            obj10 = Rectangle(2, 3, 1, (12, 1))
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            obj = Rectangle(2, 3, 1, [{'keykey': 'haha'}])

    def test_y_ValueError(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            obj10 = Rectangle(2, 3, 5, -10)

    def test_area(self):
        self.assertEqual(self.obj1.area(), 8)
        self.assertEqual(self.obj2.area(), 50)
        self.assertEqual(self.obj3.area(), 18)
        self.assertEqual(self.obj4.area(), 70)

    def test_area_unnecessary_arg(self):
        
        with self.assertRaises(TypeError):
            self.obj1.area(12)

    def display(self):
        """Display normal"""
        obj = Rectangle(1, 1, 1, 1, 1)
        var = StringIO()
        sys.stdout = var
        obj.display()
        self.assertEquals(var.getvalue(), '#\n')
        sys.stdout = sys.__stdout__

    def test_display_too_many_args(self):
        """Display with too many args"""
        with self.assertRaises(TypeError):
            self.obj1.display(1)

    def update_arg(self):
        """normal condition for updating"""
        self.assertEqual(str(obj4), '[Rectangle] (7) 1/1 - 10/7')
        obj4.update(12)
        self.assertEqual(str(obj4), '[Rectangle] (12) 1/1 - 10/7')
        obj4.update(12, 5)
        self.assertEqual(str(obj4), '[Rectangle] (12) 1/1 - 5/7')
        obj4.update(12, 5, 15)
        self.assertEqual(str(obj4), '[Rectangle] (12) 1/1 - 5/15')
        obj4.update(12, 5, 15, 3)
        self.assertEqual(str(obj4), '[Rectangle] (12) 3/1 - 5/7')
        obj4.update(12, 5, 15, 3, 9)
        self.assertEqual(str(obj4), '[Rectangle] (12) 3/9 - 5/7')

    def test_update_args_empty(self):
        """update empty parameter with arg update"""
        obj = Rectangle(4, 2, 1, 0, 6)
        obj.update()
        self.assertEqual(str(obj), '[Rectangle] (6) 1/0 - 4/2')

    def test_update_args_TypeError(self):
        """typeerror with arg update"""
        obj = Rectangle(4, 2, 1, 0, 6)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            obj.update(1, "bobobum")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            obj.update(2, 3, "mama")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            obj.update(2, 3, 1, [['34']])
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            obj.update(1, 1, 1, 1, {"potato": "pohtato"})

    def test_update_args_ValueError(self):
        """value error w/arg update"""
        obj = Rectangle(4, 2, 1, 0, 6)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            obj.update(1, 0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            obj.update(2, -7)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            obj.update(3, 4, 0)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            obj.update(5, 6, -7)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            obj.update(7, 8, 9, -7)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            obj.update(10, 1, 2, 3, -7)

    def test_kwargs(self):
        """test kwarg works in normal conditions"""
        r = Rectangle(4, 2, 1, 0, 8)
        r.update(width=30)
        self.assertEqual(str(r), '[Rectangle] (8) 1/0 - 30/2')
        r.update(height=20)
        self.assertEqual(str(r), '[Rectangle] (8) 1/0 - 30/20')
        r.update(y=15, x=5)
        self.assertEqual(str(r), '[Rectangle] (8) 5/15 - 30/20')
        r.update(id=9)
        self.assertEqual(str(r), '[Rectangle] (9) 5/15 - 30/20')

    def test_kwargs_new_key(self):
        """non-existant key w/kwarg in instance"""
        r10 = Rectangle(4, 2, 1, 0, 8)
        r10.update(jigglypuff=30)
        self.assertEqual(str(r10), '[Rectangle] (8) 1/0 - 4/2')
        self.assertEqual(r10.jigglypuff, 30)

    def test_update_kwargs_TypeError(self):
        """type error for kwargs update"""
        r = Rectangle(4, 2, 1, 0, 6)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(1, "bobobum")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(2, 3, "nahnahnah")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(2, 3, 1, [['34']])
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(1, 1, 1, 1, {"potato": "pohtato"})

    def test_update_kwargs_ValueError(self):
        """value error for kwargs update"""
        r = Rectangle(4, 2, 1, 0, 6)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(1, 0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(2, -7)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(3, 4, 0)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(5, 6, -7)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(7, 8, 9, -7)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(10, 1, 2, 3, -7)

    def to_dict(self):
        """check that to_dictionary work"""
        d1 = self.obj1.to_dictionary()
        self.assertEqual({"id": 1, "width": 2, "height": 4, "x": 0, "y": 0},
                         d1)
        d2 = self.r2.to_dictionary()
        self.assertEqual({"id": 2, "width": 5, "height": 10, "x": 2, "y": 0},
                         d2)
        d3 = self.r3.to_dictionary()
        self.assertEqual({"id": 3, "width": 3, "height": 6, "x": 2, "y": 2},
                         d3)
        d4 = self.r4.to_dictionary()
        self.assertEqual({"id": 7, "width": 10, "height": 7, "x": 1,
                          "y": 1}, d4)
        self.assertTrue(isinstance(d1, dict))

    def create_rect(self):
        """test normal use of create"""
        rr = {"id": 2, "width": 1, "height": 1, "x": 1, "y": 1}
        new_r = Rectangle.create(**rr)
        self.assertEqual(str(new_r), "[Rectangle] (2) 1/1 - 1/1")

    def to_dictionary_update(self):
        """check update for dict works"""
        r5 = (100, 120, 40, 10, 42)
        d5 = self.r5.to_dictionary()
        self.assertEqual({"id": 42, "width": 100, "height": 120, "x": 40,
                          "y": 10}, d5)
        r = Rectangle(11, 22, 33, 44, 55)
        r.update(**d5)
        self.assertEqual(r.__dict__, d5)

    def test_save_to_file(self):
        """save_to_file under normal conditions"""
        r11 = Rectangle(1, 2, 3, 4, 5)
        r12 = Rectangle(11, 22, 33, 44, 55)
        pobj = [r11, r12]
        Rectangle.save_to_file(pobj)
        with open("Rectangle.json", "r", encoding='utf-8') as f:
            ls = [r11.to_dictionary(), r12.to_dictionary()]
            self.assertEqual(json.dumps(ls), f.read())

    def test_save_to_file_empty(self):
        """save_to_file with empty list"""
        tehe = []
        Rectangle.save_to_file(tehe)
        with open("Rectangle.json", "r", encoding='utf-8') as f:
            self.assertEqual("[]", f.read())

    def test_load_from_file(self):
        """load_from_file under normal conditions"""
        r01 = Rectangle(1, 2, 3, 4, 5)
        r02 = Rectangle(11, 22, 33, 44, 55)
        pobj = [r01, r02]
        Rectangle.save_to_file(pobj)
        hiya = Rectangle.load_from_file()
        self.assertTrue(isinstance(hiya, list))
