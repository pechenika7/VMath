from math import sqrt

def SolveEqu(equ):
    D = equ[1]**2-4*equ[0]*equ[2]
    roots = list()
    if D > 0:
        roots = (((-equ[1] + sqrt(D)) / (2 * equ[0])), ((-equ[1] - sqrt(D)) / (2 * equ[0])))
    elif D == 0:
        roots = ((-equ[1] / 2 * equ[0]), (-equ[1] / 2 * equ[0]))
    elif D < 0:
        roots = (None, None)
    return roots

def Solve(list_params):
    res = list()
    for i in list_params:
        roots = SolveEqu(i)
        res.append(roots)
    return res