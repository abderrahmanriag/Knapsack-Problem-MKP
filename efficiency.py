import pickle
from typing import List

Genome=List[int]

def simple(items)->Genome:
    sim=[]
    length=len(items)
    for i in range(length):
        s=0
        for j in range(len(items[i].resource)):
            s=s+int(items[i].resource[j])
        d=int(items[i].value)/s
        d=round(d, 2)
        sim.append(d)
    for i in range(length):
        sim[i]=[sim[i], i]
    sim.sort(reverse=True)
    for i in range(length):
        sim[i]=sim[i][1]
    return sim

def scaled(subject):
    items, k=subject
    length=len(items)
    sc=[]
    for i in range(len(items)):
        s=0
        for j in range(len(k.capacities)):
            s=s+(int(items[i].resource[j])/int(k.capacities[j]))
        s=int(items[i].value)/s
        sc.append(round(s, 2))
    for i in range(length):
        sc[i]=[sc[i], i]
    sc.sort(reverse=True)
    for i in range(length):
        sc[i]=sc[i][1]

    return sc


