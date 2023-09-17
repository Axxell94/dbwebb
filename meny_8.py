#!/usr/bin/env python

# Menyval 8: Gör så Marvin kan tala rövarspråket.
# Marvin ska använda ett input anrop för att ta emot ett ord och sen skriva ut ordet översatt till rövarspråket.
# Exempel: "b" blir "bob" och "Hans" blir "hohanonsos"

# Problemet = C0200: Consider using enumerate instead of iterating with range and len (consider-using-enumerate)

CONSONANTS = "bcdfghjklmnpqrstvwxz"

word = input("Type: ")
word = word.lower()
rov = ""

for letter in word:
    if letter in CONSONANTS:
        rov = rov + letter + "o" + letter
    else:
        rov = rov + letter

print(f"Translated word: {rov}")
