import random

while True:
    try:
        lvl = int(input("Level: "))
        n = random.randint(1, lvl)
        while True:
            guess = int(input("Guess: "))

            if guess > n:
                print("Too Large!")
            elif guess < n:
                print("Too small!")
            elif guess == n:
                print("Just right!")
                raise EOFError
    except ValueError:
        pass
    except EOFError:
        break
