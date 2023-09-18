#!/usr/bin/env python
# pylint: disable=line-too-long
# pylint: disable=missing-module-docstring

# Menyval 7: Gör så att Marvin kan validera personnummer med hjälp av Luhnalgoritmen.
# Algoritmen funkar på så sätt att varannan siffra multipliceras med 2 och 1, med start på första siffran i personnumret.
# Om något tal vid multiplikationen blir större än 9 ersätts det talet med dess siffersumma.
# Därefter summeras alla tal och om summan är jämt delbar med 10 så är kontrollsiffran korrekt.
# Om personnumret validerar ska Marvin skriva ut Valid annars Not valid. Koden ska klara av personnummer med och utan - innan de fyra sista siffrorna.


def valid_person(personnummer: int) -> bool:
    """
    Accept a string of 10 numbers and check if it is a valid personnummer.
    Use the Luhn Algorithm to check if the personnummer is valid.
    Luhn Algorithm works by multiplying every other number by 2, starting with the last number
    If any number is greater than 9, add the two numbers together
    and then adding the sum of the digits and doing mod 10
    """

    try:
        personnummer = personnummer[::-1]
        personnummer = [int(x) for x in personnummer]

        for i in range(1, len(personnummer), 2):
            personnummer[i] *= 2
            if personnummer[i] > 9:
                personnummer[i] = personnummer[i] % 10 + 1

        total = sum(personnummer)
        if total % 10 == 0:
            return True

        return False

    except ValueError:
        return False


user_input = input("Enter your social security number, 10 numbers: ")

# If personnummer is longer than 11 characters, it is not valid
if len(user_input) > 11:
    print("Personnummer is too long")
else:
        # Remove - from personnummer
    user_input = user_input.replace("-", "")

if valid_person(user_input):
    print("Valid")
else:
    print("Not valid")
