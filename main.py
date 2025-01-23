from time import time
import datetime
from reading import ReadFile
from countingclass import Solve
from thebiggest import BiggerRoot

time1 = time()

print(datetime.datetime.now().strftime('%d/%m/%Y')+ ' Starting')#вывод даты

path ='data.inp'
list_params = ReadFile(path)
print(list_params)

list_roots = Solve(list_params)
print(list_roots)

print(BiggerRoot(list_roots, max, abs))

print('Finish, ', time()-time1)