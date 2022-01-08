# AirBnB Clone - The console
the console for airbnb project. Create a command interpreter that can modify or delete the database
The users like the administrator of the app Airbnb clone has the posibility of the manipulate objects and data of the application, this objects are:
 
 * Users
 * Places
 * States
 * Cities
 * Amenities
 * Reviews


![alt text](https://i.ibb.co/RSzZ5yh/815046647d23428a14ca.png)


## Requirements


## Python Scripts

    Allowed editors: vi, vim, emacs
    All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
    All your files should end with a new line
    The first line of all your files should be exactly #!/usr/bin/python3
    A README.md file, at the root of the folder of the project, is mandatory
    Your code should use the PEP 8 style (version 1.7 or more)
    All your files must be executable
    The length of your files will be tested using wc
    All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
    All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
    All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')

## Python Unit Tests

    Allowed editors: vi, vim, emacs
    All your files should end with a new line
    All your test files should be inside a folder tests
    You have to use the unittest module
    All your test files should be python files (extension: .py)
    All your test files and folders should start by test_
    Your file organization in the tests folder should be the same as your project
    e.g., For models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py
    e.g., For models/user.py, unit tests must be in: tests/test_models/test_user.py
    All your tests should be executed by using this command: python3 -m unittest discover tests
    You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
    All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
    All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
    All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
    We strongly encourage you to work together on test cases, so that you don’t miss any edge 
 
 
## Installation
 
 For use this console you need to have:
 * Linux ubuntu 14.04.3 LTS or higger
 * Python 3.7 or higger

## Files



 -  HBNHCommand: console.py
 -  Amenity: models/amenity.py
 -  BaseModel: models/base_model.py
 -  City: models/city.py
 -  models.init : models/__init__.py
 -  Place: models/place.py
 -  Review: models/review.py
 -  State: models/state.py
 -  User: models/user.py
 -  FileStorage: models/engine/file_storage.py
 -  engine.init: models/engine/__init__.py

```
How To run the command interpreter:
```
$ ./console.py


## Examples

Interactive mode:
```
$ ./console.py
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
(hbnb)
(hbnb) quit
$
```
Non-interactive mode:
```
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

## AUTHORS
 
* **Boumaiza Kais** - [Boumaiza-kais](https://github.com/Boumaiza-kais)
* **Lafine Sami** - [afinesami](https://github.com/afinesami)