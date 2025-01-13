class Frazione:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __add__(self, other):
        num = self.num * other.den + other.num * self.den
        den = self.den * other.den
        return Frazione(num, den)

    def __sub__(self, other):
        num = self.num * other.den - other.num * self.den
        den = self.den * other.den
        return Frazione(num, den)

    def __mul__(self, other):
        num = (self.num * other.num)
        den = (self.den * other.den)
        return Frazione(num, den)
    
    def __str__(self):
        return f"{self.num}/{self.den}"


# Esempio di utilizzo
f1 = Frazione(3, 4)
f2 = Frazione(2, 4)

# Addizione
f3 = f1 + f2
print(f3)  # Output: Frazione(5, 4)

# Sottrazione
f4 = f1 - f2
print(f4)  # Output: Frazione(1, 4)

# Moltiplicazione
f5 = f1 * f2
print(f5)  # Output: Frazione(6, 16)

# Rappresentazione
print(f1)  # Output: Frazione(3, 4)



