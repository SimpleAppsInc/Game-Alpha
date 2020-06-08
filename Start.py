from Game import Giris
print("Welcome to Story of an Life. \n To start")
name = input("Enter your name here: ")
print("Welcome " + name + "\n*Start game\n*Help\n*About\n*Exit")
answer = input("Your choice: ").lower()
if answer == "start game" or answer == "start":
    Giris()

