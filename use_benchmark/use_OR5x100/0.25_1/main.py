import pickle
import matplotlib.pyplot as plt
import numpy as np
import greedy
import try_methods
import operation
import info
import efficiency
import time

def statistics(b):
    b=b[0]
    sim=efficiency.simple()
    th=(len(sim)//3)*2
    for i in range(len(b)):
        if b[i] in sim[th:]:
            d=sim.index(b[i]+6)
            d=sim[d]
            b[i]=b[d]
    return b


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

def Local_Search(a):
    pickle_in=open(info.sub_path, 'rb')
    items, _=pickle.load(pickle_in)

    v=a[0][0]
    m=change(a, v, len(items))
    for i in range(len(a[0])):
        g=change(a, a[0][i], len(items))
        if g[1]>=m[1]:m=g
    return g

def LS():


    pickle_in=open(info.sol_path, 'rb')
    popu=pickle.load(pickle_in)

    #popu=popu[:6]



    start=time.time()
    y_eff=[]
    y_sim=[]
    t_eff=[]
    t_sim=[]
    for i in range(0, len(popu), 2):
        start=time.time()
        a=Local_Search(popu[i])
        b=Local_Search(popu[i+1])
        y_sim.append(a[1])
        y_sim.append(b[1])
        end=time.time()
        t=end-start
        t_sim.append(round(t, 2))

        #print(fr'a={popu[i][1]}=>{a[1]} b={popu[i+1][1]}=>{b[1]}, time={round(end-start, 1)}')
        start=time.time()
        a, b=operation.local_search(popu[i][0], popu[i+1][0])
        y_eff.append(a[1])
        y_eff.append(b[1])
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
    x=np.array(x)
    plt.plot(x, y, color='b', label='original values')
    plt.plot(x, y_sim, color='r', label='simple method for Local Search')
    plt.plot(x, y_eff, color='y', label='efficiency method for local search')
    plt.legend(loc='lower left')


    xx=[]
    for i in range(len(x)//2):
        xx.append(i)
    plt.subplot(1, 2, 2)
    print(t_sim)
    print(t_eff)
    t_sim=np.array(t_sim)
    t_eff=np.array(t_eff)
    plt.plot(xx, t_sim, color='r', label='running time for simple method')
    plt.plot(xx, t_eff, color='y', label='running time for efficiency method')





    plt.xlabel('solutions')
    plt.ylabel('fitness value')
    plt.title('values')
    plt.show()

def main():
    LS()
main()