myName=input("Hello! What is your name?")
userNumber = input("Well, " + myName+ " ,I am thinking of a number between 1 and 10.")

shouting = ("Wrong, better luck next time.")

if userNumber == "3":
    print("Good job," + myName + "! You guessed my number!")
else:
    print("Wrong, better luck next time.")