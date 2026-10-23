
import random

fortunes = [
    "Something good is coming your way!",
    "Today is a good day to start something new.",
    "Real change, enduring change, happens one step at a time.",
    "Life is 10% what happens to me and 90% how I react to it.",
    "Spread love everywhere you go.",
    "Wake up determined, go to bed satisfied.",
    "Your intuition will guide you through a tricky situation today.",
    "An unexpected acquaintance will soon bring you great joy.",
    "Do not fear extra room in your life; it is space for better things to come.",
    "Your kindness is a bank account that never runs out of interest.",
    "Building a culture that deeply values people doesn’t preclude holding them to high standards.",
]

colors = [
    "Purple",
    "Blue",
    "Pink",
    "Green",
    "Yellow",
    "Red",
    "Brown",
    "Black",
    "White",
    "Orange",
    "Gray",
    "Turquoise",
    "Silver",
    "Gold",
]


print("================================")
print("           FORTUNE ME!")
print("================================")

for attempt in range(3):
    input("\nPress Enter to reveal your fortune...")

    fortune = random.choice(fortunes)
    color = random.choice(colors)

    print("\nYour fortune and color is:", fortune)
    print("Your lucky color is:", color)

    print(f"\nFortune {attempt + 1} of 3")
    

print("\nThat was your 3 fortunes for today!")
print("Have a wonderful day!")
