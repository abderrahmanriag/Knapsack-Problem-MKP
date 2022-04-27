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
    a=Hill_climbing(a)
    b=Hill_climbing(b)
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
    a, b=local_search(a[0], b[0])

    #print(fr'{a[1]}, {b[1]}')

    population[-1]=a
    population[-2]=b

    population=greedy.BesttoWorst(population)

    b=greedy.BestAndWorst(population)
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
    #greedy.greedy()
    pickle_in=open(info.best_path, 'rb')
    best_popu=pickle.load(pickle_in)

    pickle_in=open(info.sol_path, 'rb')
    population=pickle.load(pickle_in)
    b=greedy.BestAndWorst(population)
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
    g = 500  # number of generations
    print(fr'Creating {g} generations...')

    start=time.time()
    #Crossover probability
    pc=0.7
    pc1=0.2
    for i in range(g):
        coor=process(population, i+1, pc)
        coordinates1.append(coor)
        coor=process(best_popu, i+1, pc1)
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


    plt.plot(x, y, color='b', label=[pc, max(y), x[y.index(max(y))]])
    plt.plot(x, y1, color='r', label=[pc1, max(y1), x[y1.index(max(y1))]])
    plt.legend(loc='lower center')


    plt.xlabel('generation')
    plt.ylabel('Fitness value')

    plt.title(fr'fitness func for {g} generations')

    plt.show()

start=time.time()
main()
end=time.time()
print(fr'running time.{end-start}')
"""
pickle_in = open(info.best_path, 'rb')
population = pickle.load(pickle_in)
b = greedy.BestAndWorst(population)
print(fr'best value={b[1]}')
value = greedy.fitness(b[0])
print(fr'value={value}')
"""