import pickle
import time
import numpy as np
from typing import List
import efficiency as eff
import info
from matplotlib import pyplot as plt
import greedy
import operation

Genome=List[int]

def change(l, v, length):
    old_value=greedy.fitness(l)
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

def supervisor_method(a):
    pickle_in=open(info.sub_path, 'rb')
    items, _=pickle.load(pickle_in)


    m=change(a, a[0], len(items))
    for i in range(len(a)):
        g=change(a, a[i], len(items))
        if g[1]>=m[1]:m=g
    return g

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

def mine(a: Genome)->Genome:
    return Hill_climbing(a)
    return a


def LS():


    pickle_in=open(info.sol_path, 'rb')
    popu=pickle.load(pickle_in)





    start=time.time()
    y_eff=[]
    y_sim=[]
    t_eff=[]
    t_sim=[]
    for i in range(0, len(popu)):
        start=time.time()
        a=pro_method(popu[i])
        y_sim.append(a[1])
        end=time.time()
        t=end-start
        t_sim.append(round(t, 2))

        #print(fr'a={popu[i][1]}=>{a[1]} b={popu[i+1][1]}=>{b[1]}, time={round(end-start, 1)}')
        start=time.time()
        a=mine(popu[i][0])
        y_eff.append(a[1])
        end=time.time()
        t=end-start
        t_eff.append(round(t, 2))
        """
        print(fr'a={popu[i][1]}=>{a[1]} b={popu[i+1][1]}=>{b[1]}, time={round(end-start, 1)}')
        print('_____________________')"""
    end=time.time()


    print(fr'running time={end-start}')
    x=[]
    y=[]
    for i in range(len(popu)):
        y.append(popu[i][1])
        x.append(i)


    plt.subplot(1, 2, 1)
    plt.title('neighborhood')
    plt.plot(x, y, color='b', label='original values')
    plt.plot(x, y_sim, color='r', label='simple method')
    plt.plot(x, y_eff, color='y', label='efficiency method')
    plt.legend(loc='lower left')
    plt.xlabel('solutions')
    plt.ylabel('fitness values')


    plt.subplot(1, 2, 2)
    plt.title('time running')
    print(t_sim)
    print(t_eff)
    t_sim=np.array(t_sim)
    t_eff=np.array(t_eff)
    plt.plot(x, t_sim, color='r', label='running time for simple method')
    plt.plot(x, t_eff, color='y', label='running time for efficiency method')
    plt.xlabel('solutions')
    plt.ylabel('time "s"')


    plt.show()
