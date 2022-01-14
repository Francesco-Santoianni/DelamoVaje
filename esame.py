class ExamException(Exception):
    pass

class MovingAverage(): 

    def __init__ (self, window_number):
        self.window_number = window_number
    
    def compute (self,numbers):
        self.numbers = numbers
        moving_averages=[]
        i= 0 

        if not all(isinstance(i,int)for i in numbers):
            raise ExamException ('I valori devono essere numeri interi')

        if len(numbers)<2:
            raise ExamException ('La lista deve avere almeno due elementi')

        if self.window_number>len(numbers) or self.window_number <= 0:
            raise ExamException ('La lunghezza della finestra deve essere compresa tra 1 e il numero di elementi nella lista')

        
        while i< len(numbers) - self.window_number+1:

            window = numbers[i : i + self.window_number]
            window_average = int((sum(window) / self.window_number))
            moving_averages.append(window_average)
            i = i+1

        return moving_averages

try:

    moving_average = MovingAverage(0)
    result = moving_average.compute([2,4,8,16])
    print(result)

except ZeroDivisionError:
    raise ExamException ('Non puoi dividere per zero')

except NameError:
    raise ExamException ('La lunghezza della finestra deve essere un numero intero')

except TypeError:
    raise ExamException ('Lo spazio dove scrivere la lunghezza della finestra non può essere vuoto e non può essere una stringa')








    