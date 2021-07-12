def viewMoney():
    try:
        with open("money.txt", 'r') as file:
            money = float(file.readline())
            money = round(money, 2)
        return money
    except FileNotFoundError:
        print("Money.txt not found, Creating a new file with 0 balance added")
        with open("money.txt", "w", newline="") as file:
            file.write(str(0))
    except Exception as e:
        print("Error Occurred", type(e), e)
        exit()

def winMoney(bjWins):
    startMoney = viewMoney()
    winMoney = startMoney + round(bjWins, 2)
    with open("money.txt", "w", newline="") as file:
        file.write(str(winMoney))

def betMoney(bjLoss):
    startMoney = viewMoney()
    lossMoney = startMoney - bjLoss
    with open("money.txt", "w", newline="") as file:
        file.write(str(lossMoney))


