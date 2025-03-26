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

# Example usage:
print(custom_round(5.7))  # Output: 6
print(custom_round(5.6))  # Output: 5