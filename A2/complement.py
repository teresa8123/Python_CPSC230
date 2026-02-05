#Teresa Wong
#002407574
#tewong@chapman.edu
#FA21S-CPSC230-07
#Programming assignment 2 - complement.py

def check_string(dna_str):
    nucleotides = ['A','C','T','G']
    for letter in dna_str:
        if letter not in nucleotides:
            return False
    return True

def complement(DNA_seq):
    sequence = ''
    for letter in DNA_seq:
        if letter == 'A':
            sequence += 'T'  # A pairs with T
        elif letter == 'T':
            sequence += 'A'  # T pairs with A
        elif letter == 'C':
            sequence += 'G'  # C pairs with G
        elif letter == 'G':
            sequence += 'C'  # G pairs with C
    return sequence

def reverse(sequence):
    return sequence[::-1]

def reverse_complement(sequence):
    comp = complement(sequence)  # Get complement first
    rev_comp = reverse(comp)      # Then reverse the complement
    return rev_comp

#asking user to input their DNA sequence
sequence_string = input("What is the DNA sequence: ")

#making sure the DNA sequence is valid
while check_string(sequence_string) != True:
    sequence_string = input("Your sequence is invalid, try again: ")

#print results
print("The DNA sequence you entered is", sequence_string)
print("The complement of your sequence is", complement(sequence_string))
print("The reverse complement of your sequence is", reverse_complement(sequence_string))