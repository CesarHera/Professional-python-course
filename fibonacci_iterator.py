import time

class fiboiter:
    def __init__(self, max=None):
        self.max = max

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.contador = 0
        return self

    def __next__(self):
        if self.contador == 0:
            self.contador += 1
            return f'Fibonacci número {self.contador}: {self.n1}'
        elif self.contador == 1:
            self.contador += 1
            return f'Fibonacci número {self.contador}: {self.n2}'
        else:
            if not self.max or self.contador + 1 <= self.max:
                self.contador += 1
                self.n1, self.n2 = self.n2, self.n1 + self.n2
                return f'Fibonacci número {self.contador}: {self.n2}'
            else:
                raise StopIteration

if __name__ == '__main__':
    # fibonacci = iter(fiboiter(10))
    # while True:
    #     try:
    #         print(next(fibonacci))
    #         time.sleep(0.05)
    #     except StopIteration:
    #         break
    
    for element in fiboiter(100):
        print(element)
        time.sleep(0.001)