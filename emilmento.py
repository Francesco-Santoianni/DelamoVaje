"""#for i in range(12):
            lista_passeggeri.append(elemento[j])
            j+=1
            if j==12:
                j=-12""" 

self.can_read = True
        try:
            my_file = open(self.name, 'r')
            my_file.readline()
        except Exception as e:
            self.can_read = False
            print('Errore in apertura del file: "{}"'.format(e))
        