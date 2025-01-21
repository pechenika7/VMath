from random import randint
f = open('data.inp', 'w')
for i in range(10000):
    item = str(randint(-500, 500)) + ' ' + str(randint(-500, 500)) + ' ' + str(randint(-500, 500)) + '\n'
    f.write(item)
f.close()