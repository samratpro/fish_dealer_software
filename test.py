import math

def custom_round(value):
    try:
        number = float(value)
        fractional_part = number - int(number)
        if fractional_part >= 0.6999999:
            return math.ceil(number)
        else:
            return math.floor(number)
    except ValueError:
        return 0




print(custom_round(380.7))