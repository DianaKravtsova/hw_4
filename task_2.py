from math import  *

class Leibniz:
    def __iter__(self):
        return self

    def __init__(self, SUM):
        self.n = 1
        self.sum = SUM
        self.sum0 = 0
        self.sum_leib = (-pow(1,self.n)) / (2*self.n + 1)
        self.i = 1


    def __next__(self):

        if round(fabs(self.sum0 - self.sum), 2) > 0.01:
            self.sum0 += self.i
            self.i = self.sum_leib
            self.n += 1
            self.sum_leib = (pow(-1, self.n)) / (2 * self.n + 1)
            return self.i
        else:
            raise StopIteration



sum = float(input("Ожидаемая сумма:", ))
print("Полученный ряд:")
row = Leibniz(sum)
for i in row:
    print(i)

