class ExamException(Exception):
    pass

class MovingAverage():
    def __init__(self, lunghezza_finestra):
        self.lunghezza_finestra = lunghezza_finestra
        if not type(self.lunghezza_finestra) == int:
            raise ExamException("Errore: la finestra deve essere un numero intero, non una stringa!")
        if self.lunghezza_finestra<=0:
            raise ExamException("Errore: la finestra non deve essere uguale o minore di 0!") 

    def compute(self, data):
        self.data = data
        i=0
        lista_media_mobile=[]

        if data == None:
            raise ExamException("Errore: la lista non può essere None!")
        if not type(data) == list:
            raise ExamException("Errore: la lista deve essere di tipo list!")
        if not (type(self.lunghezza_finestra))== int:
            raise ExamException("Errore: tutti i valori devono essere numeri interi!")
        if not all(isinstance(x, int) or isinstance(x, float) for x in self.data):
            raise ExamException("Errore: la lista deve contere solo numeri interi!")
        if len(data)<self.lunghezza_finestra:
            raise ExamException("Errore: la finestra deve essere minore o uguale al numero di elementi nella lista!")
        if len(data)<=0:
            raise ExamException("Errore: la lista deve contenere almeno un elemento!")


        while i < len(data) - self.lunghezza_finestra+1:

            finestra = data[i:i+self.lunghezza_finestra]

            media_mobile = sum(finestra)/self.lunghezza_finestra

            lista_media_mobile.append(media_mobile)

            i = i+1
        return lista_media_mobile

try:
    moving_average = MovingAverage(4)
    result = moving_average.compute([2,4,8,16,32])
    print(result)
except NameError:
    raise ExamException("Errore: la finestra deve essere un numero intero!")
except TypeError:
    raise ExamException("Errore: la finestra non può essere vuota!")

    