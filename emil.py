class ExamException(Exception):
    pass

#In questa classe definisco self.name, dove 
class CSVTimeSeriesFile:

    def __init__(self,name):
        self.name = name
        
        if self.name == None:
            raise ExamException('Nessun file inserito, inserisci il file data.csv ')

        if self.name == '':
            raise ExamException('File non presente, inserisci data.csv')

        if (type(self.name) != str):
            raise ExamException('Il file deve essere in formato stringa')
        
        if self.name != 'data.csv':
            raise ExamException('Il file deve essere la lista di passeggeri su linee aeree internazionali per ogni mese dal 1949 al 1960, ovvero data.csv')

        
    def get_data(self):

        self.can_read = True
        try:
            my_file = open(self.name, 'r')
            my_file.readline()
        except Exception as e:
            self.can_read = False
            print('Errore in apertura del file: "{}"'.format(e))
        

        values = []
        with open(self.name) as x:
            for line in x:
                
                lista_aerei= line.strip().split(',')
                if (lista_aerei[0] != 'date'):
                    try:
                        lista_aerei[1] = int(lista_aerei[1])
                    except:
                        pass
                    values.append(lista_aerei)
                    
        return values
    

time_series_file = CSVTimeSeriesFile(name= 'data.csv')
time_series = time_series_file.get_data()


def compute_avg_monthly_difference(time_series, first_year, last_year):
    matrice= []

    if (type(first_year) != str or type(last_year) != str):
        raise ExamException('GLi anni devono essere in formato stringa')
    
    if last_year == first_year:
        raise ExamException('Il primo e l\'ultimo anno devono essere diversi')

    #provo a convertire gli anni in interi, con un metodo try\except  
    try:
        first_year= int(first_year)
        last_year= int(last_year)
    except:
        pass
    

    if  last_year < first_year:
        raise ExamException("Il primo anno dev'essere minore dell\'ultimo")

    for i in range(last_year-first_year+1):
        matrice.append([])
        

        for j in range(12):
            matrice[i].append([None])

    for elemento in time_series:
        elemento[0]= elemento[0].split('-')
        elemento[0][1] = int(elemento[0][1])
        elemento[0][0] = int(elemento[0][0])


        if (elemento[0][0]>= first_year and elemento[0][0]<=last_year):
            matrice[elemento[0][0]-first_year][elemento[0][1]-1]= elemento[1]

    #Adesso, finalmente, faremo la time time series
    M= matrice
    
    variazione_mesi= 0
    lista_variazione_mesi= []
    
    for j in range(12):
        somma_mesi= 0
        for i in range(last_year-first_year):
            somma_mesi+= (M[i+1][j]-M[i][j])
        
        
        variazione_mesi= somma_mesi/(last_year-first_year)
        lista_variazione_mesi.append(variazione_mesi)
        
            
        
    return lista_variazione_mesi


avg_difference = compute_avg_monthly_difference(time_series, '1949', '1951')
print(avg_difference)
