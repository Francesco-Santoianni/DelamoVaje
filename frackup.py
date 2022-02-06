#backup
class ExamException(Exception):
    pass

class CSVTimeSeriesFile:

    def __init__(self, name):
        self.name = name

    def get_data(self):
        lista1 = []
        with open(self.name) as x:
            for line in x:
                lista2 = line.strip().split(',')
                if (lista2[0] == 'date'):
                    continue
                lista2[1] = int(lista2[1])
                lista1.append(lista2)
        return lista1

time_series_file = CSVTimeSeriesFile(name='data.csv')
time_series = time_series_file.get_data()

def compute_avg_monthly_difference(time_series, first_year, last_year):
    first_year = int(first_year)
    last_year = int(last_year)
    lista_di_liste = []
    with open('data.csv') as x:
        for line in x:
                #divido gli elementi per ',' e per '-'
                lista_raw = line.strip().split(',')
                lista_raw[0] = lista_raw[0].split('-')
                if (lista_raw[0][0] == 'date'):
                    continue
                #converto l'anno in int
                lista_raw[0][0] = int(lista_raw[0][0])
                #converto i passengers in int
                lista_raw[1] = int(lista_raw[1])

                #aggiungo solo gli elementi che mi servono(anno e passengers)
                lista_raffinata = []
                lista_raffinata.append(lista_raw[0][0])
                lista_raffinata.append(lista_raw[1])
                #aggiungo la lista con gli elementi necessari alla lista finale
                lista_di_liste.append(lista_raffinata)

        #return lista_di_liste
   
    lista_scarsa = []
    matrice_mesi = [ [],[],[],[],[],[],[],[],[],[],[],[] ]
        
    y = 0
    for i in range(first_year, last_year+1):
        if(lista_di_liste[y][0]==i):
            for j in range(0, 12):
                lista_scarsa.append(lista_di_liste[y][1])
                y+=1

    
    contatore_mesi = 0  
    for item in lista_scarsa:
        matrice_mesi[contatore_mesi].append(item)
        if(contatore_mesi==11):
            contatore_mesi=0
        else:
            contatore_mesi+=1
    
    incremento_medio = [  ] 
    contatore_matrice = 0   
    while(contatore_matrice<12):
        incremento = 0
        incremento = (matrice_mesi[contatore_matrice][-1]-matrice_mesi[contatore_matrice][0])/2        
        incremento_medio.append(incremento)
        contatore_matrice+=1
        
    return incremento_medio


print(compute_avg_monthly_difference(time_series, '1949', '1960'))