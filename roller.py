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
    t_roll = str(input("Enter the types and amounts of dice in the "
                       "(num d die,) format: "))
    all_dice = t_roll.split(',')
    total_number = []
    for dice in all_dice:
        d = dice.split('d')
        die = d[1]
        rolls = int(d[0])
        if die in available_dice:
            total = available_dice[die](rolls)
            total_number.append(total)
        else:
            break
    final_number = sum(total_number)
    print("Your final total is: ", final_number)
