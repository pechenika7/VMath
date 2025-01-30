from math import sqrt

class First():
    def __init__(self, list_):
        self.a = list_[0]
        self.b = list_[1]
        self.c = list_[2]

class Counting(First):

    def __init__(self, list_):
        super().__init__(list_)

    @classmethod
    def Discr(cls, a, b, c):
        return b ** 2 - 4 * a * c

    def SolveEqu(self):
        D = Counting.Discr(self.a, self.b, self.c)
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

class CountingGeron(First):

    def __init__(self, list_):
        super().__init__(list_)

    @classmethod
    def SemiPerimeter(cls, a, b, c):
        return (a + b +c)/2

    def CalcSqu(self):
        p = CountingGeron.SemiPerimeter(self.a, self.b, self.c)
        try:
            self.squ = sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        except:
            print('Problem with negative root: ', str(self.a), str(self.b), str(self.c))
            self.squ = None
        return self.squ



def Solve(list_params):
    s_dict = dict()
    res = list()
    for i in list_params:
        g = s_dict.get(i)
        if g is None:
            t = Counting(i)
            roots = t.SolveEqu()
            s_dict[i] = roots
        else:
            roots = s_dict[i]
        res.append(roots)
    return res

def SolveGeron(list_params):
    s_dict = dict()
    res = list()
    for i in list_params:
        g = s_dict.get(i)
        if g is None:
            t = CountingGeron(i)
            squ = t.CalcSqu()
            s_dict[i] = squ
        else:
            squ = s_dict[i]
        res.append(squ)
    return res