#https://docs.google.com/document/d/e/2PACX-1vSsSDmsHj0dsqG3rs1Erv2KGksKCSpk27RAUfrL5p6aaIAIplReUfOnh8NUNP-D6j_uOhF1fhTfd5Hg/pub
#####################################################
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

        if not (type(self.lunghezza_finestra))== int:
            raise ExamException("Errore: tutti i valori devono essere numeri interi!")
        if not all(isinstance(x, int) for x in list(data)):
            raise ExamException("Errore: la lista deve contere solo numeri interi!")
        if len(data)<self.lunghezza_finestra:
            raise ExamException("Errore: la finestra deve essere minore o uguale al numero di elementi nella lista!")
        """if self.lunghezza_finestra==0:
            raise ExamException("Errore: la finestra non deve essere uguale a 0!")"""
        if len(data)==0:
            raise ExamException("Errore: la lista non può essere vuota!")
        if len(data)<2:
            raise ExamException("Errore: la lista deve contenere almeno due elementi!")
            
        i=0
        lista_media_mobile=[]

        while i < len(data) - self.lunghezza_finestra+1:

            finestra = data[i:i+self.lunghezza_finestra]

            media_mobile = int((sum(finestra)/self.lunghezza_finestra))

            lista_media_mobile.append(media_mobile)

            i = i+1
        return lista_media_mobile

####################################################
try:
    moving_average = MovingAverage(2)
    result = moving_average.compute([2,4,8,16])
    print(result)
except NameError:
    raise ExamException("Errore: la finestra deve essere un numero intero!")
except TypeError:
    raise ExamException("Errore: la finestra non può essere vuota!")