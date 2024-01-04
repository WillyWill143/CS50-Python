import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if y := re.search(r"^(1?\d)(:[0-5]\d)? (AM|PM) to (1?\d)(:[0-5]\d)? (AM|PM)$", s):
        if y.group(3) == "AM" and y.group(6) == "PM":
            if 0 < int(y.group(1)) < 13 and 0 < int(y.group(4)) < 13:
                p = y.group(2)
                q = y.group(5)
                if not p: p = ":00"
                if not q: q = ":00"
                if (y.group(1) and y.group(4)) == "12":
                    return f"00{p} to {y.group(4)}{q}"
                return f"{y.group(1).zfill(2)}{p} to {int(y.group(4))+12}{q}"
            pass
        elif y.group(3) == "PM" and y.group(6) == "AM":
            if 0 < int(y.group(1)) < 13 and 0 < int(y.group(4)) < 13:
                p = y.group(2)
                q = y.group(5)
                if not p: p = ":00"
                if not q: q = ":00"
                return f"{int(y.group(1))+12}{p} to {y.group(4).zfill(2)}{q}"
            pass
        raise ValueError("lol")
    else:
        raise ValueError("lol")


if __name__ == "__main__":
    main()
