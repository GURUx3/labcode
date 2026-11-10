def fibonacci(count):
    """Generate the first count numbers in the Fibonacci sequence."""
    sequence = []
    first, second = 0, 1

    for _ in range(count):
        sequence.append(first)
        first, second = second, first + second

    return sequence


print(fibonacci(10))
