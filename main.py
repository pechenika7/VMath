from time import time
import datetime
from reading import ReadFile
from countingclass import Solve
from thebiggest import BiggerRoot

def my_funct(x, y):
    return 2*x + 2*y

time1 = time()

print(datetime.datetime.now().strftime('%d/%m/%Y')+ ' Starting')#вывод даты

path ='data.inp'
list_params = ReadFile(path)
print(list_params)

list_roots = Solve(list_params)
print(list_roots)

print(BiggerRoot(list_roots, my_funct))

print('Finish, ', time()-time1)