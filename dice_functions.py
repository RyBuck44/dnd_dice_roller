import random


def dfour(rolls) -> int:
    """
    Function that generates a number between 1 and 4. Can be called
        multiple times and will return sum of all numbers generated.
    :param rolls: Amount of times the die will be rolled.
    :return: sum of all the rolls
    """
    numbers = []
    for number in range(rolls):
        roll = random.randint(1, 4)
        numbers.append(roll)
    g_total = sum(numbers)
    return g_total


def dsix(rolls) -> int:
    """
    Function that generates a number between 1 and 6. Can be called
        multiple times and will return sum of all numbers generated.
    :param rolls: Amount of times the die will be rolled.
    :return: sum of all the rolls
    """
    numbers = []
    for number in range(rolls):
        roll = random.randint(1, 6)
        numbers.append(roll)
    g_total = sum(numbers)
    return g_total


def deight(rolls) -> int:
    """
    Function that generates a number between 1 and 8. Can be called
        multiple times and will return sum of all numbers generated.
    :param rolls: Amount of times the die will be rolled.
    :return: sum of all the rolls
    """
    numbers = []
    for number in range(rolls):
        roll = random.randint(1, 8)
        numbers.append(roll)
    g_total = sum(numbers)
    return g_total


def dten(rolls) -> int:
    """
    Function that generates a number between 1 and 10. Can be called
        multiple times and will return sum of all numbers generated.
    :param rolls: Amount of times the die will be rolled.
    :return: sum of all the rolls
    """
    numbers = []
    for number in range(rolls):
        roll = random.randint(1, 10)
        numbers.append(roll)
    g_total = sum(numbers)
    return g_total


def dtwelve(rolls) -> int:
    """
    Function that generates a number between 1 and 12. Can be called
        multiple times and will return sum of all numbers generated.
    :param rolls: Amount of times the die will be rolled.
    :return: sum of all the rolls
    """
    numbers = []
    for number in range(rolls):
        roll = random.randint(1, 12)
        numbers.append(roll)
    g_total = sum(numbers)
    return g_total


def dtwenty(rolls) -> int:
    """
    Function that generates a number between 1 and 20. Can be called
        multiple times and will return sum of all numbers generated.
    :param rolls: Amount of times the die will be rolled.
    :return: sum of all the rolls
    """
    numbers = []
    for number in range(rolls):
        roll = random.randint(1, 20)
        numbers.append(roll)
    g_total = sum(numbers)
    return g_total



