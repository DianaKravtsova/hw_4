from math import  *

class Leibniz:
    def __iter__(self):
        return self

    def __init__(self):
        self.n = 1
        self.sum = 1.76
        self.sum0 = 1
        self.sum_leib = (-pow(1,self.n))/ (2*self.n + 1)


    def __next__(self):

        if round(fabs(self.sum - self.sum0), 2) < 0.01:
            self.sum0 += self.sum_leib
            self.n +=1

        else:
            raise StopIteration




row = Leibniz()
for i in row:
    print(i)

