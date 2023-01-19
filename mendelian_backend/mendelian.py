import random

class Gene:

    def __init__(self, a, g):
        self.character = a
        assert type(a) == str and len(a) == 1
        self.allele = [a.lower(), a.upper()]

        assert type(g) == list and len(g) == 2
        self.genotype = g

        self.a1 = self.allele[self.genotype[0]]
        self.a2 = self.allele[self.genotype[1]]

        self.alleles = [self.a1, self.a2]

        self.j = f"{self.a1}{self.a2}"


class Organism:

    def __init__(self, name, genes):
        self.name = name
        self.genes = genes

    def breed(self, mate):
        assert type(mate) == Organism

        mgenes = mate.genes

        gene_pairs = list(zip(self.genes, mgenes))

        new_genes = []
        for gp in gene_pairs:
            sa = random.choice(gp[0].genotype)
            ma = random.choice(gp[1].genotype)

            new_gene = Gene(gp[0].character, [sa, ma])
            new_genes.append(new_gene)
        
        product = Organism(f"Child-{self.name}-{mate.name}", new_genes)

        return product


if __name__ == "__main__":
    gene = Gene('a', [1, 0])
    
    m = Organism("bob", [gene])
    f = Organism("sarah", [gene])

    res = m.breed(f)

    print(res.genes[0].genotype)