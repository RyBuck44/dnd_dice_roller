from dice_functions import d_roller

available_dice = [
    4,
    6,
    8,
    10,
    12,
    20,
]

while True:
    t_roll = str(input("Enter the types and amounts of dice in the "
                       "(num d die,) format: "))
    all_dice = t_roll.split(',')
    total_number = []
    for dice in all_dice:
        d = dice.split('d')
        die = int(d[1])
        rolls = int(d[0])
        if die in available_dice:
            total = d_roller(die, rolls)
            total_number.append(total)
        else:
            break
    final_number = sum(total_number)
    print("Your final total is: ", final_number)
