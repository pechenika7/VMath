def MyFunc(x):
    return x

def BiggerRoot(list_roots, f = max, g = MyFunc):
    res = list()
    for i in list_roots:
        try:
            item = f(g(i[0]), g(i[1]))
        except:
            item = None
        finally:
            res.append(item)
    return res