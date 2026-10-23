
import random

fortunes = [
    "Something good is coming your way!",
    "Today is a good day to start something new.",
    "Real change, enduring change, happens one step at a time.",
    "Life is 10% what happens to me and 90% how I react to it.",
    "Spread love everywhere you go.",
    "Wake up determined, go to bed satisfied.",
    "Just don't give up trying to do what you really want to do. Where there is love and inspiration, I don't think you can go wrong."
]

colors = [
    "Purple",
    "Blue",
    "Pink",
    "Green",
    "Yellow",
    "Red"
]


print("================================")
print("           FORTUNE ME!")
print("================================")

for attempt in range(3):
    input("\nPress Enter to reveal your fortune...")

    fortune = random.choice(fortunes)

    print("\nYour fortune and color is:")
    print(f"{fortune} and {color}")

    print(f"\nFortune {attempt + 1} of 3")

print("\nThat was your 3 fortunes for today!")
print("Have a wonderful day!")
