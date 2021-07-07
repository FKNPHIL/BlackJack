import db as db
import playGame as pG
import random


def makeCards():
    suits = ["clubs", "hearts", "spades", "diamonds"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

    deck = []
    for suit in suits:
        counter = 0
        for rank in ranks:
            newCard = []
            newCard.append(suit)
            newCard.append(rank)
            newCard.append(values[counter])
            deck.append(newCard)
            counter += 1
    return deck

def main():
    print("WELCOME TO BLACKJACK!")
    print("BlackJack Payout is 3:2\n")
    print("Your Available Money: "+ str(db.viewMoney()))
    choice = input("Would you like to play a game (y/n) >>")
    while choice.lower() == "y":
        deck = makeCards()
        wager = pG.getWager()
        playerCards = pG.playerCards(deck)
        dealerCards = pG.dealerCards(deck)
        playerScore = pG.getScores(playerCards)
        dealerScore = pG.getScores(dealerCards)
        print("\nDEALER'S SHOW CARD:")
        for card in dealerCards:
            print(card[1], card[0])
        print("\nYOUR CARDS:")
        for card in playerCards:
            print(card[1], card[0])
        print()

        playerChoice = input("h to Hit or s to Stand (h/s): ")
        if playerChoice.lower() != "h" and playerChoice.lower() != "s":
            print("You must enter either 'h' or 's'")
            continue

        if playerChoice.lower() == "h":
            playerCards = []
            playerCard = random.choice(deck)
            playerCards.append(playerCard)
            deck.remove(playerCard)
            print(playerCards)
            for card in playerCards:
                print(card[1], card[0])
            



        print("BYE!")
        break
    db.betMoney(wager)
    db.winMoney(0)
    money = db.viewMoney()
    print(money)
    print(makeCards())
    exit()

    #playerCard1;
    #dealerCard1;
    #playerCard2;
    #dealerCard2;





if __name__ == '__main__':
    main()

