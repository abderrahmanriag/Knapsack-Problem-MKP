import pickle
import greedy
import create_subject as subject
import comparison as c
import comp_new as cn
import time

import greedy

sol_path='sol.pickle'
sub_path='sub.pickle'
max_path='sMAX.pickle'
coor_path='coor51251.pickle'
ben_path=r'C:\Users\lenovo\PycharmProjects\Knapsack Problem\benchmark\chubeas\OR5x500\OR5x500-0.25_1.dat'

def verify():
    pickle_in=open(sol_path, 'rb')
    population=pickle.load(pickle_in)

    pickle_in=open(sub_path, 'rb')
    subject=pickle.load(pickle_in)

    b=greedy.BestAndBad(population)
    print(fr'best={b}')
    greedy.informations(b, subject)

    b=b[0]

    s=[]
    for i in range(len(b)):
        if b[i] not in s:
            s.append(b[i])
    print(fr'len b={len(b)}, len s={len(s)}')

def main():
    print(time.ctime(time.time()))
    #subject.main(ben_path, sub_path)
    c.main(sub_path, sol_path, max_path)


main()