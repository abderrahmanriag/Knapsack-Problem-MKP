import pickle
import time
from matplotlib import pyplot as plt
import greedy
import my_approach as o
import GA as ga

def main(sub_path, sol_path):

    greedy.greedy(sub_path, sol_path)

    #Load the population
    pickle_in=open(sol_path, 'rb')
    population=pickle.load(pickle_in)

    b=greedy.BestAndBad(population)

    my_approach=[b[1]]
    GA=[b[1]]

    g=500   #NUMBER OF GENERATIONS
    gm=20

    pc=0.2 #CROSSOVER PROBABILITY

    start = time.time()
    print(fr'crossover probability pc={pc}')
    print(fr'build {g} generations...')

    #Load the subject
    pickle_in=open(sub_path, 'rb')
    subject=pickle.load(pickle_in)
    m1, popu1=o.begin(population, pc, gm, subject)
    m2, popu2=ga.begin(population, pc, g, subject)

    my_approach=my_approach+m1
    GA=GA+m2

    pickle_out=open(sol_path, 'wb')
    b1=greedy.BestAndBad(popu1)
    b2=greedy.BestAndBad(popu2)
    if b1[1]>=b2[1]:
        pickle.dump(popu1, pickle_out)
        greedy.informations(b1, subject)
    else:
        pickle.dump(popu2)
        greedy.informations(b2)
    end=time.time()
    x=[]
    for i in range(len(GA)):
        x.append(i)
    xm=[]
    for i in range(len(my_approach)):
        xm.append(i)
    plt.subplot(1, 2, 1)
    plt.plot(xm, my_approach, color='b', label=(pc, [max(my_approach), x[my_approach.index(max(my_approach))]]))
    plt.legend(loc='lower center')


    plt.xlabel('generation')
    plt.ylabel('Fitness value')

    plt.title(fr'generate {gm} generations in {round(((end-start)//60), 2)} minutes')

    plt.subplot(1, 2, 2)
    plt.title(fr'generate {g} generations in {round(((end - start) // 60), 2)} minutes')
    plt.plot(x, GA, color='r', label=(pc, [max(GA), x[GA.index(max(GA))]]))
    plt.legend(loc='lower center')

    plt.xlabel('generation')
    plt.ylabel('Fitness value')

    plt.show()




