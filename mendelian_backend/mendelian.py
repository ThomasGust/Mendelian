class Gene:

    def __init__(self, a, g):

        assert type(a) == str and len(a) == 1
        self.allele = [a.lower(), a.upper()]

        assert type(g) == list and len(g) == 2
        self.genotype = g

        self.a1 = self.allele[self.genotype[0]]
        self.a2 = self.allele[self.genotype[1]]

        self.j = f"{self.a1}{self.a2}"


class Organism:

    def __init__(self, name, genes):
        pass
