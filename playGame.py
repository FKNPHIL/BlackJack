import random

def getChoice():
    while True:
        choice = input("Would you like to play a game (y/n) >>")
        if choice.lower() == "y":
            return choice
        if choice.lower() == "n":
            print("OK GOODBYE!")
            exit()
        if choice.lower() != "y":
            print("YOU MUST ENTER 'Y' or 'N'")
            continue

def getWager():
    while True:
        try:
            wagerAmount = int(input("Enter your wager amount (5 to 1000) >>"))
            if wagerAmount < 5 or wagerAmount > 1000:
                print("You must enter a correct number between 5 and 1000")
                continue
            return wagerAmount
        except ValueError:
            print("You must enter a number between 5 and 1000")
        except Exception as e:
            print("Error occurred", type(e), e)
            exit()


def playerCards(deck):
    playerCards = []

    playerCard = random.choice(deck)
    playerCards.append(playerCard)
    deck.remove(playerCard)

    playerCard = random.choice(deck)
    playerCards.append(playerCard)
    deck.remove(playerCard)

    return playerCards


def dealerCards(deck):
    dealerCards = []

    dealerCard = random.choice(deck)
    dealerCards.append(dealerCard)
    deck.remove(dealerCard)

    dealerCard = random.choice(deck)
    dealerCards.append(dealerCard)
    deck.remove(dealerCard)

    return dealerCards


def getScores(handCards):
    total = 0
    for card in handCards:
        score = card[2]
        total += score
    return total


def playerChoice(deck):
    while True:
        try:
            playerChoice = input("h to Hit or s to Stand (h/s): ")
            if playerChoice.lower() != "h" and playerChoice.lower() != "s":
                print("You must enter either 'h' or 's'")
                continue
        except ValueError:
            print("Invalid selection. Please choose h or s only")
        except Exception as e:
            print("Error Occurred", type(e), e)
            exit()


        if playerChoice.lower() == "s":
            dealerCards = []
            dealerCard = random.choice(deck)
            dealerCards.append(dealerCard)
            deck.remove(dealerCard)
            return dealerCards
        else:
            break

def checkForWin(playerScores, dealerScores):
    if (playerScores == dealerScores):
        print("GAME IS TIED")
        return 0
    if (playerScores > 21):
        print("YOU HAVE LOST SORRY!")
        return -1
    if (dealerScores > 21):
        print("YOU HAVE WON CONGRATS!")
        return 1
    if (playerScores > dealerScores):
        print("YOU HAVE WON CONGRATS!")
        return 1
    if (playerScores < dealerScores):
        print("YOU HAVE LOST SORRY!")
        return -1
