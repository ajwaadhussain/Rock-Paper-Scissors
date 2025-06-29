import random

user_win = 0
computer_win = 0
options=['rock','scissors','paper']

while True:
    user_pick = input("choose rock/paper/scissors or quit").lower()
    
    if user_pick == 'q':
        break
    
    if user_pick not in options:
        continue
    
    random_num = random.randint(0,2)
    computer_pick = options[random_num]
    print("Computer picked " + computer_pick)
    
    if user_pick == "rock" and computer_pick == "scissors":
        print("You Won!")
        user_win += 1
        
    elif user_pick == "scissors" and computer_pick == "paper":
        print("You Won!")
        user_win += 1
        
    elif user_pick == "paper" and computer_pick == "rock":
        print("You Won!")
        user_win += 1    
    
    elif user_pick == computer_pick:
        print("Draw")
     
    else:
        print("You Lost!")
        computer_win += 1
        
print("You Won " + str(user_win) + " times")
print("Computer Won " + str(computer_win) + " times")
print("Goodbye")
