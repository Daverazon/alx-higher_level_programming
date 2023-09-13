#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        keys = tuple(a_dictionary)
        values = [a_dictionary[key] for key in keys]
        big = values[0]
        for v in values:
            if big < v:
                big = v
        return keys[values.index(big)]
