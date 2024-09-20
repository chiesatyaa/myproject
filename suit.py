import random

listGame = ['Scissors', 'Rock', 'Papper', 'sciossors', 'papper', 'rock']
userInput = input('What you would be choose?  Scissors, Rock, or  Paper?: ')

computer_random_choices = random.choice(listGame)

if ((userInput == 'Scissors') or (userInput == 'scissors')) and  ((computer_random_choices == 'Scissors') or (computer_random_choices == 'scissors')):
    print(f'User choose {userInput} and Computer choose {computer_random_choices}, the result is Draw')
    if ((userInput == 'Scissors') == (userInput == 'scissors')) and  ((computer_random_choices == 'Rock') or (computer_random_choices == 'rock')):
        print(f'User choose {userInput} and Computer choose {computer_random_choices}, the result is Lose')
        if  ((userInput == 'Scissors') == (userInput == 'scissors')) and  ((computer_random_choices == 'Papper') or (computer_random_choices == 'papper')):
            print(f'User choose {userInput} and Computer choose {computer_random_choices}, the result is Win')
        else:
            print('Wrong Input')
elif ((userInput == 'Rock') == (userInput == 'rock')) and (computer_random_choices == 'Rock' or (computer_random_choices == 'rock')):
    print(f'User choose {userInput} and Computer choose {computer_random_choices}, the result is Draw')
    if ((userInput == 'Rock') == (userInput == 'rock')) and   (computer_random_choices == 'Paper' or (computer_random_choices == 'papper')):
        print(f'User choose {userInput} and Computer choose {computer_random_choices}, the result is Lose')
        if  ((userInput == 'Rock') == (userInput == 'rock')) and  (computer_random_choices == 'Scissors' or (computer_random_choices == 'scissors')):
            print(f'User choose {userInput} and Computer choose {computer_random_choices}, the result is Win')
        else:
            print('Wrong Input')
elif ((userInput == 'Paper') == (userInput == 'paper')) and  (computer_random_choices == 'Paper')  or (computer_random_choices == 'paper'):
    print(f'User choose {userInput} and Computer choose {computer_random_choices}, the result is Draw')
    if ((userInput == 'Paper') == (userInput == 'paper')) and  (computer_random_choices == 'Scissors'  or (computer_random_choices == 'scissors')):

        print(f'User choose {userInput} and Computer choose {computer_random_choices}, the result is Lose')
        if  ((userInput == 'Paper') == (userInput == 'paper')) and  (computer_random_choices == 'Rock' or (computer_random_choices == 'rock')):
            print(f'User choose {userInput} and Computer choose {computer_random_choices}, the result is Win')
        else:
            print('Wrong Input')
