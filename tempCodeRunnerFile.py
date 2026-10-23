
import random

fortunes = [
    "Something good is coming your way!",
    "Today is a good day to start something new.",
]

print("================================")
print("       FORTUNE ME!")
print("================================")

input("Press Enter to reveal your fortune...")

fortune = random.choice(fortunes)

print("\nYour fortune for today is:")
print(fortune)
print("\nHave a wonderful day!")
