import info
from object import *
from knapsack import *
import pickle

def open_file():
    #open the file which constaints the benchmark
    #define the path where the file is located
    melef=open(info.ben_path,"r")    #r for read
    f=melef.readlines()
    #f is just a lines of numbers that inside this file
    return f

def to_list(a):
    ra8m=0
    cap=[]
    for i in range(1, len(a)):
        if(a[i]==' '):
            cap.append(a[ra8m+1:i])
            ra8m=i
        if(i==len(a)-1):
            cap.append(a[ra8m+1:])
    if(cap[-1]=='\n'):cap.pop(-1)
    return cap
def get_DimList(lst):
    dim=[]
    dims=[]
    for i in range(1, 91, 15):
        for j in range(i, i+15):
            for k in range(len(lst[j])):
                dim.append(lst[j][k])
        dims.append(dim)
        dim=[]
    return dims
def setItems(lst):
    dims=[]
    value=[]
    for i in range(1, len(lst)):
        dims.append(lst[i])
    for i in range(len(lst[1])):
        value.append(lst[0][i])
    items=[]
    for i in range(len(dims[1])):
        l=[]
        for j in range(len(dims)):
            l.append(dims[j][i])
        it=item(l, value[i])
        items.append(it)
    return items

def main():
    item_list=[]
    #Get the lines of the this file using the function open_file()
    f=open_file()
    for i in range(len(f)):
        item_list.append(to_list(f[i]))
    capacities=item_list[-1]
    #to_list is a function which get one line from benchmark
    # "follows" and convert it into a list
    # So we give all the lines of the file to convert the whole file

    dims=get_DimList(item_list)
    #get_DimList(item_list) for organizing those numbers in lists of dimensions and profit
    items=setItems(dims)

    k=knapsack(capacities)
    pickle_out=open(info.sub_path, 'wb')
    pickle.dump([items, k], pickle_out)

    print(capacities)
    print(len(items))

main()

