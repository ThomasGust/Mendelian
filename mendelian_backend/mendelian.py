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
        self.g = g

        self.a1 = self.allele[self.g[0]]
        self.a2 = self.allele[self.g[1]]

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
            sa = random.choice(gp[0].g)
            ma = random.choice(gp[1].g)

            new_gene = Gene(gp[0].character, [sa, ma])
            new_genes.append(new_gene)
        
        product = Organism(f"Child-{self.name}-{mate.name}", new_genes)

        return product

    
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

def make_row(genotype, allele):
	row = []
	for a in genotype:
		row.append(a + allele)
	return row

def make_table(parent1, parent2):
	table = []
	for a in parent1:
		table.append(make_row(parent2, a))
	return table

def get_all_combinations(parent): # Finds all possible combinations of alleles a parent can pass on to their offspring, assuming independen assortment.
	if len(parent) == 1:
		return [parent[0][0], parent[0][1]]
	else:
		genlist = []
		for x in get_all_combinations(parent[1:]):
			genlist.append(parent[0][0] + x)
			genlist.append(parent[0][1] + x)
		return genlist

def print_table(table, c1, c2): # formats and prints Punnett square
	latextable = []
	divlength = (len(c1[0])*2+4)*2**(len(c1[0]))
	print('')
	print('', end=' ')
	for a in c2:
		print(' '*(len(c1[0])+3) + a + '', end=' ')
		latextable.append('& ' + a + ' ')
	print('\n' + ' '*(len(c1[0])+1) + '-'*(divlength))
	latextable.append('\\\ \n\\hline\n')
	
	for i, row in enumerate(table):
		print(c1[table.index(row)], end=' ')
		latextable.append(c1[table.index(row)] + ' & ')
		print('|', end=' ')
		for j, cell in enumerate(row):
			print(cell + ' | ', end=' ')
			if j != len(row)-1:
				latextable.append(cell + ' & ')
			else:
				latextable.append(cell + ' ')
		print('\n' + ' '*(len(c1[0])+1) + '-'*(divlength))
		if i != len(table)-1:
			latextable.append('\\\ \n')	
	return latextable

if __name__ == "__main__":
    #environment = Environment('Human')
    c1 = get_all_combinations("Aa BB".split(' '))
    c2 = get_all_combinations("aa Ba".split(' '))
    t = make_table(c1, c2)
    for row in t:
        print(row)
