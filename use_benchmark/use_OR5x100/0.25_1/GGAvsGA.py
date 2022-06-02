import pickle
import info
import operation
import simple_GA
import greedy
import matplotlib.pyplot as plt
import time

def main():
    start=time.time()
    population=greedy.greedy()

    #define the number of generations
    g=500
    pc=0.2
    print(fr'build {g} generations...')
    print(fr'Camparison the GGA with GA, crossover probability={pc}')

    GA=[]
    GGA=[]

    GA.append(greedy.BestAndBad(population)[1])
    GGA.append(greedy.BestAndBad(population)[1])

    m, population1=operation.begin(population, pc, g)
    GGA=GGA+m
    m, population2=simple_GA.begin(population, pc, g)
    GA=GA+m

    pickle_out=open(info.sol_path, 'wb')
    if max(GGA)>=max(GA):
        pickle.dump(population1, pickle_out)
        greedy.informations(greedy.BestAndBad(population1))
    else:
        pickle.dump(population2, pickle_out)
        greedy.informations(greedy.BestAndBad(population2))

    end=time.time()
    print(fr'running time:{end-start}')

    x=[]
    for i in range(len(GA)):
        x.append(i)

    plt.plot(x, GGA, color='b', label=('GGA', [max(GGA), x[GGA.index(max(GGA))]]))
    plt.plot(x, GA, color='r', label=('GA', [max(GA), x[GA.index(max(GA))]]))
    plt.legend(loc='lower center')

    plt.xlabel('generation')
    plt.ylabel('Fitness value')

    plt.title(fr'generate {g} generations in {round((end-start), 2)} seconds')

    plt.show()




