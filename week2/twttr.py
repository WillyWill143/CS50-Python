txt = input("Input: ")
vwls = ["a", "e", "i", "o", "u","A", "E", "I", "O", "U"]
output = print("Output: ", end="")

for t in txt:
    if t not in vwls:
        print(t, end="")

print()
