# Exercise 1 Text Cleaner

import re

def clean_text(text):
    # Remove pounctuations
    text = re.sub(r"[^\w\s]", "", text)
    # Remove extra spaces
    text = "".join(text.split())
    #convert to  lowecase
    return text.lower()

input_text = "Hello , World.!!!  Welcome to Python, programming "
cleaned_text = clean_text(input_text)
print(cleaned_text)