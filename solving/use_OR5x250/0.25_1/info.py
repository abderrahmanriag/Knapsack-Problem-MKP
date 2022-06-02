import my_approach as o
import create_subject as cs
import comparison as c
import time

sol_path = 'sol.pickle'
sub_path = 'sub.pickle'
max_path = 'sMAX.pickle'
coor_path = 'coor51251.pickle'
ben_path = r'C:\Users\lenovo\PycharmProjects\Knapsack Problem\benchmark\chubeas\OR5x250\OR5x250-0.25_1.dat'


def main():
    print(time.ctime(time.time()))
    #cs.main(ben_path, sub_path)
    c.main(sub_path, sol_path, max_path)

main()