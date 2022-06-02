import os
import pickle
from random import choices, randint, choice
from typing import List
import greedy
import efficiency as eff
import time
import matplotlib.pyplot as plt
import Local_Search as LS

Genome=List[int]
Population=List[Genome]

def sort_value(q, items):
    values=[]
    for i in range(len(q)):
        values.append(items[q[i]].value)
    values.sort(reverse=True)
    l=[]
    for i in range(len(values)):
        for j in range(len(q)):
            if items[q[j]].value==values[i]:
                l.append(q[j])
                break
    return l


def new_upgrade(a:Genome, subject):
    sc=eff.scaled(subject)
    half=len(sc)//2
    home=[]
    for i in range(len(a)):
        if a[i] in sc[half:]:
            home.append(a[i])
    for i in range(len(home)):
        a.remove(home[i])
    for i in range(len(sc[:half])):
        a.append(sc[i])
        value=greedy.fitness(a, subject)
        if value==0:a.remove(sc[i])
    return a


def upgrade(a: Genome, subject)->Genome:
    sc=eff.scaled(subject)
    th=len(sc)//3
    tth=th*2
    length=len(a)-1
    home=[]
    for i in range(len(a)):
        if a[length] in sc[tth:]:
            home.append(a[length])
            length-=1
    length=len(home)-1
    for i in range(len(home)):
        a.remove(home[length])
        length-=1
        if length==1:break
    for i in range(len(sc[:tth])):
        if sc[i] not in a:
            a.append(sc[i])
            value=greedy.fitness(a, subject)
            if value==0:a.remove(sc[i])
    return a

def mutation(a:Genome, subject):
    #a=upgrade(a, subject)
    return new_upgrade(a, subject)
    #return a

def local_search(a: Genome, b: Genome, subject)->Population:
    length=max(len(a), len(b))
    for i in range(length):
        a=LS.neighborhood(a, subject)
        b=LS.neighborhood(b, subject)
    #return upgrade(a[0], subject), upgrade(b[0], subject)
    return a, b

def selection_pair(population)->Population:
    return choices(
        population,
        k=2
    )

def reSort(a:Genome):
    b=[]
    length=len(a)-1
    for i in range(len(a)):
        b.append(a[length])
        length-=1
    return b

def remove_repetition(a:Genome):
    g=[]
    for i in range(len(a)):
        if a[i] not in g:g.append(a[i])
    return g

def crossover(a:Genome, b:Genome)->Population:
    #b=reSort(b)
    length=len(b)
    p=randint(0, length-1)
    return remove_repetition(a[0:p]+b[p:]), remove_repetition(b[0:p]+a[p:])

def organize_candidates(population:Population, cand:int):
    half=len(population)//2
    candidates=[]
    while len(candidates)!=cand//2:
        for i in range(len(population)):
            candidates.append(population[i])
    while len(candidates)!=cand:
        c=choice(population[half:])
        if c not in candidates:
            candidates.append(c)
    return candidates

def genetic(population: Population, cand:int, subject)->Population:
    #cand:NUMBER OF CANDIDATES FOR CROSSOVER OPERATION
    candidates=organize_candidates(population, cand)
    a, b=selection_pair(candidates)
    a=a[0]
    b=b[0]
    a = mutation(a, subject);  b= mutation(b, subject)
    length=min(len(a), len(b))
    if length==len(b):
        a, b = crossover(a, b)
    else:
        a, b = crossover(b, a)
    a=greedy.SortAccordingScEff(a, subject);b=greedy.SortAccordingScEff(b, subject)
    #a, b=local_search(a, b, subject)
    a = mutation(a, subject);  # b= mutation(b, subject)
    a, b=local_search(a, b, subject)
    a=remove_rep(a, subject); b=remove_rep(b, subject)
    return a, b

def remove_rep(a:Genome, subject):
    g=[]
    for i in range(len(a)):
        if a[i] not in g:
            g.append(a[i])
    value=greedy.fitness(g, subject)
    return [g, value]

def process(population:Population, pc:float, subject)->Population:

    #populatino size "len(population)"
    ps=len(population)

    #Define the candidates of the crossover operation according pc
    cand=ps*pc

    a, b=genetic(population, int(cand), subject)
    #a, b=local_search(a, b, subject)

    population[-1]=a; population[-2]=b

    population= greedy.SortDesc(population)

    return population

def begin(population:Population, pc:float, g:int, subject, max_path)->Genome:

    #g:NUMBER OF GENERATIONS
    #pc:CROSSOVER PROBABILITY

    if max_path in os.listdir(os.getcwd()):
        with open(max_path, 'rb') as f:
            maxs = pickle.load(f)
    else:
        maxs=[]

    if len(maxs)==g:
        maxs=[]
        """print(fr'the list is elready exist with best={maxs[-1]}')
        x=input(fr'press 1 to repeat 0 to stop  ')
        if x=='1':maxs=[]"""
    while len(maxs)!=g:

        population=process(population, pc, subject)
        b= greedy.BestAndBad(population)

        maxs.append(b[1])

        print(fr'best solution={b[1]}, in the generation number={len(maxs)}')


        with open(max_path, 'wb') as f:
            pickle.dump(maxs, f)

    return maxs, population

def main(sol_path, sub_path):
    population=greedy.greedy(sol_path, sub_path)
    """pickle_in=open(info.best_path, 'rb')
    best_popu=pickle.load(pickle_in)"""

    b= greedy.BestAndBad(population)

    first=[]
    second=[]

    first.append(b[1])
    second.append(b[1])

    g = 100  # number of generations
    #Crossover probability
    pc1=0.2

    start = time.time()
    print(fr'crossover probability pc={pc1}')
    print(fr'build {g} generations...')

    pickle_in=open(sub_path, 'rb')
    subject=pickle.load(pickle_in)
    m1, popu1=begin(population, pc1, g, subject)
    first=first+m1


    pickle_out = open(sol_path, 'wb')
    pickle.dump(popu1, pickle_out)
    greedy.informations(greedy.BestAndBad(popu1), subject)


    end=time.time()
    print(fr'running time:{end-start}')

    x=[]; y=[];
    for i in range(len(first)):
        x.append(i); y.append(first[i]);

    plt.plot(x, y, color='b', label=(pc1, [max(y), x[y.index(max(y))]]))
    plt.legend(loc='lower center')

    plt.xlabel('generation')
    plt.ylabel('Fitness value')

    plt.title(fr'generate {g} generations in {round((end-start), 2)} seconds')

    plt.show()
