def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if  len(s) < 2 or len(s) > 6:
        return False
    elif not s[0].isalpha() or not s[1].isalpha():
        return False
    elif checkFirstZero(s):
        return False
    elif checkMiddleZero(s):
        return False
    elif last(s):
        return False
    elif worng(s):
        return False
    return True

def last(s):
    isAlp = False
    isNum = False
    for w in s:
        if not w.isalpha():
            isNum = True
        else:
            if isNum:
                return True
    return False

def checkCuntuNNumber(s):
    isFirstTry = True
    isNum = False
    for w in s:
        if not w.isalpha():
            if isFirstTry:
                isNum = True
                isFirstTry = False
    if isNum and s[-1].isalpha():
        return True


def checkMiddleZero(s):
    isFirstTry = True
    isNum = False
    for w in s:
        if not w.isalpha():
            if isFirstTry:
                isNum = True
                isFirstTry = False
    if isNum and s[-1].isalpha():
        return True
    else:
        return False

def checkFirstZero(s):
    for w in s:
        if not w.isalpha():
            if int(w) == 0:
                return True
            else:
                return False

def worng(s):
    for w in s:
        if w in [" ", ".", ","]:
            return True
    return False


main()
