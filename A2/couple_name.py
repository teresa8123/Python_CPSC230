#Teresa Wong
#002407574
#tewong@chapman.edu
#FA21S-CPSC230-07
#Programming assignment 2 - couple_name.py

def first_split(name_1):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    # Find first consonant and include everything up to and including it
    for i in range(len(name_1)):
        if name_1[i].lower() in consonants:
            return name_1[0:i+1]  # Include the consonant
    return name_1  # If no consonant found, return whole name

def second_split(name_2):
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    
    if name_2[0].lower() in vowels:
        return name_2  # Return whole name if starts with vowel
    else:
        # Find first consonant after the first letter
        for i in range(1, len(name_2)):
            if name_2[i].lower() in consonants:
                return name_2[i+1:]  # Return everything after that consonant
        return name_2[1:]  # If no consonant, return everything after first letter

def couple_name(x, y):
    return first_split(x) + second_split(y)

name_1 = input("What is the first name, capitalize the first letter: ")
name_2 = input("What is the second name, do not use any capitalization: ")
print(couple_name(name_1, name_2))