# Rock paper scissors
# List of valid moves
moves = ["rock", "paper", "scissors"]

# Initialize scores
player_score = 0
computer_score = 0

# Import random for computer moves
import random

print("Welcome to Rock Paper Scissors Tournament!")
print("Valid moves are:", moves)

# Main game loop
while player_score < 3 and computer_score < 3:
    # Track round number
    current_round = player_score + computer_score + 1
    print(f"\nRound {current_round}")
    
    # Get player move
    player_move = input("Your move: ").lower()
    
    # Check for quit
    if player_move == "quit":
        print("Thanks for playing!")
        break
        
    # Validate player move
    if player_move not in moves:
        print("Invalid move! Please try again.")
        continue
    
    # Get computer move
    computer_move = moves[random.randint(0, 2)]
    print(f"Computer chose: {computer_move}")
    
    # Determine winner
    if player_move == computer_move:
        print("It's a tie! No points awarded.")
    elif ((player_move == "rock" and computer_move == "scissors") or
          (player_move == "paper" and computer_move == "rock") or
          (player_move == "scissors" and computer_move == "paper")):
        print("You win this round!")
        player_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1
    
    print(f"Score - You: {player_score}, Computer: {computer_score}")

# Announce tournament winner
if player_score > computer_score:
    print("\nCongratulations! You won the tournament!")
elif computer_score > player_score:
    print("\nThe computer won the tournament!")
print(f"Final Score - You: {player_score}, Computer: {computer_score}")

#madlibs

# Lists to store word types needed
nouns = ["NOUN", "NOUN", "NOUN", "NOUN"]
verbs = ["VERB", "VERB", "VERB"]
adjectives = ["ADJECTIVE", "ADJECTIVE", "ADJECTIVE"]

# List to store collected words
player_words = []

print("Welcome to Adventure Mad Libs!")
print("I'll ask you for words to create a funny story.")

# Collect nouns
print("\nFirst, I need some nouns...")
for i in range(len(nouns)):
    word = input(f"Enter noun {i + 1}: ")
    player_words.append(word)

# Collect verbs
print("\nNow some verbs (action words)...")
for i in range(len(verbs)):
    word = input(f"Enter verb {i + 1}: ")
    player_words.append(word)

# Collect adjectives
print("\nFinally, some adjectives (describing words)...")
for i in range(len(adjectives)):
    word = input(f"Enter adjective {i + 1}: ")
    player_words.append(word)

# Create the story (note the multi-line f-string)
story = f""" 
Once upon a time, there was a {player_words[7]} {player_words[0]} who loved to {player_words[4]}.
One day, while {player_words[5]} through the {player_words[8]} forest,
the {player_words[0]} found a {player_words[1]} and a {player_words[2]}.

Suddenly, a {player_words[9]} {player_words[3]} appeared and started to {player_words[6]}!
The brave {player_words[0]} knew exactly what to do.

The End.
"""

print("\nHere's your story:")
print(story)
