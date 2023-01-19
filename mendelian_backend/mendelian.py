import random
import string
import numpy as np
import math

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
    
    def compute_full_punnet_square(self, mate):
        assert len(self.genes) == len(mate.genes)

        punnet_square = np.zeros((math.pow(len(self.genes), 2), math.pow(len(mate.genes), 2)))
        

    
    def string_alleles(self):

        string_alleles = ""

        for gene in self.genes:
            string_alleles += gene.j
        
        return string_alleles

class Environment:
    def __init__(self, species_name, genes=list(string.ascii_lowercase), population_size=100):
        self.species_name = species_name
        self.population_size = population_size
        self.genes = genes

        self.organisms = []

        for _ in range(self.population_size):
            organism_genes = []
            for g in self.genes:
                organism_genes.append(Gene(g, [random.choice([0, 1]), random.choice([0, 1])]))
            
            self.organisms.append(Organism(self.species_name, genes=organism_genes))
    def random_pairs(self, ls):
        return [ls[i] for i in random.sample(range(len(ls)), 2)] 

    def step(self):
        organism_pairs = [self.random_pairs(self.organisms) for i in range(len(self.organisms)//2)]

        new_organisms = []

        for op in organism_pairs:
            new_organism1 = op[0].breed(op[1])
            new_organisms.append(new_organism1)
            new_organism2 = op[0].breed(op[1])
            new_organisms.append(new_organism2)
        
        self.organisms = new_organisms

        print(len(self.organisms))
    
    def simulate(self, epochs):
        for e in range(epochs):
            print(e)
            self.step()

if __name__ == "__main__":
    environment = Environment('Human')