class Tribonachi:
    def __iter__(self):
        return self

    def __init__(self):
        self.one = 0
        print(self.one)
        self.two = 1
        print(self.two)
        self.three = 1
        print(self.three)
        self.four = self.one + self.two + self.three
        print(self.four)
        self.count = 4

    def __next__(self):

        if self.count < 35:
            self.one = self.two
            self.two = self.three
            self.three = self.four
            self.four = self.one + self.two + self.three
            self.count += 1
            return self.four
        else:
            raise StopIteration




trib = Tribonachi()
for i in trib:
    print(i)

