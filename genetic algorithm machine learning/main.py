import numpy as np
import pandas as pd
import random
import client
import json
import os
import pickle

POP_SIZE = 30
POOL_SIZE = POP_SIZE // 2
GENOTYPE_LEN = 11
ALLELE_MIN = -10 #  try to reduce it to -5, 0, ...
ALLELE_MAX = 10
NICHE_DISTANCE = 2
N_GENERATIONS = 1
INIT_GENOTYPE = [0.0, -1.45799022e-12, -2.28980078e-13,  4.62010753e-11, -1.75214813e-10, -1.83669770e-15,  8.52944060e-16,  2.29423303e-05, -2.04721003e-06, -1.59792834e-08,  9.98214034e-10]
POP_SCORES_FILE = 'pop_scores.json'
PARENT_CHILD_FILE = 'parent_child.json'
SCORE_DICT_PATH = 'score_dict.pickle'
score_dict = {}


def save(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
        
def mutate(gen, e=0.2, force=False):
    genotype = gen[:]
    if len(genotype) != GENOTYPE_LEN:
        raise IndexError('Invalid size geno')
    probabs = [np.random.random() for _ in range(GENOTYPE_LEN)]
    if force:
        if min(probabs) > e:
            index = random.randint(0, GENOTYPE_LEN-1)
            probabs[index] = e/10
    for i, p in enumerate(probabs):
        if p < e:
            allele = genotype[i][0]
            index = genotype[i][1]

            if allele != 0:
                allele *= random.choice([-1, 1]) * random.uniform(0.9, 1.1)
            else:
                allele = random.uniform(-1, 1)
            genotype[i] = [allele, index]
    # genotype = np.array(genotype)
    genotype = np.clip(genotype, ALLELE_MIN, ALLELE_MAX)
    return genotype

def get_ordered(genotype):
    """
    convert an order free genotype to an 
    ordered genotype
    """
    o_genotype = [None] * GENOTYPE_LEN
    for i in range(len(genotype)):
        index = int(genotype[i][1])
        allele = genotype[i][0]
        o_genotype[index] = allele
    return o_genotype

def get_niche_distance(genotype1, genotype2):
    """
    find the number of positions in which 
    the strings differ
    """
    dist = 0
    o_genotype1 = get_ordered(genotype1)
    o_genotype2 = get_ordered(genotype2)
    for i in range(GENOTYPE_LEN):
        dist += (o_genotype1[i] != o_genotype2[i])
    return dist

def find_fitness(genotype1, errors, pop_dict,  p=0.1):
    fit_score = -(p*errors[0] + (1 - p)*errors[1])
    N = 0
    for genotype in pop_dict['Genotype']:
        if get_niche_distance(genotype1, genotype) < NICHE_DISTANCE:
            N += 1
    N = 1
    return fit_score/N    

def generate_pop():
    """
    Generate the starting population
    """
    pop_dict = {
        'Genotype': [],
        'Train Error': [],
        'Validation Error': [],
        'Fitness': []
    }
    
    pop = [make_order_free(INIT_GENOTYPE)]
    
    for i in range(POP_SIZE):
        index = np.random.randint(len(pop))
        genotype = pop[index]
        mutated_genotype = mutate(genotype, e=0.4)
        random.shuffle(mutated_genotype)
        pop.append(mutated_genotype[:])
    
#         for g in pop:
#             print([a[1] for a in g], sep=',')
#         print()    
    pop = np.array(pop)
    pop = np.round(pop, 2)
    np.random.shuffle(pop)
    
    for i in range(POP_SIZE):
        
        pop_dict['Genotype'].append(pop[i])
        errors = get_errors(pop[i])
        te = errors[0]
        ve = errors[1]
        fitness = find_fitness(pop[i], errors, pop_dict)
        pop_dict['Train Error'].append(te)
        pop_dict['Validation Error'].append(ve)
        pop_dict['Fitness'].append(fitness)
        
    return pop_dict

def get_proba(v):
    """
    find the selection probability
    """
    # mutate
    p = []
    least = min(v)
    v = [utility - least for utility in v]
    total = sum(v)
    if total == 0:
        p = [0] * POP_SIZE
        p[0] = 1
        return p
    for utility in v:
        p.append(utility/total)
    return p

def make_order_free(genotype):
    of_genotype = []
    for i, allele in enumerate(genotype):
        of_genotype.append([allele, i])
    return of_genotype

def get_ordered_list(pop):
    o_pop = []
    for genotype in pop:
        o_pop.append(get_ordered(genotype))
    return o_pop

def lineup(g1, g2): 
    """
    align vector g2 along g1
    """
    new_g2 = []
    for i in range(len(g1)):
        for j in range(len(g2)):
            if g1[i][1] == g2[j][1]:
                new_g2.append(g2[j])   
                break
    return new_g2

def crossover(parent1, parent2):
    index = int(np.random.randint(1, GENOTYPE_LEN))

    child1 = np.r_[parent1[:index], parent2[index:]]
    child2 = np.r_[parent2[:index], parent1[index:]]

    return child1, child2

def get_mating_pool(pop_dict):
    """
    find the fitness scores of parent
    and select a subset of them with the 
    selection probability
    """
    rng = np.random.default_rng()
    fitness_scores = pop_dict['Fitness']
    
    return rng.choice(POP_SIZE, POOL_SIZE, p=get_proba(fitness_scores))

def get_parent_indices(mating_pool):
    assert len(mating_pool) >= 2, "invalid size of mating pool"
    rng = np.random.default_rng()
    return rng.choice(len(mating_pool), 2, False)
  

def get_least_fit_index(fitness_list):
    mn_fitness = 0
    index = -1
    for i, fitness in enumerate(fitness_list):
        if fitness < mn_fitness:
            mn_fitness = fitness
            index = i
            
    if index == -1:
        print('scores are 0')
    return index

def get_errors(genotype):
    """
    find the train and validation error
    """
    global score_dict
    geno = tuple(get_ordered(genotype))
    if score_dict and (geno in score_dict):
        return score_dict[geno]
    score_dict[geno] = client.get_errors(client.SECRET_KEY, get_ordered(genotype))
    return score_dict[geno]

def replace_least_fit(child, pop_dict): 
    index = get_least_fit_index(pop_dict['Fitness'])
    pop_dict['Genotype'][index] = child[:]
    errors = get_errors(child)
    pop_dict['Train Error'][index] = errors[0]
    pop_dict['Validation Error'][index] = errors[1]
    pop_dict['Fitness'][index] = find_fitness(child, errors, pop_dict)

def mate(mating_pool, pop_dict, g_index):
    for i in range(POP_SIZE//2):
        mate_dict = {}
    
        index1, index2 = get_parent_indices(mating_pool)
       
        parent1 = pop_dict['Genotype'][index1]
        parent2 = pop_dict['Genotype'][index2]
        parent2 = lineup(parent1, parent2)
        
        child1, child2 = crossover(parent1, parent2)
#         df = pd.DataFrame(columns=['Generation', 'Parent1', 'Parent2', 'Child1', 'Child2', 'Mutated Child1', 'Mutated Child2'])
        mate_dict['Generation'] = g_index
        mate_dict['Parent1'] = get_index(parent1)
        mate_dict['Parent2'] = get_index(parent2)
        mate_dict['Child1'] = get_index(child1)
        mate_dict['Child2'] = get_index(child2)
        child1 = mutate(child1)
        child2 = mutate(child2)
        mate_dict['Mutated Child1'] = get_index(child1)
        mate_dict['Mutated Child2'] = get_index(child2)
    
        df = pd.DataFrame(mate_dict, index=[0])
        save_parent_child(df)

        replace_least_fit(child1, pop_dict)
        replace_least_fit(child2, pop_dict)


def genetic_algo(n_gen=N_GENERATIONS):
    
    if not os.path.exists(POP_SCORES_FILE):
        pop_dict = generate_pop()
        save([], POP_SCORES_FILE)
    else:
        with open(POP_SCORES_FILE) as f:
            data = json.load(f)
        pop_dict = {
            'Genotype': data[-1]['Genotype'],
            'Train Error': data[-1]['Train Error'],
            'Validation Error': data[-1]['Validation Error'],
            'Fitness': data[-1]['Fitness']
        }
    for g_index in range(1, n_gen+1):

        pop = {'Genotype': []}
        for geno in pop_dict['Genotype']:
            pop['Genotype'].append(get_index(geno))
        save_parent_child(pop)

        mating_pool = get_mating_pool(pop_dict)
        mate(mating_pool, pop_dict, g_index)

        with open(POP_SCORES_FILE, 'r') as f:
            data = json.load(f)
            
        pop_dict['Genotype'] = [geno.tolist() if isinstance(geno, np.ndarray) else geno for geno in pop_dict['Genotype']] 
        data.append(pop_dict)
        save(data, POP_SCORES_FILE)   
        
def score_dict_init():
    global score_dict
    if os.path.exists(SCORE_DICT_PATH):
        with open(SCORE_DICT_PATH, 'rb') as handle:
            score_dict = pickle.load(handle)
    
def save_parent_child(data, file='child.txt'):
    df = pd.DataFrame(data)
    df.to_csv(file, mode='a')

def get_index(genotype):
    global score_dict
    get_errors(genotype)
    for i, geno in enumerate(score_dict.keys()):
        if geno == tuple(get_ordered(genotype)):
            return i
    print('index error')
    raise SystemExit

def save_score_dict():
    global score_dict  
    with open(SCORE_DICT_PATH, 'wb') as handle:
        pickle.dump(score_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)

if __name__ == '__main__':
    score_dict_init()
    genetic_algo()
    save_score_dict()

