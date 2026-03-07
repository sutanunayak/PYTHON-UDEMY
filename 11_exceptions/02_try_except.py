Chai_menu = {"masala": 30, "ginger": 40}

try:
    Chai_menu["elaichi"]
except KeyError:
    print("The key that you are trying to access does not exists")

print("Hello chai code")