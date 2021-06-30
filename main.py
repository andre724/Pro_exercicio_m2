class fibonacci():
    def __init__(self,termos):
        self.quant_termos= termos
        self.before = 0
        self.after = 1
    def __iter__(self):
        self.after= 0
    
    def __next__(self):
        if self.quant_termos <=0:
            return 0
        elif self.quant_termos == 1:
            print('Primeiro termo da sequencia é ', self.quant_termos, ':' )
        else:
            fibo_sqcia=[]
            for i in range(0, self.quant_termos):
                fibo_sqcia.append(self.before)
                aux = self.before + self.after
                self.before = self.after
                self.after  = aux
               
                print(fibo_sqcia[i])

   


f1= fibonacci(15)

f2= fibonacci(10)

next(f1)
