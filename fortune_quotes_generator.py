
import random

fortunes = [
    "Something good is coming your way!",
    "Today is a good day to start something new.",
    "Real change, enduring change, happens one step at a time.",
    "Life is 10% what happens to me and 90% how I react to it.",
    "Nothing is impossible. The word itself says 'I'm possible!",
    "Spread love everywhere you go."
    "Just don't give up trying to do what you really want to do. Where there is love and inspiration, I don't think you can go wrong.",

]

print("================================")
print("       FORTUNE ME!")
print("================================")

input("Press Enter to reveal your fortune...")

fortune = random.choice(fortunes)

print("\nYour fortune for today is:")
print(fortune)
print("\nHave a wonderful day!")
