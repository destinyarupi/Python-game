import random

choice = ["R", "P", "S"]
choices = {
    "R": "ROCK",
    "P": "PAPER",
    "S": "SCISSORS"
}

print('"R" for ROCK \n"P" for paper \n"S" for scissors \npick an option:')

while True:
    player_choice = str(input()).upper()
    ai_choice = random.choices(choice)

    if not player_choice in choice:
        print('Invalid selection')
        continue

    print(f"Player({choices[player_choice]}) : CPU({choices[ai_choice[0]]}) ")

    if player_choice == ai_choice[0]:
        print("DRAW")
        continue
    elif player_choice == 'R' and ai_choice[0] == 'S':
        print("You Wins")
        break
    elif player_choice == 'S' and ai_choice[0] == 'P':
        print("You Wins")
        break
    elif player_choice == 'P' and ai_choice[0] == 'R':
        print("You Wins")
        break
    else:
        print("You Lose")
        break
