names = ["Sutanu", "Punit", "Lisure", "Sam"]
bills = [60, 40, 100, 80]

for name, amount in zip(names, bills):
    print(f"{name} paid {amount} rupees")