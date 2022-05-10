import pickle
from random import choices, randint, randrange, random
from typing import List
import Local_Search as ls
import greedy
import info

Genome=List[int]
Population=List[Genome]

def selection_pair(popu:Population)->Population:
    return choices(popu, k=2)

def crossover(a:Genome, b:Genome)->Population:
    p=randint(0, len(b)-1)
    return a[0:p]+b[p:], b[0:p]+a[p:]

def genetic(popu:Population, cand:int)->Population:
    candidates=[]
    for i in range(cand):
        candidates.append(popu[i])
    a, b=selection_pair(candidates)
    a=a[0]; b=b[0]
    length=min(len(a), len(b))
    if length==len(b):
        return crossover(b, a)
    return crossover(a, b)

def process(popu:Population, pc:float):
    print(fr'a={popu[0][1]}, b={popu[1][1]}')

    #population size "len(population)"
    ps=len(popu)

    #Define the candidate of the crossover operation according the crossover probability pc
    cand=ps*pc

    a, b=genetic(popu, int(cand))

    a=ls.mine(a)
    b=ls.mine(b)

    print(fr'a={a[1]}, b{b[1]}')


def main():
    pickle_in=open(info.sol_path, 'rb')
    popu=pickle.load(pickle_in)

    process(popu, 0.2)
