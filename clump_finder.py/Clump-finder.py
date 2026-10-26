# Code 4 - Find ALL Clumps
dna = "ATGCGACTATAGCTACTATACGATACTATAGCTACTATACGAT"

print("DNA length:", len(dna))
print("Searching for all 5-mers that appear 3 or more times...")
print("")

found = []

for i in range(len(dna)-4):
    pattern = dna[i:i+5]
    count = dna.count(pattern)
    
    if count >= 3 and pattern not in found:
        found.append(pattern)
        print(pattern, "appears", count, "times - CLUMP FOUND!")

print("")
print("Total clumps found:", len(found))
print("Clumps:", found)
