import random

def main():
    difficulty = int(input("What difficulty do you want to play? \neasy: 1, medium: 2, hard: 3\n"))
    
    dictionary = open("dictionary.txt", "r")
    
    if difficulty == 1:
        word = dictionary.readlines()[random.randint(0, 539)]
    
    elif difficulty == 2:
        word = dictionary.readlines()[random.randint(540, 841)]

    elif difficulty == 3:
        word = dictionary.readlines()[random.randint(842, 851)]

    else:
        print("Please choose a valid difficulty")
    
    print(word)

    dictionary.close()




main()
