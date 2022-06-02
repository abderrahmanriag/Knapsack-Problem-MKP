import my_approach as o
import comparison as c
import create_subject as subject


sol_path='sol.pickle'
sub_path='sub.pickle'
max_path='sMAX.pickle'
coor_path='coor51251.pickle'
ben_path=r'C:\Users\lenovo\PycharmProjects\Knapsack Problem\benchmark\chubeas\OR10x500\OR10x500-0.25_1.dat'

def main():
    #subject.main(ben_path, sub_path)
    c.main(sub_path, sol_path, max_path)


main()