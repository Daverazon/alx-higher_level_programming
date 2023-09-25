#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    index = 0
    new = []
    for x, y in zip(my_list_1, my_list_2):
        result = 0
        if index < list_length:
            try:
                result = x / y
            except (ValueError, TypeError):
                print("wrong type")
            except ZeroDivisionError:
                print("division by zero")
            finally:
                index += 1
                new.append(result)
    while index < list_length:
        print("out of range")
        new.append(0)
        index += 1
    return (new)
