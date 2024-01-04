from validator_collection import checkers

e = input("What's your email address? ")

if checkers.is_email(e):
    print("valid")
else:
    print("invalid")
