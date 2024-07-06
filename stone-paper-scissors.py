# Import random module
import random
print('Stone - Paper - Scissors')
 
 
# Input no. of rounds
n = int(input('Enter number of rounds: '))
 
 
# List containing Snake(s), Water(w), Gun(g)
options = ['s', 'p', 'x']
 
# Round numbers
rounds = 1
 
# Count of computer wins
Comp = 0
 
# Count of player wins
User = 0
 
 
# There will be n rounds of game
while rounds <= n:
    comp = 0
    user = 0
    comp_win=0
    user_win=0
    
    # Display round
    print(f"Round :{rounds}\nStone - 's'\nPaper - 'p'\nScissors - 'x'")
 
    # Exception handling
    try:
        player = input("Choose your option (type 'exit' to quit): ")
        if player == 'exit':
            print("Exiting the game.")
            break
        #Process the input here
        print(f"You choose: {player}")
    except EOFError as e:
        print("EOFError occurred: No input received. Please try again.")
 
    # Control of bad inputs
    if player != 's' and player != 'p' and player != 'x':
        print("Invalid input, try again\n")
        continue
 
    # random.choice() will randomly choose
    # item from list- options
    computer = random.choice(options)
    print("computer choose: ", computer)
 
    # Conditions based on the game rule
    if computer == 's':
        if player == 'x':
            comp_win = comp+1
        elif player == 'p':
            user_win = user+1
        else:
            comp_win = user_win
 
    elif computer == 'p':
        if player == 's':
            comp_win = comp+1
        elif player == 'x':
            user_win = user+1
        else:
            comp_win = user_win
 
    elif computer == 'x':
        if player == 'p':
            comp_win = comp+1
        elif player == 's':
            user_win = user+1
        else:
            comp_win = user_win
 
    # Announce winner of every round
    if user_win > comp_win:
        print(f"You Won round {rounds}\n")
    elif comp_win == user_win:
        print("Draw!!\n")
    else:
         print(f"Computer Won round {rounds}\n")

    #updating User And Comp Values     
    if user_win > comp_win:
        User=User+1
    else:
        Comp=Comp+1
    
 
    rounds += 1
 
 
# Final winner based on the number of wons
if User > Comp:
    print("Congratulations!! You Won")
elif Comp > User:
    print("ohh noo!...You lose!!")
elif Comp == User:
    print("Match Draw!!")
