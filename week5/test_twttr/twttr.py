def main():

    txt = input("Input: ")
    output = shorten(txt)
    #print()
    print(f"Output: {output}")


def shorten(word):
    vwls = ["a", "e", "i", "o", "u","A", "E", "I", "O", "U"]
    shorts = []
    for l in word:
        if l not in vwls:
            shorts.append(l)
    output = str("".join(shorts))
    return output



if __name__ == "__main__":
    main()
