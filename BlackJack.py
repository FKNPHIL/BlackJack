import db as db
import playGame as pG
import random


def makeCards():
    suits = ["♣", "♥", "♠", "♦"]
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
    deck = makeCards()
    print("WELCOME TO BLACKJACK!")
    print("BlackJack Payout is 3:2\n")
    print("Your Available Money: " + str(db.viewMoney()))
    if db.viewMoney() <= 4:
        getMoney = pG.getMoney()

    while True:
        choice = pG.getChoice()
        wager = pG.getWager()
        playerCards = pG.playerCards(deck)
        dealerCards = pG.dealerCards(deck)
        playerScore = pG.getScores(playerCards)
        dealerScore = pG.getScores(dealerCards)
        print("\nDEALERS CARDS:")
        print(dealerCards[0][1], dealerCards[0][0])
        print("? ???")
        print("\nYOUR CARDS:")
        for card in playerCards:
            print(card[1], card[0])
        print()

        if len(playerCards) == 2:
            if (playerCards[0][2]) == 11 and (playerCards[1][2]) == 11:
                playerCards[0][2] = 1
                playerScore -= 10

        if len(dealerCards) == 2:
            if (dealerCards[0][2]) == 11 and (dealerCards[1][2]) == 11:
                dealerCards[0][2] = 1
                dealerScore -= 10

        if playerScore == 21:
            print("BLACKJACK you win")
            bjWin = db.winMoney(wager * 1.5)
            continue


        while playerScore <= 21:
            playerChoice = input("(H)it or (S)tand >>")
            if playerChoice.lower() != "h" and playerChoice.lower() != "s":
                print("You must enter either 'h' or 's'")
                continue

            if playerChoice.lower() == "h":
                playerCard = random.choice(deck)
                playerCards.append(playerCard)
                deck.remove(playerCard)
                playerScore = pG.getScores(playerCards)
                if playerScore > 21:
                    for card in playerCards:
                        if card[2] == 11:
                            card[2] = 1
                            playerScore -= 10
                for card in playerCards:
                    print(card[1], card[0])
            else:
                print("\nDEALERS CARDS")
                for card in dealerCards:
                    print(card[1], card[0])
                break
            if playerScore > 21:
                print("YOU BUSTED")
                break

        while dealerScore <= 17 and playerScore <= 21:
            print("DEALER MUST HIT")
            dealerCard = random.choice(deck)
            dealerCards.append(dealerCard)
            deck.remove(dealerCard)
            input("Press enter to continue....")
            print(dealerCard[1], dealerCard[0])
            dealerScore = pG.getScores(dealerCards)
            if dealerScore > 21:
                for card in dealerCards:
                    if card[2] == 11:
                        card[2] = 1
                        dealerScore -= 10

        if dealerScore == 21:
            print("DEALER HAS BLACKJACK")
        if dealerScore > 21:
            print("DEALER BUSTED")
        if playerScore == 21 and dealerScore > 17:
            print()
            print("YOU GOT BLACKJACK!!")

        print()
        print("Players Score is "+str(playerScore))
        print("DealerScore is "+str(dealerScore))
        didWin = pG.checkForWin(playerScore, dealerScore)
        if didWin == 1:
            bjWin = db.winMoney(wager * 1.5)
        if didWin == 0:
            bjWin = db.winMoney(wager)
        print("Your Available Money: "+ str(db.viewMoney()))
        if (db.viewMoney()) <= 4:
            print("\nYOU HAVE BEEN BANKRUPTED! GOOD THING YOU WEREN'T PLAYING FOR REAL MONEY!")
            getmoney = pG.getMoney()

        if len(deck) <=26:
            print("\nHalf deck used, dealer is reshuffling...")
            deck = makeCards()
            input("Deck shuffled press enter to continue...")


if __name__ == '__main__':
    main()

