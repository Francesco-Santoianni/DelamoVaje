

class ExamException(Exception):
    pass

class CSVTimeSeriesFile:

    def __init__(self,name):
        self.name = name
        

    def get_data(self):
        
        values = []
        with open(self.name) as x:
            for line in x:
                
                lista_aerei= line.strip().split(',')
                if (lista_aerei[0] != 'date'):
                    lista_aerei[1] = int(lista_aerei[1])
                    values.append(lista_aerei)
                    
        return values
    
    
time_series_file = CSVTimeSeriesFile(name='data.csv')
time_series = time_series_file.get_data()
print(time_series_file.name)
print(time_series)
        
        