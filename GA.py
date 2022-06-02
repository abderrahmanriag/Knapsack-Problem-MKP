import pickle
from random import choice, randint
import greedy
import my_approach as o

def mutation(a, subject):
    v=greedy.fitness(a, subject)
    items=subject[0]
    c=randint(0, len(items)-1)
    while c in a:
        c=randint(0, len(items)-1)
    a.append(c)
    value = greedy.fitness(a, subject)
    if value>=v:
        return [a, value]
    a.remove(c)
    return [a, v]

def genetic(population, subject, pc):

    #Get the number of candidates of crossover operation
    cand=len(population)*pc

    candidates=[]
    while len(candidates)!=int(cand):
        g=choice(population)
        if g not in candidates:
            candidates.append(g)

    a, b=o.selection_pair(candidates)
    a=a[0];b=b[0]
    length=min(len(a), len(b))
    if length==len(a):
        a, b=o.crossover(a, b)
        return mutation(a, subject), mutation(b, subject)
    b, a=o.crossover(b, a)
    return mutation(b, subject), mutation(a, subject)

def process(population, subject, pc:float):
    a, b=genetic(population, subject, pc)
    population[-1]=a;population[-2]=b
    return greedy.SortDesc(population)



def begin(population, pc:float, g:int, subject):

    m=[]
    for i in range(g):
        population=process(population, subject, pc)
        m.append(greedy.BestAndBad(population)[1])
    return m, population




