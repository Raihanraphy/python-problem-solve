import random

dice = {
    1: "⚀", 2: "⚁", 3: "⚂",
    4: "⚃", 5: "⚄", 6: "⚅"
}

roll = random.randint(1, 6)
print("You rolled:", dice[roll])
