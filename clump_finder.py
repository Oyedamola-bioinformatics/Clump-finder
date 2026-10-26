# Code 4 - Find ALL Clumps
dna = "ATGCGACTATAGCTACTATACGATACGATACGATATATATACGATACGA"
k = 3
L = 20
t = 3

def find_clumps(dna, k, L, t):
    clumps = []
    for i in range(len(dna) - L + 1):
        window = dna[i:i+L]
        kmers = {}
        for j in range(len(window) - k + 1):
            kmer = window[j:j+k]
            kmers[kmer] = kmers.get(kmer, 0) + 1
        for kmer, count in kmers.items():
            if count >= t and kmer not in clumps:
                clumps.append(kmer)
    return clumps

print("DNA:", dna)
print("Clumps found:", find_clumps(dna, k, L, t))
print("These are the clumps that show the Origin of Replication")
