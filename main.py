import datetime
from reading import read_file
from counting import solve
from thebiggest import bigger_root


print(datetime.datetime.now().strftime('%d/%m/%Y')+ ' Starting')#вывод даты

path ='data.inp'
list_params = read_file(path)
print(list_params)

list_roots = solve(list_params)
print(list_roots)

bigger_root()

print('Finish')