from docplex.mp.model import Model
import pickle
import info

def kp():
    KP=Model(name='KP')
    values=[10, 5, 18, 12, 15, 1, 2, 8]
    weights=[4, 2, 5, 4, 5, 1, 3, 5]
    C=15
    N=len(weights)
    x=KP.binary_var_list(N, name='x')
    KP.add_constraint(sum(weights[i]*x[i] for i in range(N))<=C)
    o=sum(values[i]*x[i] for i in range(N))
    KP.set_objective('max', o)
    KP.print_information()
    KP.solve()
    print('Optimization is done, Objective function value: %.2f'% KP.objective_value)
    KP.print_solution()
    print('The values: ', values)
    print('The weights: ', weights)



def multi():
    pickle_in=open(info.sub_path, 'rb')
    items, k=pickle.load(pickle_in)

    valeus=[]
    weights=[]
    for i in range(len(items)):
        valeus.append(items[i].value)
        weights.append(items[i].resource)

    cap=k.capacities
    KP=Model(name='KP')
    N=len(weights)
    x=KP.binary_var_list(N, name='x')
    for j in range(len(cap)):
        print(fr'cap={cap[j]}')
        KP.add_constraint(sum(int(weights[i][j]) * int(x[i]) for i in range(N)) <= cap[j])
    o=sum(valeus[i]*x[i] for i in range(N))
    KP.set_objective('max', o)
    KP.print_information()
    KP.solve()
    print('Optimization is done, Objective function value: %.2f'% KP.objective_value)
    KP.print_solution()
    print('The values: ', valeus)
    print('The weights: ', weights)

multi()