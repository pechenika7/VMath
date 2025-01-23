from math import sqrt

def SolveEqu(equ):
    D = equ[1]**2-4*equ[0]*equ[2]
    roots = list()
    if D > 0:
        try:
            roots = (((-equ[1] + sqrt(D)) / (2 * equ[0])), ((-equ[1] - sqrt(D)) / (2 * equ[0])))
        except:
            print('Problem with zero division: ', str(equ[0]))
            roots = (None, None)
    elif D == 0:
        try:
            roots = ((-equ[1] / 2 * equ[0]), (-equ[1] / 2 * equ[0]))
        except:
            print('Problem with zero division: ', str(equ[0]))
            roots = (None, None)
    elif D < 0:
        roots = (None, None)
    return roots

def Solve(list_params):
    s_dict = dict()
    res = list()
    for i in list_params:
        g = s_dict.get(i)
        if g is None:
            roots = SolveEqu(i)
            s_dict[i] = roots
        else:
            roots = s_dict[i]
        res.append(roots)
    return res