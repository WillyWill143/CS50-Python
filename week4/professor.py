
import random
import sys

def main():
    level = get_level()


    score = 0

    for i in range(10):
        a = generate_integer(level)
        b = generate_integer(level)

        for j in range(3):
            ans = input(f"{a} + {b} =")
            if int(ans) == int(a + b):
                score += 1
                break
            else:
                print("EEE")
                if j == 2:
                    print(a+b)
            j += 1

        i += 1

    print(f"Score: {score}")
    sys.exit(0)

# Prompts the user for a level, n
# If the user does not input 1, 2, or 3, the program should prompt again.

# get_level prompts (and, if need be, re-prompts) the user for a level and returns 1, 2, or 3,
def get_level():
    while True:
        try:
            level = int(input())
            if level < 1 or level > 3:
                level = input()
            else:
                break
        except ValueError:
            level = input()
    return level


# generate_integer returns a randomly generated non-negative integer with level digits or raises a ValueError if level is not 1, 2, or 3
def generate_integer(level):
    if level == 1:
        y = random.randint(0, 9)
    elif level == 2:
        y = random.randint(10, 99)
    elif level == 3:
        y = random.randint(100, 999)
    else:
        raise ValueError

    return y


if __name__ == "__main__":
    main()
