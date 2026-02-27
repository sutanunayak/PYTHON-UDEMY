masala_spices = ('cardimum','cloves', 'cinnamon')

(spice1, spice2, spice3) = masala_spices

print(f"Main masala spices: {spice1}, {spice2}, {spice3}")

ginger_ratio, cardimum_ratio = 2 , 3
print(f"Ratio is for the G :{ginger_ratio} and C : {cardimum_ratio}")
ginger_ratio, cardimum_ratio = cardimum_ratio, ginger_ratio
print(f"After swapping the ratio is for the G :{ginger_ratio} and C : {cardimum_ratio}") # Swiping values

# membership

print(f"Is ginger in masala spices ? {'cinnamon' in masala_spices}")