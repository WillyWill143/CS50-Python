z  = input("What is the answer to the Great Queation of Life, the Universe, and Everything? ").lower().strip()

if z in ["42", "forty-two", "forty two"]:
    print("yes")
else:
    print("No")


##or

def main():
    answer = input("What is the answer to the Great Question of Life, the Universe and Everything? ").lower().strip()
    fort(answer)

def fort(z):
    if z == "42" or z == "forty two" or z == "forty-two":
        print("Yes")
    else:
        print("No")



main()
