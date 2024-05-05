import sys

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        if sys.argv[1][-3:] != ".py":
                sys.exit("Not a python file")
        else:
            print(count_line(sys.argv[1]))





def count_line(file):
    try:
        counter = 0
        with open(file, "r") as fil:
            for line in fil:
                if not (line.lstrip().startswith("#") or line.strip() == ""):
                    counter += 1
            return counter
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()



####or

import sys

def main():

    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif not sys.argv[1].endswith(".py"):
        sys.exit("Not a python file")
    else:
        print(count_lines(sys.argv[1]))

def count_lines(file):
    try:
        lines = []
        with open(file) as file:
            for line in file:
                if not (line.lstrip().startswith("#") or line.isspace()):
                    lines.append(line.strip())
    except FileNotFoundError:
        sys.exit("File does not exist")
    return len(lines)

if __name__ == "__main__":
    main()
