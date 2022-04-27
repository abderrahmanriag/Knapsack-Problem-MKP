import pickle
from random import choices, randint, randrange, random
from typing import List
import info

Genome=List[int]
Population=List[Genome]

def generate_genome(length:int)->Genome:
    return [randint(0, 99) for _ in range(length)]

def crossover(a:Genome, b:Genome)->[Genome, Genome]:
    length=len(b)
    p=randint(0, length-1)
    print(fr'p={p}')
    return a[0:p]+b[p:], b[0:p]+a[p:]

def mutation(genome:Genome, num:int=1, probability:float=0.5)->Genome:
    index=randrange(len(genome))
    if random()<probability:
        r=randint(0, 1)
        if r==1:
            n=randint(0, 99)
            if n not in genome:
                genome.append(n)
    return genome

def bit(genom:Genome, length:int)->Genome:
    return [(0 if i not in genom else 1)for i in range(length)]

# importing the required module
import matplotlib.pyplot as plt

def curve():
    # x axis values
    x = [1, 2, 3]
    # corresponding y axis values
    y = [2, 4, 1]

    # plotting the points
    plt.plot(x, y)

    # naming the x axis
    plt.xlabel('x - axis')
    # naming the y axis
    plt.ylabel('y - axis')

    # giving a title to my graph
    plt.title('My first graph!')

    # function to show the plot
    plt.show()

def main():
    pickle_in=open(info.sub_path, 'rb')
    items, k=pickle.load(pickle_in)
    for i in range(len(items)):
        print(items[i].resource, '#', items[i].value)

    print(k.capacities)

