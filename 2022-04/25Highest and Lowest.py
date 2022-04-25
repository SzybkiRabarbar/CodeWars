def high_and_low(numbers):
    numbers=[int(n) for n in numbers.split()]
    return f'{max(numbers)} {min(numbers)}'