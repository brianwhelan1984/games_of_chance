import random

total = 100

#Write your game of chance functions here

def heads_or_tails(guess, bet):
    #making sure bet is valid
    if bet <= 0 :
        print("Please bet some money to play game!")
        return 0
    
    #start the game and select coin
    print('Lets play, you selected ' + guess)
    #computers result
    result = random.randint(1,2)
    if result == 1:
        print("Heads it is")
    elif result == 2:
        print("Tails it is")
    
    #determine winner")
    if (result == 1 and guess == "Heads") or (result == 2 and guess == "Tails"):
        winnings = bet * 2
        print("Congrats you won" + str(winnings) + ".")
        return winnings
    else:
        print("You lost ")
        return -bet

def cho_han(guess, bet):
    if bet <= 0 :
        print("Please bet some money to play game!")
        return 0

    print("Lets play Cho Han! your guess is " + str(guess)+ " and you bet "+ str(bet) + ".")
#simulates a dice roll and adds them together for a result
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    total = dice1 + dice2
    print("The winning number is "+ str(total) + ".")

    if (total % 2 == 0 and guess == "Even") or (total % 2 !=0 and guess == "Odd" ):
        winnings= bet * 2
        print("Congrats you win " + str(winnings))
        return winnings
    else:
        print("Sorry you loose" +str(bet))
        return -bet

def pick_a_card(bet):
    if bet <= 0 :
        print("Please bet some money to play game!")
        return 0
    
    print("Lets play pick a card your bet is " + str(bet))
    computer_card = random.randint(1,13)
    player_card = random.randint(1,13)

    print("Your card is " + str(player_card) + " and the computers card is " + str(computer_card) + ".")

    if computer_card > player_card:
        print("Computer Wins! you losse " + str(bet) +".")
        return -bet
    elif player_card > computer_card:
        winnings = bet*2
        print("You win " + str(winnings) + ".")
        return winnings
    else:
        print("It's a draw.")
        return 0

def roulette(guess, bet):
    if bet <= 0 :
        print("Please bet some money to play game!")
        return 0

    # find the winning number
    print("Lets play roulette your guess is " +str(guess)+ " and you bet "+ str(bet)+ ".")
    winning_number = random.randint(1,37)
    if winning_number == 37:
        print("The wheel landed on 00.")
    else:
        print("The wheel landed on " + str(winning_number) + ">")

    if guess % 2 == 0 and winning_number % 2 ==0 and winning_number != 0 :
        print("Congrats you won! "+ str(bet) + ".")
        return bet

    elif guess % 2 != 0 and winning_number %2 != 0 and winning_number != 37:
        print("Congrats you won! "+ str(bet) + ".")

    elif guess == winning_number:
        winnings = bet*35
        print("Congrats you've picked thw winning number you've won " + str(winnings) + ".")
        return winnings

    else:
        print("Sorry you've lost!")
        return -bet

total += heads_or_tails("Heads", 10)
total += pick_a_card(5)
total += cho_han("Even", 2)
total += roulette(13, 10)
total += roulette(3, 1)
total += roulette(22, total)
print("Your total amount of money is " + str(total))