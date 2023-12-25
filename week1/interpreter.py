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
