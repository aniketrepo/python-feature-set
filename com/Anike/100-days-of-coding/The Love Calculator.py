print("Welcome to the love calculator!")
name1 = input("Please enter name 1: ")
name2 = input("Please enter name 2: ")
print("The love calculator is calculating your score...")

combined_names = name1 + name2
lowercase_names = combined_names.lower()

# for TRUE
t = lowercase_names.count("t")
r = lowercase_names.count("r")
u = lowercase_names.count("u")
e = lowercase_names.count("e")
first_digit = t + r + u + e

# for LOVE
l = lowercase_names.count("l")
o = lowercase_names.count("o")
v = lowercase_names.count("v")
e = lowercase_names.count("e")
second_digit = l + o + v + e

love_score = int(str(first_digit) + str(second_digit))
if (love_score < 10) or (love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
