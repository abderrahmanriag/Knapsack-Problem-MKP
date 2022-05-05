def Hill_climbing(a: Genome)->Genome:
    sim=eff.simple()
    th=len(sim)//3
    th=sim[th:]
    f=[]
    for i in range(len(a)):
        if a[i] in th:
            f.append(a[i])
    for i in range(len(f)):
        a.remove(f[i])
    for i in range(len(sim)):
        if sim[i] not in a:
            a.append(sim[i])
            value=greedy.fitness(a)
            if value==0:
                a.remove(sim[i])
    return [a, greedy.fitness(a)]

def local_search(a: Genome, b: Genome)->Population:
    a=Hill_climbing(a)
    b=Hill_climbing(b)
    return [a, b]
