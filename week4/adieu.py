import inflect

p = inflect.engine()

names_list = []

while True:
    try:
        name = input("Name: ")
        names_list.append(name)
    except EOFError:
        print()
        break
#I had many bugs in this code, wherein i ran it manually and it worked fine but
#the check50 didnt accept it and turns out the problem is that the output was part of the loop so i removed it 
output = p.join(names_list)
print("Adieu, adieu, to " + output)

