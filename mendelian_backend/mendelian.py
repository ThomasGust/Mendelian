import random
import string

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

        self.ci_dict = {self.allele[0]:0, self.allele[1]:1}
        self.ic_dict = {0:self.allele[0], 1:self.allele[1]}


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
            assert gp[0].character == gp[1].character
            sa = random.choice(gp[0].genotype)
            ma = random.choice(gp[1].genotype)

            new_gene = Gene(gp[0].character, [sa, ma])
            new_genes.append(new_gene)
        
        product = Organism(f"Child-{self.name}-{mate.name}", new_genes)

        return product

class Environment:


    def __init__(self, species_name, genes=string.ascii_lowercase, population_size=100):
        self.species_name = species_name
        self.population_size = population_size



if __name__ == "__main__":
    mg1 = Gene('a', [1, 0])
    mg2 = Gene('b', [0, 0])

    fg1 = Gene('a', [1, 1])
    fg2 = Gene('b', [0, 1])
    
    m = Organism("bob", [mg1, mg2])
    f = Organism("sarah", [fg1, fg2])

    res = m.breed(f)

    print(res.genes[0].genotype, res.genes[1].genotype)