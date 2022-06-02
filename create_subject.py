import pickle
from knapsack import *
from object import *

def open_file(benchmark_path):
    #open the benchmark file
    #define the path where the file is located
    melef=open(benchmark_path,"r")    #r for read
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
    if(cap[-1]=='\n' or cap[-1]==' '):cap.pop(-1)
    return cap

def miniList(item):
    mm=[]
    for i in range(len(item[0])):
        l=[]
        for j in range(len(item)):
           l.append(item[j][i])
        mm.append(l)
    return mm

def setItems(lines, n):
    # Create a dims list for saving the dimensions info
    dims=[]
    d=[]
    m=1
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            d.append(lines[i][j])
            m+=1
            #print(fr'd={d}, m={m}')
        if m==int(n)+1:
            dims.append(d)
            d=[]
            m=1
    ml=miniList(dims)
    items=[]
    for i in range(len(ml)):
        resource=ml[i]
        value=resource[0]
        resource.remove(value)
        ii=item(resource, value)
        items.append(ii)
    return items

def setKNAPSACK(lines):
    length=lines[0][1]
    cap=[]
    c=0
    n=len(lines)-1
    while c!=int(length):
        if '' in lines[n]:lines[n].remove('')
        print(fr'lines={lines[n]}, length={length}, c={c}, n={n}')
        cap=lines[n]+cap
        c=c+len(lines[n])
        lines[n]=''
        n-=1

    n=len(lines)-1
    for i in range(len(lines)):
        if lines[n]=='':
            lines.remove(lines[n])
        else:
            break
        n-=1

    return cap, lines

def main(benchmark_path, sub_path):
    #Get the lines of the this file using the function open_file()
    f=open_file(benchmark_path)
    #Convert the lises taht inside "f" into lists
    lines=[]
    for i in range(len(f)):
        lines.append(to_list(f[i]))

    # Get the knapsack's info and create an instance
    cap, lines=setKNAPSACK(lines)
    k = knapsack(cap)
    print(fr'cap={k.capacities}')

    # Get the benchmark info "number of items, dimensions
    ben=lines[0]
    nbr_items=ben[0]

    # Remove the benchmark info form the lines list
    lines.remove(ben)

    # The rest numbers in lines are the items info
    # Create items list
    items=setItems(lines, nbr_items)

    # Save the subject in pickle file
    pickle_out=open(sub_path, 'wb')
    pickle.dump([items, k], pickle_out)


