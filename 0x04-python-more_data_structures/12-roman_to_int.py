#!/usr/bin/python3
if __name__ == "__main__":
    def roman_to_int(roman_string):
            if type(roman_string) is not str:
                return 0
            rom = (("I", 1), ("V", 5), ("X", 10), ("L", 50), ("C", 100), ("D", 500), ("M", 1000))
            num = 0
            prev = None
            for x in roman_string:
                for y in rom:
                    if y[0] == x:
                        num += y[1]
                        if prev and rom.index(prev) < rom.index(y):
                                num -= prev[1] * 2
                        prev = y
                    break
            return (num)
