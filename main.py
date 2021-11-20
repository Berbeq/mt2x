from math import sqrt

class mt2x:
        def __init__(self, a, b, c):
            self.a = int(a)
            self.b = int(b)
            self.c = int(c)

        def der(self):
            ax = self.a * 2
            print(f"Orginal: {self.a}x^2 + {self.b}x + {self.c}")
            print(f"Deriverad: {ax}x + {self.b}")

        def noll(self):
            an = self.a
            bn = self.b
            cn = self.c
            if self.a/self.a != 1:
                an = self.a / self.a
                bn = self.b / self.a
                cn = self.c / self.a
            if an <= 0:
                an = an*-1
                bn = bn*-1
                cn = cn*-1

            try:
                n1 = -1*bn/2 + sqrt(((bn/2)**2) - cn)
            except:
                n1 = "Finns ej"
            try:
                n2 = -1*bn/2 - sqrt(((bn/2)**2) - cn)
            except:
                n2 = "Finns ej"
            

            print("Nollställe 1: " + str(n1))
            print("Nollställe 2: " + str(n2))









if __name__ == "__main__":
    v = mt2x(input("a term:"), input("b term:"), input("c term:"))
    print("der, noll")
    val = input("")
    if val == "der":
        v.der()
    if val == "noll":
        v.noll()