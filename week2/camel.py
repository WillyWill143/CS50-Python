def main():
    camel = input("camelCase: ")
    convert(camel)
    print()

def convert(camel):
    print("snake_case: ", end="")
    for c in camel:
        if c.islower():
            print(c, end="")
        elif c.isupper():
            print("_", c.lower(), end="", sep="")

main()
