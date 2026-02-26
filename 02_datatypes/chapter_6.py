chai_type  = "Ginger chai"
customer_name = "John Doe"

print(f"Order for {customer_name} : {chai_type} please !")

chai_description = "Aromatic and spicy ginger chai"
print(f"First word: {chai_description[:8]}")
print(f"First word: {chai_description[10:]}")
print(f"First word: {chai_description[::-1]}") # Reverse string

label_text = "Chai Spêcial"
encoded_label = label_text.encode("utf-8")
print(f"Encoded label : {encoded_label}")
print(f"Non Encoded label : {label_text}")  # Proper way to Encode & Decode
decoded_label = encoded_label.decode("utf-8")
print(f"Decoded label : {decoded_label}")