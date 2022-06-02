import pickle
from random import choices, randint, choice
from typing import List
import greedy
import info

Genome=List[int]
Population=List[Genome]
pickle_in=open(info.sub_path, 'rb')
items, _=pickle.load(pickle_in)
length_items=len(items)

def selection_pair(population)->Population:
    return choices(
        population,
        k=2
    )

def crossover(a:Genome, b:Genome)->Population:
    length=len(b)
    p=randint(0, length-1)
    return sorted(set(a[0:p]+b[p:])), sorted(set(b[0:p]+a[p:]))

def toCrossover(population, cand:int):
    candidates=[]
    for i in range(cand):
        candidates.append(population[i])
    a, b=selection_pair(candidates)
    a=a[0]
    b=b[0]
    length=min(len(a), len(b))
    if length==len(b):
        return crossover(a, b)
    return crossover(b, a)

def mutation(a:Genome):
    r=randint(0, length_items-1)
    a.append(r)
    value=greedy.fitness(a)
    if value==0:
        a.remove(r)
    return [a, value]


def toMutation(a:Genome, b:Genome):
    return mutation(a), mutation(b)

def process(population=Population, pc=float)->Population:

    #population size "len(population)"
    ps=len(population)

    #Define the candidates of the crossover operation according pc
    cand=ps*pc

    a, b=toCrossover(population, int(cand))
    a, b=toMutation(a, b)
    population[-1]=a; population[-2]=b
    population=greedy.SortDesc(population)

    return population

def begin(population:Population, pc:float, g:int):
    m=[]
    for i in range(g):
        population=process(population, pc)
        m.append(greedy.BestAndBad(population)[1])
    return m, population

