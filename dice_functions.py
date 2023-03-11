import random


def dfour() -> int:
    """
    This function is called on when the user wants to roll a d4 dye
    :return: number between 1 and 4
    """
    roll = random.randint(1, 4)
    return roll


def dsix() -> int:
    """
    This function is called on when the user wants to roll a d6 dye
    :return: number between 1 and 6
    """
    roll = random.randint(1, 6)
    return roll


def deight() -> int:
    """
    This function is called on when the user wants to roll a d8 dye
    :return: number between 1 and 8
    """
    roll = random.randint(1, 8)
    return roll


def dten() -> int:
    """
    This function is called on when the user wants to roll a d10 dye
    :return: number between 1 and 10
    """
    roll = random.randint(1, 10)
    return roll


def dtwelve() -> int:
    """
    This function is called on when the user wants to roll a d12 dye
    :return: number between 1 and 12
    """
    roll = random.randint(1, 12)
    return roll


def dtwenty() -> int:
    """
    This function is called on when the user wants to roll a d20 dye
    :return: number between 1 and 20
    """
    roll = random.randint(1, 20)
    return roll
