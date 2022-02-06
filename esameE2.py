
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


def compute_avg_monthly_difference(time_series, first_year, last_year):
    Matrice= []
    for i in range(last_year-first_year+1):
            Matrice.append([])
            for j in range(12):
                Matrice[i].append(None)


    return Matrice
        
        
        





avg_difference = compute_avg_monthly_difference(time_series, 1949, 1951)
print(avg_difference)



"""with open('data.csv') as x:
            for line in x:
                lista_aerei2=line.strip().split(',')
                lista_aerei2[0][0]= line.strip().split('-')
                if (lista_aerei2[0] == 'Date'):
                    continue

                    lista_aerei2[0][0] = (lista_aerei2[0][0])
                    lista_aerei2[1]= (lista_aerei2[1])

                    lista_definitiva= []
                    lista_definitiva.append(lista_aerei2[0][0])
                    lista_definitiva.append(lista_aerei2[1]) 
                    Matrice.append(lista_definitiva)
            return Matrice"""













