menu = [
    "Masala chai",
    "Iced Lemon Tea",
    "Green Tea",
    "Iced peach Tea",
    "Ginger Tea"
]


iced_tea = [tea for tea in menu if "Iced" in tea]
Iced_tea = [tea for tea in menu if len(tea) > 10]
print(Iced_tea)