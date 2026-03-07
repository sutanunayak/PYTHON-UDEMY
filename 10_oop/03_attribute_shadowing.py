class Chai:
    temperature = "hot"
    strength = "Strong"


cutting = Chai()
print(cutting.temperature)

cutting.temperature = "mild"
cutting.cup = "small"
print(f"After changing {cutting.temperature}")
print("Cup size is ", cutting.cup)
print("Direct look into the class ", Chai.temperature)

del cutting.temperature
del cutting.cup
print("After deleting the attribute from object ", cutting.cup)
print(cutting.temperature)