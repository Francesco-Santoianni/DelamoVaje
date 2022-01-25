class ExamException(Exception):
    pass

class MovingAverage(): 

    def __init__ (self, window_number):
        self.window_number = window_number

        if type(self.window_number) == str:
            raise ExamException('La lunghezza della finestra non può essere una stringa')

        if self.window_number == None:
            raise ExamException('La finestra non può essere None')
        if self.window_number <= 0:
            raise ExamException('La lunghezza della finestra non può essere uguale a zero o negativa')
        
        if self.window_number == None:
            raise ExamException ('La lunghezza della finestra non può essere None')
        
        if type(self.window_number) == float:
            raise ExamException('La lunghezza della finestra non può essere float')
    
    
    def compute (self,numbers):
        self.numbers = numbers
        moving_averages=[]
        i= 0 

        if numbers== None:
            raise ExamException('La lista non può essere None ')

        if not type(self.numbers) == list:
            raise ExamException('La lista deve essere una lista')

        if len(numbers)<self.window_number:
            raise ExamException("La finestra deve essere minore o uguale al numero di elementi della lista")
        

        if type(numbers) ==str: 
            raise ExamException('La lista non può contenere una stringa')
        
        if len(numbers) == 0:
            raise ExamException('la lista non può non avere elementi')
        
        if not all(isinstance(x, float) or isinstance(x, int) for x in numbers):
            raise ExamException ('La lista deve contenere solo numeri')

        if len(numbers) == 0:
            raise ExamException ('deve esserci scritto un numero maggiore di zero nella lista')
        
        

        
####################Ecco il programma!###################       
        
        
        while i< len(numbers) - self.window_number+1:

            window = numbers[i : i + self.window_number]
            window_average = ((sum(window) / self.window_number))
            moving_averages.append(window_average)
            i = i+1

        
        return moving_averages

try:

    moving_average = MovingAverage(2)
    result = moving_average.compute([2,4,8,16])
    print(result)

except TypeError:
    raise ExamException('La lista deve essere una serie di numeri, non può essere vuota')

except NameError:
    raise ExamException ('La lunghezza della finestra deve essere un numero intero')