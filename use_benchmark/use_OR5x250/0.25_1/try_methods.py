import pickle
import info
def main():
    pickle_in=open(info.sub_path, 'rb')
    items, k=pickle.load(pickle_in)

    for i in range(len(items)):
        print(fr'{items[i].resource}#{items[i].value}')
    print(len(items))
    print(k.capacities)