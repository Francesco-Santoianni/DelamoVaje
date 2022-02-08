class ExamException(Exception):
    pass

class CSVTimeSeriesFile:

    def __init__(self, name):
        self.name = name

    def get_data(self):
        #controllo la correttezza del nome del file
        if ( (self.name == '') or (self.name == None) ):
            raise ExamException('Errore: nessun file inserito.')
        if ( type(self.name) != str ):
            raise ExamException('Errore: nome del file inserito non valido.')

        #controllo duplicati
        lista_linee = []
        with open(self.name) as y:
            for line in y:
                lista_linee.append(line)
       
            misuratore = 0
            for line in y:   
                for i in lista_linee:
                    if (i == line):
                        misuratore+=1
                if(misuratore >= 2):
                    raise ExamException('Errore: la linea {0} è presente più volte nel file.'.format(line))
                misuratore=0
        

        lista1 = []
        with open(self.name) as x:
            for line in x:
                lista2 = line.strip().split(',')
                #skippo la prima linea
                if (lista2[0] == 'date'):
                    continue
                              
                #se per un mese non ci sono info, non lo modifico
                #converto prima in float, poi in int, per sicurezza
                if (lista2[1] != ''):
                    lista2[1] = float(lista2[1])
                    lista2[1] = int(lista2[1])
                    if (lista2[1]<0):
                        lista2[1] = lista2[1]*(-1)
                if (lista2[1] == ''):
                    lista2[1] = 0
                
                lista3 = []
                lista3.append(lista2[0])
                lista3.append(lista2[1])

                lista1.append(lista3)
        return lista1

time_series_file = CSVTimeSeriesFile(name='data.csv')
#controllo l'esistenza del file inserito
try:
    time_series = time_series_file.get_data()
except FileNotFoundError:
    raise ExamException('Errore: file di nome \'{0}\' non trovato.'.format(time_series_file.name))

#Print per vedere get_data()
#print('\nVerifica get_data():\n')
print(time_series_file.get_data())
######################################################

def compute_avg_monthly_difference(time_series, first_year, last_year):
    #controllo se first_year e last_year sono delle stringhe
    if (type(first_year) != str):
        raise ExamException('Errore: first_year deve essere una stringa.')
    if (type(last_year) != str):
        raise ExamException('Errore: last_year deve essere una stringa.')
    #cambio gli anni da stringhe a int, per comodità
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
                
                #skippo i float
                lista_raw[1] = lista_raw[1].split('.')
                if (len(lista_raw[1]) > 2):
                    continue

                if (lista_raw[1][0] != ''):
                    #lista_raw[1] = float(lista_raw[1])
                    lista_raw[1][0] = int(lista_raw[1][0])
                    if (lista_raw[1][0]<0):
                        lista_raw[1][0] = lista_raw[1][0]*(-1)
                
                if (lista_raw[1][0] == ''):
                    lista_raw[1][0] = 0
                try:
                    #converto l'anno in int se possibile
                    lista_raw[0][0] = int(lista_raw[0][0])
                except:
                    continue
                
                #aggiungo solo gli elementi che mi servono(anno e passengers)
                lista_raffinata = []
                lista_raffinata.append(lista_raw[0][0])
                lista_raffinata.append(lista_raw[1][0])
                #aggiungo la lista con gli elementi necessari alla lista finale
                lista_di_liste.append(lista_raffinata)

        #controllo se first_year e/o last_year sono presenti nel file csv/txt
        flag_esistenza=0
        lista_anni = []
        for i in range( 0,int((len(lista_di_liste)/12)) ):
            lista_anni.append(lista_di_liste[flag_esistenza][0])
            flag_esistenza+=12
        if ((first_year not in lista_anni) and (last_year not in lista_anni)):
            raise ExamException('Errore: first_year e last_year non sono presenti nel file csv/txt inserito.')
        elif (first_year not in lista_anni):
            raise ExamException('Errore: first_year non presente nel file csv/txt inserito.')
        elif (last_year not in lista_anni):
            raise ExamException('Errore: last_year non presente nel file csv/txt inserito.')

        
    #creo una lista d'appoggio e una matrice per i mesi
    lista_scarsa = []
    matrice_mesi = [ [],[],[],[],[],[],[],[],[],[],[],[] ]
    #scorro gli elementi finché non trovo l'elemento corrispondente a first_year, per poi iniziare da quello
    contatore_elementi = 0
    for item in lista_di_liste:
        if(lista_di_liste[contatore_elementi][0]==first_year):
            break
        else:
            contatore_elementi+=12

    for i in range(first_year, last_year+1):
        #if(lista_di_liste[contatore_elementi][0]==i):
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
        #conto gli zeri per un mese, se solo un elemento non è zero, allora appendo come incremento 0, in caso contrario calcolo l'incremento medio e appendo
        flag_zeri=0
        for item in matrice_mesi[contatore_matrice]:
            if(item != 0):
                flag_zeri+=1
            
        if (flag_zeri < 2):
            incremento_medio.append(0)
        else:
            incremento = 0
            incremento = (matrice_mesi[contatore_matrice][-1]-matrice_mesi[contatore_matrice][0])/2 
            incremento_medio.append(incremento)
        
        contatore_matrice+=1
                
    return incremento_medio

#print('\nVerifica funzione:\n')
print(compute_avg_monthly_difference(time_series, '1949', '1950'))
###################################################################
    
    
