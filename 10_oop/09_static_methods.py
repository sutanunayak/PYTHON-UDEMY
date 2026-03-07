class ChaiUtils:

    def clean_ingredients(text):
        return [item.strip() for item in text.split(",")]
    

raw = " water  , milk , ginger , honey"


cleaned = ChaiUtils.clean_ingredients(raw)
print(f"cleaned format {cleaned}")