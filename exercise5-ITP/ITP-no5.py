def kmer (DNA , k:int):
    database = {}
    for index in range(len(DNA)):
        stop1 = k+index
        print("stop > ", stop1)
        print("len dna ->", len(DNA))
        if stop1-1 < len(DNA):
            text = DNA[0 + index:stop1]
            database.setdefault(index + 1, 0)
            database[index+1] = text

    return database

if __name__ == '__main__':
    DNAstructure = input("input DNA Structure >>> ")
    kmercount = int(input("input k-mer count >>> "))
    print(kmer(DNAstructure, kmercount))