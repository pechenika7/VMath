def BiggerRoot(list_roots, f):
    res = list()
    for i in list_roots:
        try:
            item = f(abs(i[0]), abs(i[1]))
        except:
            item = None
        finally:
            res.append(item)
    return res