#!/usr/bin/python3
""" Tests Amenity """

import unittest
import os
import pep8
import datetime
from models import amenity
Amenity = amenity.Amenity

class Test_Amenity(unittest.TestCase):
    """ Tests amenity """

    def test_pep8(self):
        """ Tests the pep8 """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0, "Check pep8")

    def test_Amenity_dict(self):
        """Amenity_dict"""
        self.assertTrue('id' in self.amenity.__dict__)
        self.assertTrue('created_at' in self.amenity.__dict__)
        self.assertTrue('updated_at' in self.amenity.__dict__)
        self.assertTrue('name' in self.amenity.__dict__)
   
    def test_save_Amenity(self):
        """Amenity save"""
        self.amenity.save()
        self.assertNotEqual(self.amenity.created_at, self.amenity.updated_at)

if __name__ == '__main__':
    unittest.main()
