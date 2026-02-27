essention_spices = {"cardamom", "ginger", "cinnamon"}
optional_spices = {"clove", "nutmeg", "ginger"}

all_spices = essention_spices | optional_spices
print(f"All spices: {all_spices}")

commom_spices = essention_spices & optional_spices
print(f"Common spices: {commom_spices}")

only_in_essential = essention_spices - optional_spices
print(f"Only in essential: {only_in_essential}")

print(f"Is 'clove' in essential spices? {'clove' in essention_spices}")
