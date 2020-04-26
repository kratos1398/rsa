from rsa import rsa
import sympy
class calculating_d:
    def __init__(self,p,q,e):
        self.p = p
        self.q = q
        self.e = e


    def calculate(self):
        newp = self.p - 1
        newq = self.q - 1
        phi_n = newp*newq
        #d = sympy.mod_inverse(phi_n,self.e)
        d = lambda A, n,s=1,t=0,N=0: (n < 2 and t%N or d(n, A%n, t, s-A//n*t, N or n),-1)[n<1]
        real_d = d(self.e,phi_n)
        return real_d
            
