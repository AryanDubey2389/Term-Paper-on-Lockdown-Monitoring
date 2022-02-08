import pickle
import json
import sys

SCORE_DICT_PATH = 'score_dict.pickle'
POP_SCORES_FILE = 'pop_scores.json'
GENOTYPE_LEN = 11

def get_ordered(genotype):
    o_genotype = [None] * GENOTYPE_LEN
    for i in range(len(genotype)):
        index = int(genotype[i][1])
        allele = genotype[i][0]
        o_genotype[index] = allele
    return o_genotype

def find_fitness_view(errors, p=0.2):
    fit_score = -(p*errors[0] + (1 - p)*errors[1])
    return fit_score

def get_par(index):
    with open(SCORE_DICT_PATH, 'rb') as handle:
        score_dict = pickle.load(handle)
    genotype = None
    fitness = 0
    with open(POP_SCORES_FILE) as f:
        data = json.load(f)
    for i, geno in enumerate(score_dict.keys()):
        if i == index:
            genotype = geno
            fitness = find_fitness_view(score_dict[geno])
            break
    print(*genotype, sep='\n')
    print()
    print("fitness:", fitness)
    print()

    for i in range(len(data)):
        for geno in data[i]['Genotype']:
            if get_ordered(geno) == list(genotype):
                return geno    


if __name__ == "__main__":
    try:
        index = int(sys.argv[1])
        par = get_par(index)
        if par == None:
        	print("This vector never became a parent")
        else:
        	print(json.dumps(par, indent=4))
    except json.decoder.JSONDecodeError:
        print("Decoding JSON has failed.")
