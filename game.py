#Rock, Paper, Scissors
import random
choices=['rock','paper','scissors']
player = input("Your choices:").lower()
coumputer=random.choice(choices)

print(f"Computer: {coumputer}")

if player == coumputer:
    print("It's a tie!")
elif (player, coumputer) in [
    ('rock', 'scissors'),
    ('paper', 'rock'),
    ('scissors', 'paper'),
]:
    print("You win!")
else:
    print("You lose!")