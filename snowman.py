import random

def main():
    difficulty = int(input("What difficulty do you want to play? \neasy: 1, medium: 2, hard: 3\n"))
    
    word = random_word(difficulty).lower()
    length = len(word) - 1
    display = []

    print(word)

    for i in range(length):
        display.append('-')
    print(display)
    print()

    incorrect_guesses = 6

    while incorrect_guesses != 6:
        break

    print_snowman(incorrect_guesses)



def random_word(difficulty):
    dictionary = open("dictionary.txt", "r")
    
    if difficulty == 1:
        word = dictionary.readlines()[random.randint(0, 539)]
    
    elif difficulty == 2:
        word = dictionary.readlines()[random.randint(540, 841)]

    elif difficulty == 3:
        word = dictionary.readlines()[random.randint(842, 851)]

    else:
        print("Please choose a valid difficulty")

    dictionary.close()

    return word

def print_snowman(incorrect_guesses):
    if incorrect_guesses == 0:
        return
    elif incorrect_guesses == 1:
        print("(       )\n '_____'")
    elif incorrect_guesses == 2:
        print(" (     )\n(       )\n '-----'")
    elif incorrect_guesses == 3:
        print("  (   )\n (     )\n(       )\n '-----'")
    elif incorrect_guesses == 4:
        print("  ('v')\n (     )\n(       )\n '-----'")
    elif incorrect_guesses == 5:
        print("    ('v')\n--<(  .  )>--\n  (   .   )\n   '-----'")
    elif incorrect_guesses == 6:
        print("     ___\n   _|___|_\n    ('v')\n--<(  .  )>--\n  (   .   )\n   '-----'") #Game over

main()
