def main():
    while True:
        try:
            f = input("Fraction: ")
            x = convert(f)
        except (ValueError, ZeroDivisionError):
            pass
        else:
            break
    p = gauge(x)
    print(f"{p}")


def convert(fraction):
    x, y = fraction.split("/")
    if int(y) == 0: 
        raise ZeroDivisionError
    elif x.isdigit() is False or y.isdigit() is False:
        raise ValueError
    elif int(x) > int(y):
        raise ValueError
    else:
        return round(int(x) / int(y) * 100)


def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()

