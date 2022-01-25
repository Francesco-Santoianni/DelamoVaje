class ExamException(Exception):
    pass

class Diff():
    def __init__(self, ratio=1):
        self.ratio = ratio
        if ratio == None:
            raise ExamException ('Errore: il ratio non può essere None!')
        if type(ratio) == str:
            raise ExamException ('Errore: il ratio non può essere una stringa!')
        if ratio<=0:
            raise ExamException ('Errore: il ratio non può essere minore di 1!')
 
    def compute(self, lista):
        self.lista = lista
        
        if self.lista == None:
            raise ExamException ('Errore: la lista non può essere None!')
        if not type(self.lista) == list:
            raise ExamException ('Errore: devi inserire una lista!')
        if self.ratio<=0:
            raise ExamException ('Errore: il ratio non può essere minore di 1!')
        if len(self.lista)<=1:
            raise ExamException ('Errore: la lista deve contenere almeno due elementi!')
        if not all(isinstance(x, float) or isinstance(x, int) for x in lista):
            raise ExamException ('Errore: tutti gli elementi devono essere dei numeri!')
        
        lista_finale = []
        numero_precedente = 0
        contatore = 0

        while(contatore<len(lista)):
            
            differenza = self.lista[contatore] - numero_precedente
            differenza_ratio = differenza/self.ratio
            lista_finale.append(differenza_ratio)
            numero_precedente = self.lista[contatore]
            contatore+=1

        return lista_finale[1:]

diff = Diff(1) 
risultato = diff.compute([2,4,8,16])
print(risultato)