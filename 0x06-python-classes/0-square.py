#!/usr/bin/python3
'print(__import__("my_module").my_function.__doc__)'
python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')

class Square():
    '''
        An empty square class
    '''
    pass
