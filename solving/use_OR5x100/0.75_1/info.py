import my_approach as o
import create_subject as cs

sol_path = 'sol.pickle'
sub_path = 'sub.pickle'
best_path = 'best51251.pickle'
coor_path = 'coor51251.pickle'
ben_path = r'C:\Users\lenovo\PycharmProjects\Knapsack Problem\benchmark\chubeas\OR5x100\OR5x100-0.75_1.dat'


def main():
    #cs.main(ben_path, sub_path)

    o.main(sol_path, sub_path)


main()