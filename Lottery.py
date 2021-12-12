#   This python program will produce three(3) random numbers just like a lottery.
#   If the user managed to guess the right numbers then he/she is considered a winner!
#   In this program, 'for', 'while', and 'if - else' loops has been used.

reset = True

while reset:
     
    import random
 
    userInput = []

#   This python program will produce three(3) random numbers just like a lottery.
    for i in range (0,3):
        num = int(input("Input random numbers between 0 to 99: "))
        while (num in userInput or num < 0 or num > 99):
            print("The entered number is invalid! Please try again.")
            num = int(input("Input random numbers between 0 to 99: "))

        userInput.append(num)

    LotteryNumber = []

    for i in range (0,3):
        num = random.randint(0, 99)
        while num in LotteryNumber:
            num = random.randint(0, 99)

        LotteryNumber.append(num)

    print("Lottery result: ")
    print(LotteryNumber)

    print("Your 3 random numbers are: ")
    print(userInput)
    
#   If the user managed to guess the right numbers then he/she is considered a winner!
#   In this program, 'for', 'while', and 'if - else' loops has been used.
    if num in userInput == LotteryNumber:
        print("JACKPOT\n")
    else:
        print("Close! try again\n")

    reset = input("Do you want to try again?\nPress [y] to restart or [n] to quit: ")
    if reset == "n":
        reset = False
    if reset == "y":
        reset = True