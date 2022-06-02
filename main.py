import greedy
import pickle
import create_subject as sub
import my_approach as o

def verify_duplicate():
    sub.main()
    greedy.greedy()
    pickle_in=open(info.sol_path, 'rb')
    population=pickle.load(pickle_in)

    values=[]
    zero=[]
    for i in range(len(population)):
        if population[i][1]==0:zero.append(0)
        else:values.append(population[i][1])

    values=sorted(set(values))

    if len(values)<len(population):
        print(fr'len values={len(values)}, len zero={len(zero)}, len popu={len(population)}')
        print(fr'size={len(population)-len(values)}')

    c=0
    for i in range(len(population)):
        if population[i][1]==0:c+=1


def main():
    o.main()

main()