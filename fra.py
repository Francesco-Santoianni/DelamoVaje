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
                #skippo la prima linea
                if (lista2[0] == 'date'):
                    continue
                #se per un mese non ci sono info, non lo modifico
                if (lista2[1] != ''):
                    lista2[1] = int(lista2[1])
                lista1.append(lista2)
        return lista1

time_series_file = CSVTimeSeriesFile(name='data.csv')
time_series = time_series_file.get_data()
#Print per vedere get_data()
print('\nVerifica get_data():\n')
print(time_series_file.get_data())


def compute_avg_monthly_difference(time_series, first_year, last_year):
    first_year = int(first_year)
    last_year = int(last_year)
    lista_di_liste = []
    with open(time_series_file.name) as x:
        for line in x:
                #divido gli elementi per ',' e per '-'
                lista_raw = line.strip().split(',')
                lista_raw[0] = lista_raw[0].split('-')
                if (lista_raw[0][0] == 'date'):
                    continue
                if (lista_raw[1] == ''):
                    lista_raw[1] = '0'
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
    #creo una lista d'appoggio e una matrice per i mesi
    lista_scarsa = []
    matrice_mesi = [ [],[],[],[],[],[],[],[],[],[],[],[] ]
    #scorro gli elementi finché non trovo l'elemento corrispondente a first_year, per poi iniziare da quello
    contatore_elementi = 0
    for item in lista_di_liste:
        if(lista_di_liste[contatore_elementi][0]==first_year):
            continue
        else:
            contatore_elementi+=12

    for i in range(first_year, last_year+1):
        if(lista_di_liste[contatore_elementi][0]==i):
            for j in range(0, 12):
                lista_scarsa.append(lista_di_liste[contatore_elementi][1])
                contatore_elementi+=1
    #creo la matrice, con 12 liste(mesi), ogni lista contiene gli elementi per quel mese
    contatore_mesi = 0  
    for item in lista_scarsa:
        matrice_mesi[contatore_mesi].append(item)
        if(contatore_mesi==11):
            contatore_mesi=0
        else:
            contatore_mesi+=1
    #calcolo l'incremento tra i mesi e aggiungo i risultati uno per uno all'ultima lista, che poi returno
    incremento_medio = [] 
    contatore_matrice = 0   
    while(contatore_matrice<12):
        incremento = 0
        incremento = (matrice_mesi[contatore_matrice][-1]-matrice_mesi[contatore_matrice][0])/2        
        incremento_medio.append(incremento)
        contatore_matrice+=1
        
    return incremento_medio

print('\nVerifica funzione:\n')
print(compute_avg_monthly_difference(time_series, '1949', '1960'))
