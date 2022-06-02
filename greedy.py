import pickle
from random import choices, randint
from typing import List
import efficiency as eff

Genome = List[int]
Population=List[Genome]

population_size=500


def greedy(sub_path, sol_path):
    pickle_in = open(sub_path, 'rb')
    subject = pickle.load(pickle_in)

    #Create 500 randomly solutions
    print('create the initial population...')
    population=organize_population(subject)
    b=BestAndBad(population)
    print(fr'best solution={b[1]}')
    population=SortDesc(population)
    with open(sol_path, 'wb') as f:
        pickle.dump(population, f)
    return population

def SortAccordingSimEff(genome, subject)->Genome:
    items, _=subject
    sim=eff.simple(items)
    length=len(sim)
    ge=[]
    for i in range(length):
        if sim[i] in genome:ge.append(sim[i])
    return ge

def SortAccordingScEff(genome, subject):
    sc=eff.scaled(subject)
    length=len(sc)
    ge=[]
    for i in range(length):
        if sc[i] in genome:ge.append(sc[i])
    return ge

def generate_genome(items)->Genome:
    return sorted(set(randint(0, len(items)-1) for _ in range(len(items)//5)))

def generate_population(subject)->Population:
    return [SortAccordingScEff(generate_genome(subject[0]), subject) for _ in range(population_size)]



def fitness(genome:Genome, subject)->int:
    items, k=subject
    cap=len(k.capacities)
    weights=[]
    for i in range(cap):
        weights.append(0)
    value=0
    for i in range(len(genome)):
        for j in range(cap):
            weights[j]=weights[j]+int(items[genome[i]].resource[j])
        value=value+int(items[genome[i]].value)
    for i in range(len(weights)):
        if weights[i]>int(k.capacities[i]):
            return 0
    return value

def informations(genome:Genome, subject):
    value=genome[1]
    genome=genome[0]
    items, k=subject
    cap=len(k.capacities)
    weights=[]
    for i in range(cap):
        weights.append(0)
    value=0
    for i in range(len(genome)):
        for j in range(cap):
            weights[j]=weights[j]+int(items[genome[i]].resource[j])
        value=value+int(items[genome[i]].value)
    print(fr'cap={k.capacities}')
    print(fr'weights={weights}, value={value}')

def BestAndBad(population)->Genome:
    values=[]
    for i in range(len(population)):
        values.append(population[i][1])
    m=values.index(max(values))
    return population[m]

def SortDesc(population)->Population:
    p=[]
    for i in range(len(population)):
        p.append(population[i][1])
    p.sort(reverse=True)
    for i in range(len(p)):
        for j in range(len(population)):
            if p[i]==population[j][1]:
                p[i]=population[j]
                break
    return p

def organize_population(subject):
    population=generate_population(subject)
    for i in range(len(population)):
        value=fitness(population[i], subject)
        population[i]=[population[i], value]
    return population
