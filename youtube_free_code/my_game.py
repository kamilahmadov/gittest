answer = "180"
guess = ""

while guess != answer:
    guess = int(input("Lets play the game where you guess my height: "))
    if guess >= 190:
        print("No, I am much shorter than your guess")
    elif guess > 180 and guess < 190:
        print("No, I am shorter but your guess is close")
    elif guess <= 170 and guess != 69:
        print("No, I am much taller than your guess")
    elif guess > 170 and guess < 180:
        print("No, I am taller but your guess is close")
    elif guess == 69:
        print("....... ▄▄ ▄▄")
        print("......▄▌▒▒▀▒▒▐▄")
        print(".... ▐▒▒▒▒▒▒▒▒▒▌")
        print("... ▐▒▒▒▒▒▒▒▒▒▒▒▌")
        print("....▐▒▒▒▒▒▒▒▒▒▒▒▌")
        print("....▐▀▄▄▄▄▄▄▄▄▄▀▌")
        print("....▐░░░░░░░░░░░▌")
        print("....▐░░░░░░░░░░░▌")
        print("....▐░░░░░░░░░░░▌")
        print("....▐░░░░░░░░░░░▌")
        print("....▐░░░░░░░░░░░▌")
        print("....▐░░░░░░░░░░░▌")
        print("....▐░░░░░░░░░░░▌")
        print("....▐░░░░░░░░░░░▌")
        print("....▐░░░░░░░░░░░▌")
        print("...▄█▓░░░░░░░░░▓█▄")
        print("..▄▀░░░░░░░░░░░░░ ▀▄")
        print(".▐░░░░░░░▀▄▒▄▀░░░░░░▌")
        print("▐░░░░░░░▒▒▐▒▒░░░░░░░▌")
        print("▐▒░░░░░▒▒▒▐▒▒▒░░░░░▒▌")
        print(".▀▄▒▒▒▒▒▄▀▒▀▄▒▒▒▒▒▄▀")
        print(".. ▀▀▀▀▀ ▀▀▀▀▀")
    else:
        print("The answer is correct!")