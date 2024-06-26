# [https://github.com/aniketrepo/python-feature-set/blob/main/com/Anike/stuff/Treasure%20Island.png] used for reference

input("Welcome to Treasure Island.")
input("Your mission is to find the treasure.")
input("You reach on the shore of the treasure island. It's big and spooky. You have a forest in front of you.")
print("Your proceed into the forest. Soon, you come to a standstill.")
input("There are two paths in front of you, left and right.")
choice1 = input("Do you choose to go right(R) or left(L): ")
if choice1 == "L":
    input("You walk down the left path for a while. You hear some noises in the bushes around you but you proceed to ignore them.")
    input("Soon, you come across a giant lake.")
    choice2 = input("You have two choices, swim(S) across the lake or wait(W). What do you choose: ")
    if choice2 == "W":
        input("Suddenly, you see the water surface rising.")
        input("A big tower emerges in front of you.")
        input("You enter the tower.")
        print("You start climbing the tower.")
        input("You've reached at the top of the tower and now there are three doors in front of you.")
        print("A red door.")
        print("A blue door.")
        print("A yellow door.")
        choice3 = input("You have to open a door, which door do you choose, red(R), blue(B) or yellow(Y): ")
        if choice3 == "R":
            input("You open the red door and proceed through a dark hallway into an empty room.")
            input("You look around the room to find something, but you fail as the room is too dark.")
            print("Suddenly, the wooden floor above the room breaks and the room is engulfed in flames in the blink of an eye.")
            print("You scream for your life but alas no one can hear you as you are alone on that island (probably).")
            input("You burn to your death, GAME OVER.")
        elif choice1 == "B":
            input("You open the blue door and proceed through a dark hallway into a dimly lit room.")
            print("Just as you enter the room you are greeted by 500 trolls who look hungry for human flesh. They feast on your body as your screams surround the entire tower.")
            print("Oh boy, GAME OVER.")
        elif choice3 == "Y":
            input("You open the yellow door and proceed through a dark hallway into a dimly lit room.")
            input("You find a lever on the floor.")
            print("You pull the lever and suddenly the ceiling breaks and a huge pile of gold coins along with a treasure chest falls down and nearly misses you.")
            input("Its the treasure that you've been looking for the entire time.")
            print("CONGRATULATIONS YOU WON THE GAME!")
        else:
            print("You chose something which doesn't even exist.")
            print("There's a special place in hell for people like you.")
            print("GAME OVER.")
    else:
        print("You proceed to swim through the unknown waters of the lake and suddenly something grabs your leg")
        input("You try to swim away but the thing pulls you down into the water.")
        input("You get a good look at what held your leg before dying.")
        input("Its a trout.")
        print("GAME OVER")
else:
    input("You start to walk down the right path")
    input("As you're walking, you suddenly fall into a really deep hole.")
    print("You fall on your head.")
    print("Instant death.")
    input("GAME OVER")
