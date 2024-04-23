txt = input("Input: ")
vwls = ["a", "e", "i", "o", "u","A", "E", "I", "O", "U"]
output = print("Output: ", end="")

for t in txt:
    if t not in vwls:
        print(t, end="")

print()


######or

def main():

    coco = str(input("Input: ").strip())
    print("Output:", output(coco))


def output(fofo):
    vowels = ["i", "o", "a", "e", "u", "A", "E", "I", "U", "O"]
    for f in fofo:
        if f in vowels:
            fofo = fofo.replace(f, "")
    return fofo


if __name__ == "__main__":
    main()

