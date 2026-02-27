cup = input("Choose you cup size (small/medium/large) : ").lower()

if cup == "small":
    print("Price is 10 Rs")
elif cup == "medium":
    print("Price is 15 Rs")
elif cup == "large":
    print("Price is 20 Rs")
else:
    print("Unknown cup size")