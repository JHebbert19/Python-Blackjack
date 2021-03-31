# This is a program for BlackJack
import secrets

cards = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

def HandValue(cards):
    value = 0
    aces = 0

    for items in cards:
        if items == "Jack":
            value = value + 10
        elif items == "Queen":
            value = value +10
        elif items == "King":
            value = value + 10
        elif items == "Ace":
            aces += 1
        else:
            value = value + int(items)

    for items in range(aces):
        if (value + 11) < 22:
            value += 11
        else:
            value += 1

    return value



Loop = "True"
while (Loop == "True"):
    PlayerHand = []
    DealerHand = []
    PlayChoice = input("Would you like to play? ")
    if (PlayChoice == "Y") or (PlayChoice == "y"):
        PlayerHand.append(secrets.choice(cards))
        PlayerHand.append(secrets.choice(cards))

        DealerHand.append(secrets.choice(cards))
        DealerHand.append(secrets.choice(cards))

        print("Here is your hand: ", PlayerHand)
        print("H is for Hit Me. X is for Hold")

        Loop2 = "True"
        while (Loop2 == "True"):
            choice = input("What would you like to do? ")

            if (choice == "H") or (choice == "h"):
                PlayerHand.append(secrets.choice(cards))
                print("Here is your updated hand: ", PlayerHand)

            elif (choice == 'X') or (choice == 'x'):
                print("The dealer has ", DealerHand)

                PlayerValue = HandValue(PlayerHand)
                DealerValue = HandValue(DealerHand)

                if PlayerValue > 21:
                    print("You Busted")
                elif DealerValue > 21:
                    print("The dealer Busted. You Won!")
                elif DealerValue > 21 and PlayerValue > 21:
                    print("You both Busted")
                elif DealerValue >= PlayerValue:
                    print("You Lost")
                else:
                    print("You Won!")
                Loop2 = "False"
            else:
                print("That was not a correct entry")
    elif (PlayChoice == "N") or (PlayChoice == "n"):
        print("Thank you for playing")
        Loop = "False"

    else:
        print("That was not a correct entry!!!")










