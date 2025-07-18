# TODO
import math
from cs50 import get_string

# Prompt Text:
text = get_string("Text: ")

# Count the number of upper and lowercase letters
letters = sum(1 for char in text if char.isalpha())

# Count the number of words
words = len(text.split())

# Count the number of sentences
sentences = sum(1 for char in text if char in ['.', '!', '?'])

# Calculate the floating points
L = (letters / words) * 100.00
S = (sentences / words) * 100.00
subindex = 0.0588 * L - 0.296 * S - 15.8

index = round(subindex)

if index > 16:
    print("Grade 16+")
elif index < 1:
    print("Before Grade 1")
else:
    print(f"Grade {index}")
