import datetime
from reading import read_file
from counting import solve
from thebiggest import bigger_root


print(datetime.datetime.now().strftime('%d/%m/%Y')+ ' Starting')#вывод даты

path ='data.inp'
f = read_file(path)
print(f)

solve()

bigger_root()

print('Finish')