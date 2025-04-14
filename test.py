import math

def custom_round(value):
    try:
        number = float(value)
        fractional_part = number - int(number)
        if fractional_part >= 0.7:
            return math.ceil(number)
        else:
            return math.floor(number)
    except ValueError:
        return 0




print(round(3.1415926, 3))