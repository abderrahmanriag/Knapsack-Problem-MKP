import my_approach as o
import time
import create_subject as subject
import comparison as c

sol_path=r'C:\Users\lenovo\PycharmProjects\Knapsack-Problem-MKP\solving\use_OR10x100\0.25_1\sol.pickle'
sub_path=r'C:\Users\lenovo\PycharmProjects\Knapsack-Problem-MKP\solving\use_OR10x100\0.25_1\sub.pickle'
ben_path=r'C:\Users\lenovo\PycharmProjects\Knapsack Problem\benchmark\chubeas\OR10x100\OR10x100-0.25_1.dat'

def main():
    print(time.ctime(time.time()))
    #subject.main(ben_path, sub_path)
    c.main(sub_path, sol_path)

main()