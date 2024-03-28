#!/usr/bin/python3
""" """
import unittest
import os
from models.amenity import Amenity
from models.base_model import BaseModel
import pep8


class TestAmenity(unittest.TestCase):
    """ """

    @classmethod
    def setUpClass(cls):
        """ """
        cls.amenity = Amenity()
        cls.amenity.name = "Breakfast"

    @classmethod
    def teardown(cls):
        """ """
        del cls.amenity

    def tearDown(self):
        """"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_Amenity(self):
        """ """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/amenity.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_checking_for_docstring_Amenity(self):
        """ """
        self.assertIsNotNone(Amenity.__doc__)

    def test_attributes_Amenity(self):
        """ """
        self.assertTrue('id' in self.amenity.__dict__)
        self.assertTrue('created_at' in self.amenity.__dict__)
        self.assertTrue('updated_at' in self.amenity.__dict__)
        self.assertTrue('name' in self.amenity.__dict__)

    def test_is_subclass_Amenity(self):
        """ """
        self.assertTrue(issubclass(self.amenity.__class__, BaseModel), True)

    def test_attribute_types_Amenity(self):
        """ """
        self.assertEqual(type(self.amenity.name), str)

    def test_save_Amenity(self):
        """ """
        self.amenity.save()
        self.assertNotEqual(self.amenity.created_at, self.amenity.updated_at)

    def test_to_dict_Amenity(self):
        """ """
        self.assertEqual('to_dict' in dir(self.amenity), True)


if __name__ == "__main__":
    unittest.main()