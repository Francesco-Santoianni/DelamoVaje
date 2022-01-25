class ExamException(Exception):
    pass

class Diff():
    def __init__(self, ratio=1):
        self.ratio = ratio

        if self.ratio == None:
            raise ExamException('Il ratio non può essere None, sciocchino')

        if type(self.ratio) == str:
            raise ExamException('Il ratio non può essere una stringa, sciocchino')

        if self.ratio == (0):
            raise ExamException ('Il ratio non può essere zero')

        if self.ratio < 0:
            raise ExamException ('Il ratio non può essere minore di zero')

    def compute (self, lista):
        self.lista = lista
        t= 0
        j = lista

        if not all(isinstance(i,int) or isinstance(i,float) for i in lista):
            raise ExamException('Gli elementi della lista non possono essere stringhe')

        if type(lista)== str:
            raise ExamException('La lista non può essere una stringa')

        if not type(lista) == list:
            raise ExamException('la lista deve contenere solo numeri') 

        if self.lista == None:
            raise ExamException ('La lista non può essere None')

        if not type(lista) == list:
            raise ExamException ('La lista deve essere una lista')
  
        if len(lista) == 0:
            raise ExamException('La lista non può essere vuota')

        if len(lista) == 1:
            raise ExamException('La lista deve contenere almeno due elementi')
        
        for i in range(0,len(lista)-1):

            differenza_elementi= [(j[t+1]-j[t-1]/self.ratio
            
        return differenza_elementi
        
diff = Diff(1)
result = diff.compute([2,4,8,16])
print(result)

#stevilka= []
        #t= 0
        #j = lista
        
        #while (t<j):
            #differenza_elementi = []


