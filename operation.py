import pickle
from random import choices, randint
from typing import List
import info
import greedy
import efficiency as eff
import time
import matplotlib.pyplot as plt

Genome=List[int]
Population=List[Genome]
Coor=List[int]


def change(l, v, length):
    old_value=l[1]
    l=l[0]
    for i in range(length):
        if i not in l:
            index=l.index(v)
            l[index]=i
            value=greedy.fitness(l)
            if value>=old_value:
                old_value=value
                v=i
            else:
                l[index]=v
    return [l, old_value]

def Hill_Climbing(b):

    pickle_in=open(info.sub_path, 'rb')
    items, _=pickle.load(pickle_in)
    v=b[0][0]
    g=change(b, v, len(items))
    for i in range(len(b[0])):
        m=change(b, b[0][i], len(items))
        if m[1]>=g[1]:g=m
    return g

def Local_Search(a, b):
    a=Hill_Climbing(a)
    b=Hill_Climbing(b)
    return [a, b]

def selection_pair(population)->Population:
    return choices(
        population,
        k=2
    )

def crossover(a:Genome, b:Genome)->Population:
    length=len(b)
    p=randint(0, length-1)
    return a[0:p]+b[p:], b[0:p]+a[p:]

def genetic(population: Population, cand:int)->Population:
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

def process(population=Population, i=int, pc=float)->Coor:

    #populatino size "len(population)"
    ps=len(population)

    #Define the candidates of the crossover operation according pc
    cand=ps*pc

    a, b=genetic(population, int(cand))
    a=[a, greedy.fitness(a)]
    b=[b, greedy.fitness(b)]
    a, b=Local_Search(a, b)

    #print(fr'{a[1]}, {b[1]}')

    population[-1]=a
    population[-2]=b

    population=greedy.SortDesc(population)

    b=greedy.BestAndBad(population)
    #print(fr'{i}--Best={b[1]}')
    coor=Coor
    if i!=0:
        x=i+1
        y=b[1]
        coor=(x, y)

    pickle_out=open(info.sol_path, 'wb')
    pickle.dump(population, pickle_out)
    return coor

def main():
    greedy.greedy()
    """pickle_in=open(info.best_path, 'rb')
    best_popu=pickle.load(pickle_in)"""

    pickle_in=open(info.sol_path, 'rb')
    population=pickle.load(pickle_in)
    b=greedy.BestAndBad(population)
    x=1
    y=b[1]
    coor=[x, y]
    coordinates1=[]
    coordinates2=[]
    coordinates1.append(coor)
    coordinates2.append(coor)
    """
    b=greedy.BestAndWorst(population)
    print(fr'best value={b[1]}')
    value=greedy.fitness(b[0])
    print(fr'value={value}')
    """
    g = 50  # number of generations
    print(fr'Creating {g} generations...')

    start=time.time()
    #Crossover probability
    pc=0.2
    pc1=0.25
    for i in range(g):
        coor=process(population, i+1, pc)
        coordinates1.append(coor)
        coor=process(population, i+1, pc1)
        coordinates2.append(coor)
    end=time.time()
    print(fr'running time:{end-start}')

    x=[]
    y=[]
    y1=[]
    for i in range(len(coordinates1)):
        x.append(coordinates1[i][0])
        y.append(coordinates1[i][1])
        y1.append(coordinates2[i][1])
    """print(fr'max value{max(y)} generation number={x[y.index(max(y))]}for pc={pc}')
    print(fr'max value{max(y1)} generation number={x[y1.index(max(y1))]}for pc={pc1}')"""


    plt.plot(x, y, color='b', label=(pc, [max(y), x[y.index(max(y))]]))
    plt.plot(x, y1, color='r', label=(pc1, [max(y1), x[y1.index(max(y1))]]))
    plt.legend(loc='lower center')


    plt.xlabel('generation')
    plt.ylabel('Fitness value')

    plt.title(fr'fitness func for {g} generations')

    plt.show()


"""
pickle_in = open(info.best_path, 'rb')
population = pickle.load(pickle_in)
b = greedy.BestAndWorst(population)
print(fr'best value={b[1]}')
value = greedy.fitness(b[0])
print(fr'value={value}')
"""