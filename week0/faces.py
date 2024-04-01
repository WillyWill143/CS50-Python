def main():
    statement = input()
    print(convert(statement))

def convert(po):
    pot = po.replace(":)", "🙂").replace(":(", "🙁")
    return pot

main()
