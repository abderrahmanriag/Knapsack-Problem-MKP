import pickle
from typing import List
import info

Genome=List[int]
def simple()->Genome:
    pickle_in=open(info.sub_path, 'rb')
    items, _=pickle.load(pickle_in)

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