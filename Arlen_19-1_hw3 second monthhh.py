
def gcd(num, denom):
    while num % denom != 0:
        num, denom = denom, num % denom
    return denom


class Fraction:

    def __init__(self, num, denom):
        self.num = num
        self.denom = denom

    def __str__(self):
        return str(self.num) + '/' + str(self.denom)

    def __add__(self, other):
        newnum = self.num * other.denom + other.num * self.denom
        newdenom = self.denom * other.denom
        common = gcd(newnum, newdenom)
        return Fraction(newnum // common, newdenom // common)

    def __sub__(self, other):
        newnum = self.num * other.denom - other.num * self.denom
        newdenom = self.denom * other.denom
        common = gcd(newnum, newdenom)
        return Fraction(newnum // common, newdenom // common)

    def __mul__(self, other):
        newnum = self.num * other.num
        newdenom = self.denom * other.denom
        common = gcd(newnum, newdenom)
        return Fraction(newnum // common, newdenom // common)




f1 = Fraction(11, 6)
f2 = Fraction(2, 9)
print(f1 + f2)  # Ответ 37/18
print(f1 - f2)  # Ответ 29/18
print(f1 * f2)  # Ответ 11/27
