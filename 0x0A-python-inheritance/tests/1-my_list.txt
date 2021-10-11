0t.txt module
====================

Importing the class from the module:
>>> MyList = __import__("1-my_list").MyList

Checking for module docstring:
>>> m = __import__("1-my_list").__doc__
>>> len(m) > 1
True

Checking for class docstring:
>>> c = __import__("1-my_list").MyList.__doc__
>>> len(c) > 1
True

Checking for method docstring
        >>> f = __import__("1-my_list").MyList.print_sorted.__doc__
        >>> len(f) > 1
        True

Checking given test case
>>> my_list = MyList()

>>> my_list.append(1)

>>> my_list.append(4)

>>> my_list.append(2)

>>> my_list.append(3)

>>> my_list.append(5)

>>> print(my_list)
[1, 4, 2, 3, 5]

>>> my_list.print_sorted()
[1, 2, 3, 4, 5]

>>> print(my_list)
[1, 4, 2, 3, 5]

Checking empty object
>>> obj1 = MyList()

>>> print(obj1)
[]

>>> obj1.print_sorted()
[]

Checking negative values
>>> obj2 = MyList()

>>> obj2.append(-1)

>>> obj2.append(0)

>>> obj2.append(-233)

>>> obj2.append(-9)

>>> print(obj2)
[-1, 0, -233, -9]

>>> obj2.print_sorted()
[-233, -9, -1, 0]

Checking NULL object
>>> obj3 = MyList()

>>> obj3.append(NULL)
Traceback (most recent call last):
    ...
NameError: name 'NULL' is not defined

>>> print(obj3)
[]

>>> obj3.print_sorted()
[]

Checking NaN object
>>> obj4 = MyList()

>>> obj4.append(NaN)
Traceback (most recent call last):
    ...
NameError: name 'NaN' is not defined

>>> print(obj4)
[]

>>> obj4.print_sorted()
[]

Checking None object
>>> obj5 = MyList()

>>> obj5.append(None)

>>> print(obj5)
[None]

>>> obj5.print_sorted()
[None]
