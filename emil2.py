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

def compute_avg_monthly_difference(time_series, primo_anno, ultimo_anno):
    matrice= []
    primo_anno= int(primo_anno)
    ultimo_anno= int(ultimo_anno)

    

    for i in range(ultimo_anno-primo_anno+1):
        matrice.append([])
        

        for j in range(12):
            matrice[i].append([])

    for elemento in time_series:
        elemento[0]= elemento[0].split('-')
        elemento[0][1] = int(elemento[0][1])
        elemento[0][0] = int(elemento[0][0])

        if (elemento[0][0]>= primo_anno and elemento[0][0]<=ultimo_anno):
            matrice[elemento[0][0]-primo_anno][elemento[0][1]-1]= elemento[1]

        
    return matrice


avg_difference = compute_avg_monthly_difference(time_series, '1949', '1951')
print(avg_difference)














