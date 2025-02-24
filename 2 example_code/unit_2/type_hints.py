# Without type hints - unclear what kind of numbers to use
def add_bonus_points(score, bonus):
    return score + bonus

# With type hints - now we know to use whole numbers
def add_bonus_points_typed(score: int, bonus: int) -> int:
    return score + bonus

# Using the function
player_score = 100
bonus_points = 50.89089

result = add_bonus_points_typed(player_score, bonus_points)
print("Final score:", result)

# This would give us a warning in our editor because it's the wrong type
text_score = "100"  # string instead of integer
#result = add_bonus_points_typed(text_score, bonus_points)