
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
    i=0;
    valori =[]
    matrice= []
    lista_passeggeri= []
    
    
    with open('data.csv') as x:
        
        for line in x:
            lista_aerei=line.strip().split(',')
            lista_aerei[0]= lista_aerei[0].split('-')

            if (lista_aerei[0][0] != 'date'):
                   
                #converto in interi gli anni, i mesi e il numero di passeggeri ogni mese
                lista_aerei[0][1] = int(lista_aerei[0][1])
                lista_aerei[1]= int(lista_aerei[1])
                lista_aerei[0][0]= int(lista_aerei[0][0])
                    
                lista_definitiva= []

                lista_definitiva.append(lista_aerei[0][0])
                lista_definitiva.append(lista_aerei[0][1])
                lista_definitiva.append(lista_aerei[1]) 
                valori.append(lista_definitiva)
                lista_passeggeri.append(lista_aerei[1])

   

    #uso la matrice definita in precedenza e creo due cicli for: uno per gli anni e uno per i mesi
    #il primo ciclo for lo uso per passare dal primo all'ultimo anno che ho messo in input, nell'ultima riga
    count= 0
    for i in range(last_year-first_year+1):
        matrice.append([])
        

        for j in range(12):
            matrice[i].append(lista_passeggeri[j])
            #hoooooggg riiiiideeeerrr
            #zapri youtube shorts
            #eat my ass, sem ze jedu oprosti
            #pij moje scanje, sem letteralmente komaj spil pol litra vode lmao
            #gay
            #no u 
            #zakaj tvoj program ne dela?
        #sem si postavil isto vprasanje dobro
        #mi printira rit,
        #grem na moj codice, pisi na chat od replit ce ces
    return matrice  
                        
    

avg_difference = compute_avg_monthly_difference(time_series, 1951, 1959)
print(avg_difference)













