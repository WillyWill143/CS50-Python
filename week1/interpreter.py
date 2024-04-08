maths = input("Expression: ").strip()

x, y, z = maths.split(" ")

x = float(x)
z = float(z)

if y == "+":
    results = x + z
    print(results)
elif y == "-":
    results = x - z
    print(results)
elif y == "*":
    results = x * z
    print(results)
elif y == "/":
    results = x / z
    print(results)


##or

def main():
    a, b, c = input("Expression: ").split(" ")
    cucu(a, b, c)

def cucu(x, y, z):

    if y == "+":
        print(float(x) + float(z))

    elif y == "-":
        print(float(x) - float(z))

    elif y == "*":
        print(float(x) * float(z))

    else:
        print(float(x) / float(z))

main()
