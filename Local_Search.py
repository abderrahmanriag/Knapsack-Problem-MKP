from typing import List
import pickle
import efficiency as eff
import greedy

Genome=List[int]



def upgrade(g:Genome, a:int, r:int, v:int, subject):
    g[g.index(a)]=r
    value= greedy.fitness(g, subject)
    if value>=v:
        return [g, value]
    g[g.index(r)]=a
    return [g, v]

def neighborhood(g:Genome, subject):
    sim=eff.simple(subject[0])
    value=greedy.fitness(g, subject)
    g=[g, value]
    for i in range(len(g)):
        for j in range(len(sim)):
            if sim[j] not in g:
                value=g[1]
                g=g[0]
                g=upgrade(g, g[i], sim[j], value, subject)
    return g[0]

def main(sol_path):
    pickle_in=open(sol_path, 'rb')
    population=pickle.load(pickle_in)

    b= greedy.BestAndBad(population)

    print(fr'best={b}')
    print(fr'best={b[1]}')
    b=neighborhood(b)
    print(fr'best={b[1]}')