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
    while True:

        choice = input("Would you like to play a game (y/n) >>")
        if choice.lower() == "n":
            break
        deck = makeCards()
        wager = pG.getWager()
        playerCards = pG.playerCards(deck)
        dealerCards = pG.dealerCards(deck)
        playerScore = pG.getScores(playerCards)
        dealerScore = pG.getScores(dealerCards)
        print("\nDEALER'S SHOW CARD:")
        print(dealerCards[0][1] + dealerCards[0][0])
        print("? ???")
        # for card in dealerCards:
        #     print(card[1], card[0])
        print("\nYOUR CARDS:")
        for card in playerCards:
            print(card[1], card[0])
        print()


        while playerScore <=20:
            playerChoice = input("h to Hit or s to Stand (h/s): ")
            if playerChoice.lower() != "h" and playerChoice.lower() != "s":
                print("You must enter either 'h' or 's'")
                continue

            if playerChoice.lower() == "h":
                playerCard = random.choice(deck)
                playerCards.append(playerCard)
                deck.remove(playerCard)
                print(playerCards)
                playerScore = pG.getScores(playerCards)
                for card in playerCards:
                    print(card[1], card[0])

            else:
                print("DEALERS CARDS")
                for card in dealerCards:
                    print(card[1], card[0])
                break
        if playerScore > 21:
            print("YOU BUSTED")
            #loss

            continue

        while dealerScore <=17:
            print("DEAL MUST HIT")
            dealerCard = random.choice(deck)
            dealerCards.append(dealerCard)
            deck.remove(dealerCard)
            print(dealerCard[1], dealerCard[0])
            dealerScore = pG.getScores(dealerCards)

        print(dealerScore)
        didWin = pG.checkForWin()

if __name__ == '__main__':
    main()

