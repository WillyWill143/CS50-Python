def ein():
    mass = int(input("Enter mass value: "))
    return print(mass * pow(300000000, 2))

ein()


#or 
def main():
    prompt = int(input("m: "))
    print("E:", calc(prompt))

def calc(n):
    E = n * (300000000**2)
    return E


main()
