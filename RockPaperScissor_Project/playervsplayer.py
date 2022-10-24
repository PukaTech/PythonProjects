#plan for Player vs player game

# ask each players name and save it to the variables player1_name and player2_name

player1_name = str(input('what is your name: '))

player2_name = str(input('what is your name: '))


# take both players choice(rock or paper or scissor)
player1_choice = str(input('Choose one: Rock, Paper, Scissor ').lower())

player2_choice = str(input('Choose one: Rock, Paper, Scissor ').lower())


#Logic1 : check if both choices are the same like rock and rock
if(player1_choice == player2_choice):{
    print('it is a tie')
}


#Logic 2 : check if player1 chooses rock and compare it with if player2 chooses scissors then player 1 wins but if player2 chooses paper then player2 wins
elif(player1_choice == 'rock'):
    #player1 chose rock and compare it with if player2 chooses scissors then player 1 wins
    if(player2_choice == 'scissor' ):{
        print(f'{player1_name} wins')
    }
    #player1 chose rock and compare it with if player2 chooses paper then player 2 wins
    elif(player2_choice == 'paper'):{
        print(f'{player2_name} wins')
    }


#Logic 3 : check if player1 chooses scissors and compare it with if player2 chooses paper then player 1 wins but if player2 chooses scissors then player2 wins
elif(player1_choice == 'scissor'):
    #player1   chose scissors and compare it with if player2 paper scissors then player 1 wins
    if(player2_choice == 'paper'):{
        print(f'{player1_name} wins')
    }

    #player1 chose scissors and compare it with if player2 chooses rock then player 2 wins
    elif(player2_choice == 'rock'):{
        print(f'{player2_name} wins')
    }
    

#Logic 4: if players enter something different than rock paper scissors then print out the line below.

else:{
    print('Something went wrong')
}
