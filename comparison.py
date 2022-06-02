import pickle
import time
from matplotlib import pyplot as plt
import efficiency
import greedy
import my_approach as o
import GA as ga

def statistics(b, subject):
    b=b[0]
    sim=efficiency.scaled(subject)
    #print(fr'scaled={sim}, len sc={len(sim)}')
    th=len(sim)//3
    tth=th*2
    s=[[], [], []]
    for i in range(len(b)):
        if b[i] in sim[:th]:s[0].append(sim.index(b[i]))
        if b[i] in sim[th:tth]:s[1].append(sim.index(b[i]))
        if b[i] in sim[tth:]:s[2].append(sim.index(b[i]))
    return s

def main(sub_path, sol_path, max_path):

    #PRINT THE CURRENT TIME
    print(time.ctime(time.time()))

    #CREATE THE INITIAL POPULATION
    population=greedy.greedy(sub_path, sol_path)

    b=greedy.BestAndBad(population)

    my_approach=[b[1]]
    GA=[b[1]]

    g=500   #NUMBER OF GENERATIONS

    pc=0.2  #CROSSOVER PROBABILITY

    start = time.time()
    print(fr'crossover probability pc={pc}, len popu={len(population)}')
    print(fr'build {g} generations...')

    #Load the subject
    with open(sub_path, 'rb') as f:
        subject=pickle.load(f)

    m1, popu1=o.begin(population, pc, g, subject, max_path)
    m2, popu2=ga.begin(population, pc, g, subject)

    my_approach=my_approach+m1
    GA=GA+m2

    b1=greedy.BestAndBad(popu1)
    b2=greedy.BestAndBad(popu2)
    if b1[1]>=b2[1]:
        with open(sol_path, 'wb') as f:
            pickle.dump(popu1, f)
        greedy.informations(b1, subject)
        s = statistics(b1, subject)
        for i in range(len(s)):
            print(fr's={s[i]}, len={len(s[i])}')
    else:
        with open(sol_path, 'wb') as f:
            pickle.dump(popu2, f)
        greedy.informations(b2, subject)
        s = statistics(b2, subject)
        for i in range(len(s)):
            print(fr's={s[i]}, len={len(s[i])}')
    end=time.time()
    print(fr'running time={end-start}')
    x=[]
    for i in range(len(GA)):
        x.append(i)

    plt.plot(x, my_approach, color='b', label=('GGA', [max(my_approach), x[my_approach.index(max(my_approach))]]))
    plt.plot(x, GA, color='r', label=('GA', [max(GA), x[GA.index(max(GA))]]))
    plt.legend(loc='lower center')

    plt.xlabel('generation')
    plt.ylabel('Fitness value')

    plt.title(fr'generate {g} generations in {round(((end-start)//60), 2)} minutes')

    plt.show()




