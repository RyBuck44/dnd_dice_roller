import random


def d_roller(die, rolls) -> int:
    numbers = []
    for number in range(rolls):
        roll = random.randint(1, die)
        numbers.append(roll)
    g_total = sum(numbers)
    return g_total
