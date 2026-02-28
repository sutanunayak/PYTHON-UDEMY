# value = 17
# remainder = value % 5

# if remainder:
#     print(f"Not divisible, remainder is {remainder}")


# value = 17

# if (remainder := value % 5):
#     print(f"Not divisible, remainder is {remainder}")


# available_sizes = ["small", "medium", "large"]

# if (requisted_size := input("Enter your chai cup size: ").lower()) in available_sizes:
#     print(f"Serving {requisted_size} chai")
# else:
#     print(f"Size is not available")


flavors = ["masala", "ginger", "lemon", "mint"]

print("Available flavors: ", flavors)

while (flavor := input("Choose your flavor: ").lower()) not in flavors:
    print(f"Sorry, {flavor} is not available")

print(f"You choose {flavor} chai")