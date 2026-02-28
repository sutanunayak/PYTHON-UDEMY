flavours = ["Ginger", "Out of stock", "Lemon", "Discounted", "Mint"]

for flavour in flavours:
    if flavour == "Out of stock":
        continue
    if flavour == "Discounted":
        print(f"{flavour} item found")
        break
    print(f"{flavour} item found")

print(f"Out side of loop")