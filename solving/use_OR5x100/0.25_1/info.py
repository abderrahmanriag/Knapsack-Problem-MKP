import pickle
from random import choice

import efficiency
import greedy
import my_approach as o
import comparison as c
import time
import efficiency as eff
import greedy

sol_path='sol.pickle'
sub_path='sub.pickle'
max_path='cMAX.pickle'
coor_path='coor51251.pickle'
ben_path=r'C:\Users\lenovo\PycharmProjects\Knapsack Problem\benchmark\chubeas\OR5x100\OR5x100-0.25_1.dat'

def v():
    pickle_in=open(sub_path, 'rb')
    subject=pickle.load(pickle_in)
    sim=eff.simple(subject[0])
    sc=eff.scaled(subject)
    same=True
    for i in range(len(sim)):
        if sim[i]!=sc[i]:
            same=False
            break
    print(fr'same={same}')

def sta():
    #greedy.greedy(sub_path, sol_path)

    with open(sol_path, 'rb') as f:
        popu=pickle.load(f)

    with open(sub_path, 'rb') as f:
        subject=pickle.load(f)

    s=c.statistics(popu[0], subject)
    print(popu[0][1])
    for i in range(len(s)):
        print(fr's={s[i]}, len s={len(s[i])}')
    s=c.statistics(popu[-1], subject)
    print(popu[-1][1])
    for i in range(len(s)):
        print(fr's={s[i]}, len s={len(s[i])}')

    print(len(popu))
def main():
    c.main(sub_path, sol_path, max_path)
main()