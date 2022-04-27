import pickle
import time
from random import choices, randint, choice, random, randrange
from typing import List
import info
import greedy

Genome=List[int]
Population=List[Genome]

def tournament(population, tour)->[Population, Population]:
    #the winners of the tournament will be the candidates of the operation
    winners=[]
    rest=[]
    for i in range(len(population)//tour):
        tour_list=[]
        for j in range(tour):
            r=choice(population)
            population.remove(r)
            tour_list.append(r)
        b=greedy.BestAndWorst(tour_list)
        winners.append(b)
        tour_list.remove(b)
        for j in range(len(tour_list)):
            rest.append(tour_list[j])
    return  winners, rest

def selection_pair(population)->Population:
    return choices(
        population,
        k=2
    )

def single_point_crossover(a: Genome, b: Genome)->[Population, Population]:
    length=len(b)
    p=randint(0, length-1)
    c=a[0:p]+b[p:]
    d=b[0:p]+a[p:]
    return [c, greedy.fitness(c)], [d, greedy.fitness(d)]

def mutation(genome:Genome, probability:float=0.5)->Genome:
    index=randrange(len(genome))
    if random()<probability:
        r=randint(0, 1)
        if r==1:
            n=randint(0, 99)
            if n not in genome:
                genome.append(n)
    return genome

def operation(population:Population, pc:int, pm:int):
    #population size ps=length of the population
    ps=len(population)

    print(fr'crossover probability={pc}, mutation probability={pm}')
    print('population size "ps"=', ps, '\ncrossover probability "pc"=', pc)
    #Crossover
    #get the cand number accourding the crossover probability
    #cand=pc*ps
    cand=pc*ps
    print('nbr of cand=', cand)

    #tournament size=ps/cand
    tour=ps/cand
    print('tour=', tour)

    winners, population=tournament(population, int(tour))

    #Create a list for saving new generation
    offspring=[]

    for i in range(100):
        a, b=selection_pair(winners)
        a=a[0]
        b=b[0]
        length=min(len(a), len(b))
        done=False
        if len(b)==length:
            offspring+=single_point_crossover(a, b)
            done=True
        if len(a)==length and done==False:
            offspring+=single_point_crossover(b, a)

    #Mutation
    #Get the number of cand according the mutation probability
    #cand=pm*ps
    #Update the mutation probability
    pm=pm+(pc/2)
    pm=round(pm, 2)
    print(fr'Update pm={pm}')
    cand=pm*len(population)
    candidates=[]
    for _ in range(int(cand)):
        r=choice(population)
        candidates.append(r)
        population.remove(r)

    for i in range(len(candidates)):
        c=candidates[i]
        m=mutation(c)
        if m==c:offspring.append(m)
        else:
            offspring.append([m, greedy.fitness(m)])

    offspring=offspring+population

    b=greedy.BestAndWorst(offspring)
    print(fr'b={b[1]}')
    print(fr'Population size={len(population)}')







def main():
    #Load the population list
    pickle_in=open(info.sol_path, 'rb')
    population=pickle.load(pickle_in)

    #Crossover probability "pc"->
    #The probability of choosing some solutions to be candidates to the crossover func
    pc=0.2
    pm=0.7
    operation(population, pc, pm)


start=time.time()
main()
end=time.time()
print(fr'running time={end-start}')
