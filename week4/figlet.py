from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
arg1 = ["-f", "--font"]

def main():
    if len(sys.argv) < 2:
        font = random.choice(figlet.getFonts())
        figgin("Input: ", font)
    elif len(sys.argv) > 2 and sys.argv[1] in arg1 and sys.argv[2] in figlet.getFonts():
        font = sys.argv[2]
        figgin("Input: ", font)
    else:
        sys.exit("Invalid usage")

def figgin(prompt, f):
    txt = input(prompt)
    figlet.setFont(font=f)
    print("Output:")
    print(figlet.renderText(txt))


main()
