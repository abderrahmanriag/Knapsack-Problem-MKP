import pickle
from random import choice, randint
import matplotlib.pyplot as plt
import numpy as np
import greedy
import try_methods
import operation as o
import info
import efficiency
import time
import Local_Search as nm
import create_subject
import GGAvsGA as g

def statistics(b):
    b=b[0]
    sim=efficiency.simple()
    th=(len(sim)//3)*2
    for i in range(len(b)):
        if b[i] in sim[th:]:
            d=sim.index(b[i]+6)
            d=sim[d]
            b[i]=b[d]
    return b

def main():
    o.main()


main()