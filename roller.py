from dice_functions import dfour, dsix, deight, dten, dtwelve, dtwenty

available_dice = {
    "1": "D4",
    "2": "D6",
    "3": "D8",
    "4": "D10",
    "5": "D12",
    "6": "D20"
}

current_choice = None

while current_choice != "0":
    if current_choice in available_dice:
        if current_choice == "1":
            total_rolls = int(input("How many D4s do you need to roll: "))
            if total_rolls == 1:
                print(f"You rolled a D4 and got: ", dfour())
            elif total_rolls >= 2:
                totals = []
                for number in range(total_rolls + 1):
                    totals.append(dfour())
                g_total = sum(totals)
                print(f"You rolled {total_rolls} D4s and the total is: ",
                      g_total)
            else:
                pass
        elif current_choice == "2":
            total_rolls = int(input("How many D6s do you need to roll: "))
            if total_rolls == 1:
                print(f"You rolled a D6 and got: ", dsix())
            elif total_rolls >= 2:
                totals = []
                for number in range(total_rolls + 1):
                    totals.append(dsix())
                g_total = sum(totals)
                print(f"You rolled {total_rolls} D6s and the total is: ",
                      g_total)
            else:
                pass
        elif current_choice == "3":
            total_rolls = int(input("How many D8s do you need to roll: "))
            if total_rolls == 1:
                print(f"You rolled a D8 and got: ", deight())
            elif total_rolls >= 2:
                totals = []
                for number in range(total_rolls + 1):
                    totals.append(deight())
                g_total = sum(totals)
                print(f"You rolled {total_rolls} D8s and the total is: ",
                      g_total)
            else:
                pass
        elif current_choice == "4":
            total_rolls = int(input("How many D10s do you need to roll: "))
            if total_rolls == 1:
                print(f"You rolled a D10 and got: ", dten())
            elif total_rolls >= 2:
                totals = []
                for number in range(total_rolls + 1):
                    totals.append(dten())
                g_total = sum(totals)
                print(f"You rolled {total_rolls} D10s and the total is: ",
                      g_total)
            else:
                pass
        elif current_choice == "5":
            total_rolls = int(input("How many D12s do you need to roll: "))
            if total_rolls == 1:
                print(f"You rolled a D12 and got: ", dtwelve())
            elif total_rolls >= 2:
                totals = []
                for number in range(total_rolls + 1):
                    totals.append(dtwelve())
                g_total = sum(totals)
                print(f"You rolled {total_rolls} D12s and the total is: ",
                      g_total)
            else:
                pass
        elif current_choice == "6":
            total_rolls = int(input("How many D20s do you need to roll: "))
            if total_rolls == 1:
                print(f"You rolled a D20 and got: ", dtwenty())
            elif total_rolls >= 2:
                totals = []
                for number in range(total_rolls + 1):
                    totals.append(dtwenty())
                g_total = sum(totals)
                print(f"You rolled {total_rolls} D20s and the total is: ",
                      g_total)
            else:
                pass
    else:
        for key, value in available_dice.items():
            print(f'{key}: {value}')
        print("0: Stop rolling")

    current_choice = input("Please choose a dye from the list above to roll: ")
