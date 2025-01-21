def ReadFile(path):
    print('enter', path)

    f = open(path, 'r')
    res = list()
    while True:
        str_ = f.readline()
        if str_ == '' or str_ == '\n':
            print('exit')
            return res
        tri = str_.split()
        for i in range(3):
            tri[i] = int(tri[i])
        res.append(tri)
