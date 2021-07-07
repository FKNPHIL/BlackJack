def viewMoney():
    try:
        with open("money.txt", 'r') as file:
            money = float(file.readline())
        return money
    except FileNotFoundError:
        print("File not found, Exiting program")
        exit()
    except Exception as e:
        print("Error Occurred", type(e), e)
        exit()

def winMoney(bjWins):
    startMoney = viewMoney()
    winMoney = startMoney + bjWins
    with open("money.txt", "w", newline="") as file:
        file.write(str(winMoney))

def betMoney(bjLoss):
    startMoney = viewMoney()
    lossMoney = startMoney - bjLoss
    with open("money.txt", "w", newline="") as file:
        file.write(str(lossMoney))


