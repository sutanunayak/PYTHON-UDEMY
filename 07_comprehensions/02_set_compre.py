favourite_chai = [
    "Masala Chai", "Green Tea", "Masala Chai",
    "Lemon Tea", "Green Tea", "Elaichi Chai"
]

unique_chai = {chai for chai in favourite_chai}
print(unique_chai)

receipes = {
    "Masala Chai": ["ginger", "cardmom", "clove"],
    "Elaichi Chai": ["Cardmom", "milk"],
    "Spicy Chai": ["ginger", "black papper", "clove"]
}


unique_spices = {spice for ingredients in receipes.values() for spice in ingredients}

print(unique_spices)