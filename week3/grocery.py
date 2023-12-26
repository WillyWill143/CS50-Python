bag = {}

while True:
    try:
        item = input().upper().strip()
        if item not in bag:
            bag[item] = 1
        else:
            bag[item] = bag[item] + 1

    except EOFError:
        sortD = dict(sorted(list(bag.items())))
        for item in sortD:
            print(sortD[item], item, sep=" ")
        break
    except KeyError:
        pass
