import pickle
from random import choices, randint, choice
from typing import List
import info
import greedy
import efficiency as eff
import time
import matplotlib.pyplot as plt
import Local_Search as LS

Genome=List[int]
Population=List[Genome]
pickle_in=open(info.sub_path, 'rb')
items, _=pickle.load(pickle_in)
length_items=len(items)

def Hill_climbing(a: Genome)->Genome:
    sim=eff.simple()
    th=len(sim)//3
    th=sim[th:]
    f=[]
    for i in range(len(a)):
        if a[i] in th:
            f.append(a[i])
    for i in range(len(f)):
        a.remove(f[i])
    for i in range(len(sim)):
        if sim[i] not in a:
            a.append(sim[i])
            value=greedy.fitness(a)
            if value==0:
                a.remove(sim[i])
    return [a, greedy.fitness(a)]

def local_search(a: Genome, b: Genome)->Population:
    return LS.mine(a), LS.mine(b)

def selection_pair(population)->Population:
    return choices(
        population,
        k=2
    )

def crossover(a:Genome, b:Genome)->Population:
    length=len(b)
    p=randint(0, length-1)
    return sorted(set(a[0:p]+b[p:])), sorted(set(b[0:p]+a[p:]))

def mutation(a:Genome):
    r=randint(0, length_items-1)
    a.append(r)
    value=greedy.fitness(a)
    if value==0:
        a.remove(r)
    return [a, value]


def toMutation(a:Genome, b:Genome):
    return mutation(a), mutation(b)

def genetic(population: Population, cand:int)->Population:
    candidates=[]
    for i in range(cand):
        candidates.append(population[i])
    a, b=selection_pair(candidates)
    a=a[0]
    b=b[0]
    length=min(len(a), len(b))
    if length==len(b):
        a, b= crossover(a, b)
        return mutation(a), mutation(b)
    b, a= crossover(b, a)
    return mutation(b), mutation(a)

def process(population=Population, pc=float)->Population:

    #populatino size "len(population)"
    ps=len(population)

    #Define the candidates of the crossover operation according pc
    cand=ps*pc

    a, b=genetic(population, int(cand))
    a, b=local_search(a[0], b[0])

    population[-1]=a; population[-2]=b

    population=greedy.SortDesc(population)

    return population

def begin(population:Population, pc:float, g:int)->Genome:
    m=[]
    for i in range(g):
        population=process(population, pc)
        b=greedy.BestAndBad(population)
        m.append(greedy.BestAndBad(population)[1])
    return m, population

def main():
    greedy.greedy()
    """pickle_in=open(info.best_path, 'rb')
    best_popu=pickle.load(pickle_in)"""

    pickle_in=open(info.sol_path, 'rb')
    population=pickle.load(pickle_in)
    b=greedy.BestAndBad(population)

    first=[]
    second=[]

    first.append(b[1])
    second.append(b[1])

    g = 500  # number of generations
    #Crossover probability
    pc1=0.2
    pc2=0.1
    start = time.time()
    print(fr'crossover probability pc={pc1}, and pc={pc2}')
    print(fr'build {g} generations...')

    m1, popu1=begin(population, pc1, g)
    first=first+m1
    m2, popu2=begin(population, pc2, g)
    second=second+m2

    pickle_out = open(info.sol_path, 'wb')
    if max(first)>=max(second):
        pickle.dump(popu1, pickle_out)
        greedy.informations(greedy.BestAndBad(popu1))
    else:
        pickle.dump(popu2, pickle_out)
        greedy.informations(greedy.BestAndBad(popu2))

    end=time.time()
    print(fr'running time:{end-start}')

    x=[]; y=[]; y1=[]
    for i in range(len(first)):
        x.append(i); y.append(first[i]); y1.append(second[i])

    plt.plot(x, y, color='b', label=(pc1, [max(y), x[y.index(max(y))]]))
    plt.plot(x, y1, color='r', label=(pc2, [max(y1), x[y1.index(max(y1))]]))
    plt.legend(loc='lower center')

    plt.xlabel('generation')
    plt.ylabel('Fitness value')

    plt.title(fr'generate {g} generations in {round((end-start), 2)} seconds')

    plt.show()
