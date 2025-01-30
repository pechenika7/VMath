from time import time
import datetime
from reading import ReadFile
from countingclass import Solve, SolveGeron
from thebiggest import BiggerRoot

time1 = time()

print(datetime.datetime.now().strftime('%d/%m/%Y')+ ' Starting')#вывод даты

path ='data2.inp'
list_params = ReadFile(path)
print(list_params)

ans = input('R - roots, G- geron, E-exit')
if ans == 'R':
    list_roots = Solve(list_params)
    print(list_roots)

    print(BiggerRoot(list_roots, max, abs))
elif ans =='G':
    print(SolveGeron(list_params))
elif ans == 'E':
    exit()

print('Finish, ', time()-time1)