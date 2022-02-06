class ExamException(Exception):
    pass

class Diff():
    def __init__(self, ratio=1):
        self.ratio = ratio

        if self.ratio == None:
            raise ExamException('Il ratio non può essere None, sciocchino')

        if type(self.ratio) == str:
            raise ExamException('Il ratio non può essere una stringa, sciocchino')

        if self.ratio == 0:
            raise ExamException ('Il ratio non può essere zero')

        if self.ratio < 0:
            raise ExamException ('Il ratio non può essere minore di zero')

    def compute (self, lista):
        self.lista = lista
        diff_lista2 = []
        prev_number=0

        if self.lista == 0:
            raise ExamException('La lista non può essere zero')

        if self.lista == None:
            raise ExamException ('La lista non può essere None')
        
        if type(self.lista)== str:
            raise ExamException('La lista non può essere una stringa')

        if not type(self.lista) == list:
            raise ExamException ('La lista deve essere una lista')

        if len(lista) == 1:
            raise ExamException('La lista deve contenere almeno due elementi')

        if len(lista) == 0:
            raise ExamException('La lista non può essere vuota')

        if not all(isinstance(i,int) or isinstance(i,float) for i in lista):
            raise ExamException('Gli elementi della lista non possono essere stringhe')

        for i in range(1, len(lista)):

            diff_lista =lista[i] - lista [i-1]/self.ratio
            diff_lista2.append(diff_lista)
            i+=1
        
        return diff_lista2 
        
diff = Diff(1)
result =  diff.compute([2,4,8,16,32,64])   
print(result)




