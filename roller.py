from dice_functions import dfour, dsix, deight, dten, dtwelve, dtwenty

available_dice = {
    "4": dfour,
    "6": dsix,
    "8": deight,
    "10": dten,
    "12": dtwelve,
    "20": dtwenty,
}

while True:
    t_roll = str(input("Enter the type and amount of dice in the num d die format: "))
    x = t_roll.split('d')
    die = x[1]
    rolls = int(x[0])
    if die in available_dice:
        total = available_dice[die](rolls)
        print(total)
    else:
        break
