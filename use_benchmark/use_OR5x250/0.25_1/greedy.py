import pickle
from random import choices, randint
from typing import List
import info
from object import *
import efficiency as eff

Genome = List[int]
Population=List[Genome]

def greedy():
    #Create 500 randomly solutions
    pickle_in=open(info.sub_path, 'rb')
    items, k=pickle.load(pickle_in)
    print('create the init population...')
    size=500
    population=generate_population(size, len(items))
    for i in range(len(population)):
        value=fitness(population[i])
        population[i]=[population[i], value]
    b=BestAndBad(population)
    print(fr'best solution in init population ={b[1]}')
    population=SortDesc(population)
    pickle_out=open(info.sol_path, 'wb')
    pickle.dump(population, pickle_out)
    return population

def SortAccordingEff(genome)->Genome:
    sim=eff.simple()
    length=len(sim)
    ge=[]
    for i in range(length):
        if sim[i] in genome:ge.append(sim[i])
    return ge

def generate_genome(length: int)->Genome:
    return sorted(set(randint(0, length-1) for _ in range(length//5)))

def generate_population(size: int, genome_length:int)->Population:
    return [SortAccordingEff(generate_genome(genome_length)) for _ in range(size)]

def fitness(genome:Genome)->int:
    pickle_in=open(info.sub_path, 'rb')
    items, k=pickle.load(pickle_in)
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


def informations(genome:Genome):
    value=genome[1]
    genome=genome[0]
    pickle_in=open(info.sub_path, 'rb')
    items, k=pickle.load(pickle_in)
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