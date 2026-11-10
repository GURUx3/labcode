def is_even(number):
    """Return True when number is evenly divisible by two."""
    return number % 2 == 0


values = range(1, 11)
even_values = [value for value in values if is_even(value)]
print(even_values)
