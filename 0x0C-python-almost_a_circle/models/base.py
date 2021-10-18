#!/usr/bin/python3
''' models/base.py
'''
import json


class Base:
    ''' first class Base
    '''

    __nb_objects = 0

    def __init__(self, id=None):
        ''' initialize Base  __init__
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def save_to_file(cls, list_objs):
        '''method: save_to_file
        '''
        list_dicts = []
        if list_objs is not None:
            for obj in list_objs:
                tmp_dict = cls.to_dictionary(obj)
                list_dicts.append(tmp_dict)
            json_L_of_D = cls.to_json_string(list_dicts)
        else:
            json_L_of_D = "[]"

        filename = cls.__name__ + ".json"

        with open(filename, "w") as file:
            num_char = file.write(json_L_of_D)

    @staticmethod
    def to_json_string(list_dictionaries):
        ''' method json string
        '''
        ret_list = []
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        if type(list_dictionaries) != list:
            ret_list.append(list_dictionaries)
        else:
            ret_list = list_dictionaries
        return json.dumps(ret_list)

    @staticmethod
    def to_json_string(list_dictionaries):
        ''' method json string
        '''
        ret_list = []
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        if type(list_dictionaries) != list:
            ret_list.append(list_dictionaries)
        else:
            ret_list = list_dictionaries
        return json.dumps(ret_list)
