import random
import db as db
import sys

def getChoice():
    while True:
        choice = input("\nWould you like to play a game? (Y)es or (N)o >>")
        if choice.lower() == "y":
           return choice
        if choice.lower() == "n":
            print("OK GOODBYE!")
            exit()
        if choice.lower() != "y":
            print("YOU MUST ENTER 'Y' or 'N'")
            continue

def getWager():
    maxWagerAmount = db.viewMoney()
    while True:
        try:
            wagerAmount = round(float(input("Enter your wager amount (5 to 1000) >>")), 2)
            if wagerAmount < 5 or wagerAmount > 1000:
                print("You must enter a correct number between 5 and 1000")
                continue
            if wagerAmount > maxWagerAmount:
                print("You only have " + str(maxWagerAmount) + " available to wager")
                continue
            bjLoss = db.betMoney(wagerAmount)
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

def getMoney():
    while True:
        getMoney = input("You don't have enough money. Would you like to get more? (Y)es or (N)o >>")
        if getMoney.lower() == "y":
            bjWin = db.winMoney(1000)
            input("1000 added. Press enter to continue....")
            break
        if getMoney.lower() == "n":
            print("You need money to wager. Exiting program")
            sys.exit()
        else:
            print("You need to enter 'y' or 'n'")
            continue