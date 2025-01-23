from math import sqrt

class counting():

    def __init__(self, list_):
        self.a = list_[0]
        self.b = list_[1]
        self.c = list_[2]

    @classmethod
    def Discr(cls, a, b, c):
        return b ** 2 - 4 * a * c

    def SolveEqu(self):
        D = counting.Discr(self.a, self.b, self.c)
        self.roots = list()
        if D > 0:
            try:
                self.roots = (((-self.b + sqrt(D)) / (2 * self.a)), ((-self.b - sqrt(D)) / (2 * self.a)))
            except:
                print('Problem with zero division: ', str(self.a))
                self.roots = (None, None)
        elif D == 0:
            try:
                self.roots = ((-self.b / 2 * self.a), (-self.b / 2 * self.a))
            except:
                print('Problem with zero division: ', str(self.a))
                self.roots = (None, None)
        elif D < 0:
            self.roots = (None, None)
        return self.roots



def Solve(list_params):
    s_dict = dict()
    res = list()
    for i in list_params:
        g = s_dict.get(i)
        if g == None:
            t = counting(i)
            roots = t.SolveEqu()
            s_dict[i] = roots
        else:
            roots = s_dict[i]
        res.append(roots)
    return res