def BiggerRoot(list_roots):
    res = list()
    for i in list_roots:
        try:
            item = max(abs(i[0]), abs(i[1]))
        except:
            item = None
        finally:
            res.append(item)
    return res