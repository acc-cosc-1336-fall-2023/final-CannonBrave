def get_most_likely_ancestor_consensus(dna_string1, dna_string2):
    positions = []
    for i in range(len(dna_string1) - len(dna_string2) + 1):
        if dna_string1[i:i+len(dna_string2)] == dna_string2:
            positions.append(i + 1)
    return positions

def main():
    while True:
        dna_string1 = input("Enter DNA string (8-16 characters): ")
        dna_string2 = input("Enter a DNA substring (exactly 4 characters): ")

        if not (8 <= len(dna_string1) <= 16) or len(dna_string2) != 4:
            print("Invalid input. Please try again.")
            continue

        positions = get_most_likely_ancestor_consensus(dna_string1, dna_string2)
        print("Positions:", " ".join(map(str, positions)))

        if input("Try again? Enter yes or no: ") != "yes":
            break
