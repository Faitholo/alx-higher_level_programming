#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):

    new_list = []
    index = 0
    if list_length <= 0:
        print("out of range")
        return new_list
    while index < list_length:
        try:
            new_list.append(my_list_1[index] / my_list_2[index])
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)
        except TypeError:
            print("wrong type")
            new_list.append(0)
        except IndexError:
            print("out of range")
            new_list.append(0)
        finally:
            index += 1
    return new_list
