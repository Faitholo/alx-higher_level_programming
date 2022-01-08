#!/usr/bin/python3
""" Test Place """

import unittest
import pep8
from models import place
from models.base_model import BaseModel

class Test_Place(unittest.TestCase):
    """ Tests Place """

    def test_pep8(self):
        """ Tests pep8 """
        pep8style = pep8.StyleGuide(quite=True)
        result = pep8style.check_files(["models/place.py"])
        self.assertEqual(result.total_errors, 0, "Check pep8")


    def test_Place_dict(self):
        """ Place_dict """
        self.assertTrue('id' in self.place.__dict__)
        self.assertTrue('created_at' in self.place.__dict__)
        self.assertTrue('updated_at' in self.place.__dict__)
        self.assertTrue('city_id' in self.place.__dict__)
        self.assertTrue('user_id' in self.place.__dict__)
        self.assertTrue('name' in self.place.__dict__)
        self.assertTrue('__class__' in self.place.__dict__)

    def test_save_Place(self):
        """ Save_Place """
        self.place.save()
        self.assertNotEqual(self.place.created_at, self.place.updated_at)

if __name__ == '__main__':
    unittest.main()
