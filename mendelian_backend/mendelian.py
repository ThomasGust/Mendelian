import random
import string
import numpy as np
import math

idx_dict = {0:"e", 1:"r", 2:"g", 3:"q", 4:"p", 5:"t", 6:"s", 7:"f", 8:"d", 9:"y", 10:'n', 11:"l", 12:"h", 13:"j"}

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

def get_combinations(p):
  if len(p) == 1:
    return [p[0][0], p[0][1]]

  else:
    g = []
    for a in get_combinations(p[1:]):
      g.append(p[0][0]+a)
      g.append(p[0][1]+a)

    return g

def create_punnet_square(p1, p2):
  assert len(p1) == len(p2)

  comb1 = get_combinations(p1)
  comb2 = get_combinations(p2)

  arr = [[[] for i in range(len(comb2))] for i in range(len(comb1))]
  for i, a in enumerate(comb1):
    for j, aj in enumerate(comb2):
      arr[i][j] = f"{a}{aj}"
  
  for row in arr:
    print(row)

def create_monster():
  mon = [list(a) for a in input("Please Input A Valid Monster String: ").split(' ')]
  assert len(mon) == 14

  return mon
def create_punnet_square_gene_indices(p1, p2, gene_indices):
  assert len(p1) == len(p2)

  np1 = []
  np2 = []

  for i, g in enumerate(p1):
    if i in gene_indices:
      np1.append(g)

  for i, g in enumerate(p2):
    if i in gene_indices:
      np2.append(g)

  p1 = np1
  p2 = np2

  comb1 = get_combinations(p1)
  comb2 = get_combinations(p2)

  arr = [[[] for i in range(len(comb2))] for i in range(len(comb1))]
  for i, a in enumerate(comb1):
    for j, aj in enumerate(comb2):
      arr[i][j] = f"{a}{aj}"
  return arr

def get_punnet_square_length(punnet_square):

  flat = []

  for x in punnet_square:
    for y in x:
      flat.append(y)
  return len(flat)

def get_punnet_square_probabilities(punnet_square):

  nps = punnet_square

  for i, r in enumerate(punnet_square):
    for j, e in enumerate(r):
      nps[i][j] = set(e)

  punnet_square = nps
  arr = np.array(punnet_square)
  unique, counts = np.unique(arr, return_counts=True)

  percentages = []
  length = get_punnet_square_length(punnet_square)
  for i, n in enumerate(counts):
    percentages.append((unique[i], n/length))

  res = [0.0, 0.0, 0.0]

  for i, (s, p) in enumerate(percentages):
    if len(list(s)) == 1:
      if list(s)[0] in string.ascii_lowercase:
        res[0] += p
      if list(s)[0] in string.ascii_uppercase:
        res[1] += p
    else:
      res[2] += p
    
  return res

def format_punnet_square_percentages(probs):
  return f'Homozygous Recessive Chance:{probs[0]}\nHomozygous Dominant Chance:{probs[1]}\nHeterozygous Chance: {probs[2]}'

def create_random_monster():
  traits = [[random.choice([0, 1]) for i in range(2)] for j in range(14)]

  monster_traits = []

  for i, t in enumerate(traits):
    t1 = t[0]
    t2 = t[1]

    char = idx_dict[i]

    if t1 == 0:
      
      a1 = char.lower()

    if t1 == 1:
      a1 = char.upper()

    if t2 == 0:
      a2 = char.lower()

    if t2 == 1:
      a2 = char.upper()

    res = f"{a1}{a2}"

    monster_traits.append(res)

  monster_string = " ".join(monster_traits)

  return [list(a) for a in monster_string.split(' ')]
    
def monster_lab():
  monster1 = create_random_monster()
  monster2 = create_random_monster()

  for i in range(14):
    print(f"Punnet Square {i}, {idx_dict[i]}:")

    arr = create_punnet_square_gene_indices(monster1, monster2, [i])

    for row in arr:
      print(row)

    print(format_punnet_square_percentages(get_punnet_square_probabilities(arr)))
    print()

def breed_monster(monstr1, monstr2, top=False, print_punnet=True):

  probs = []

  for i in range(14):
    arr = create_punnet_square_gene_indices(monstr1, monstr2, [i])
      
    prob = get_punnet_square_probabilities(arr)
    probs.append(prob)

    if print_punnet:
      print(f"Punnet Square for Gene {i}, known as {idx_dict[i]}: ")

      narr = []
      for row in arr:
        print(row)
      print(format_punnet_square_percentages(prob))
      print()

  new_monster = []

  for i, prob in enumerate(probs):
    if not top:
      ng = random.choices([0, 1, 2], weights=prob, k=1)
      ng = ng[0]
    else:
      m = max(prob)
      ng = prob.index(m)

    if ng == 0:
      new_monster.append(f"{idx_dict[i].lower()}{idx_dict[i].lower()}")

    if ng == 1:
      new_monster.append(f"{idx_dict[i].upper()}{idx_dict[i].lower()}")

    if ng == 2:
      new_monster.append(f"{idx_dict[i].upper()}{idx_dict[i].upper()}")

  monstr_out = " ".join(new_monster)

  return monstr_out
  
if __name__ == "__main__":
  monstr1 = create_random_monster()
  monstr2 = create_random_monster()
  print(" ".join(f"{m[0]}{m[1]}" for m in monstr1))
  print(" ".join(f"{m[0]}{m[1]}" for m in monstr2))
  print(breed_monster(monstr1, monstr2, top=False))
