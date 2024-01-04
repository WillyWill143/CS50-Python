import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    matches = re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip)
    if matches:
        if all(0 <= int(matches.group(i)) <= 255 for i in range(1,5)):
            return True
        else:
            return False

    else:
        return False




if __name__ == "__main__":
    main()
