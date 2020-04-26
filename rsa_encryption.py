class rsa_encryption:
    def __init__(self,x,e,n):
        self.x = int(x)
        self.e = int(e)
        self.n = int(n)
    def encrypt(self):
        binary_rep = bin(self.e)
        binary_rep = binary_rep.replace("0b","")
        binary_rep = list(binary_rep)
        initial_value = pow(int(self.x),1)
        initial_value = initial_value % self.n
        binary_rep.remove(binary_rep[0])
        recurring_value = initial_value
        for b in binary_rep:   #[hn-1,....h0]
            if b == '0':  #if the processed bit is 0, we only square
                recurring_value = pow(recurring_value,2) % self.n
            elif b == '1': #if the processed bit is 1, we square and then multiply
                recurring_value = pow(recurring_value,2) % self.n
                recurring_value = (recurring_value * self.x) % self.n
        return recurring_value # we return the value once we iterated through every bit
