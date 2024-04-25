def main():
    c = get_perc("Fraction: ")
    print(c)

def get_perc(prompt):
    while True:
        try:
            x, y = input(prompt).split("/")
            if 0 <= int(x)/int(y) <= 0.1:
                return("E")
            elif 0.9 <= int(x)/int(y) <= 1:
                return("F")
            elif 0.1 < int(x)/int(y) < 0.9:
                return str(round(int(x)/int(y)*100)) + "%"
        except (ValueError, ZeroDivisionError):
            pass



main()


####or

def main():
    c = get_perc("Fraction: ")
    print(c)

def get_perc(prompt):
    while True:
        try:
            a, b = input(prompt).split("/")
            a = int(a)
            b = int(b)
            d = round((a / b) * 100)
            if 100 >= d >= 99:
                d = "F"
                return d
            elif d <= 1:
                d = "E"
                return d
            elif d > 100:
                pass
            else:
                return str(int(d)) + "%"
        except (ValueError, ZeroDivisionError):
            pass
main()
