import random


def coin_flip():
    coin = ['Heads', 'Tails']
    result = random.choice(coin)
    return result


def d_roller(die, rolls) -> int:
    numbers = []
    for number in range(rolls):
        roll = random.randint(1, die)
        numbers.append(roll)
    g_total = list(numbers)
    return g_total


