def bearAndSteadyGene(gene):
    count = [gene.count(letter) for letter in letters]
    seek = []
    for i in range(0, 4):
        add = int(count[i]-n/4)
        if(add > 0):
            seek.append(letters[i])
    
    add = [int(gene.count(x)-n/4) for x in seek]
    for i in range(sum(add), len(gene)):
        for j in range(0, len(gene)):
            count = [gene[j:j+i].count(x) for x in seek]
            if(count == add):
                return i

letters = ['A','C','G','T']
n = int(input())
gene = input()
print(bearAndSteadyGene(gene))