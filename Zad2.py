class Potegi:
    def __init__(self, a, n):
        self.a = a
        self.n = n
        self.current_exponent = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_exponent < self.n:
            result = self.a ** self.current_exponent
            self.current_exponent += 1
            return result
        else:
            raise StopIteration

 
gen = Potegi(5, 5) #5^5
for p in gen:
    print(p) 