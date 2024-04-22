import random

input("Press enter to toss the coin.")
num = random.randint(0, 1)
if num == 1:
    print("Heads")
else:
    print("Tails")
