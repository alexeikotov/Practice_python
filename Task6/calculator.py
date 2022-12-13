class Complex:

    def __init__(self, a, b=0):
        self.r = a
        self.j = b
    
    def __str__(self):
        if self.r >= 0 and self.j >= 0:
            return f"{self.r} + {self.j}*j"
        elif self.r < 0 and self.j >= 0:
            return f"({self.r}) + {self.j}*j"
        elif self.r >= 0 and self.j < 0:
            return f"{self.r} + ({self.j})*j"
        elif self.r < 0 and self.j < 0:
            return f"({self.r}) + ({self.j})*j"

    def __eq__(self, num):
        return self.r == num.r and self.j == num.j

    def add(self, num):
        return Complex(self.r + num.r, self.j + num.j)

    def sub (self, num):
        return Complex(self.r - num.r, self.j - num.j)

    def mul (self, num):
        return Complex(self.r*num.r - self.j*num.j,
         num.r*self.j +self.r*num.j)

    def dev (self,num):
        return Complex((self.j*num.r - self.r*num.j)/(num.r**2 + num.j**2),
        (self.r*num.r + self.j*num.j)/(num.r**2 + num.j**2)) 
    
    def mod (self):
        return (self.r**2+self.j**2)**0.5
