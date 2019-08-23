import random
def hangman():
    x = input("Difficulty: ")
    x = str(x)
    num = random.randint(0, 24)
    allwords = ["dick", "balls", "pussy", "asshole", "fuckface", "spiderman", "ghostbusters", "dickhole", "pussylips", "rimjob", "lobster", "roastbeef", "sushi", "apple", "carnival", "guitar", "mansion", "television", "football", "quarterback", "airplane", "riffle", "shotgun", "sniper", "python"]
    easywords = ["dick", "balls", "cunt", "fuck", "butt", "cat", "dog", "bug", "rug", "shoe", "rent", "cars", "bus", "van", "red", "blue", "game", "lame", "tame", "rain", "egg", "baby", "bee", "weed", "coke"]
    medwords = ["asshole", "bastard", "fucker", "tickle", "skittle", "cocaine", "truck", "abusive", "medium", "marriage", "parents", "study", "blowjob", "rimjob", "partner", "coffee", "sneaker", "president", "bacon", "credit", "monkey", "runner", "remote", "riffle", "interest"]
    hardwords = ["maximize", "difficult", "universal", "cuntface", "dysentery", "cemetery", "cortex", "lesbian", "dictionary", "patriot", "equator", "minimize", "cappuccino", "espresso", "government", "kingdom", "centralize", "capitalize", "confidence", "acceptance", "adoption", "integration", "dumptruck", "welcoming", "programmer"]
    if x == "easy":
        word = easywords[num]
    elif x == "medium":
        word = medwords[num]
    elif x == "hard":
        word = hardwords[num]
    else:
        word = allwords[num]
    wrong = 0
    stages = ["",
              "_______       ",
              "|      |      ",
              "|      |      ",
              "|      0      ",
              "|     /|\     ",
              "|     / \     ",
              "|             "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter: "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "_" not in board:
              print("You win!")
              print(" ".join(board))
              win = True
              break
    if not win:
        print("\n".join(stages[0: wrong]))
        print("You lose! It was {}.".format(word))
        
              
