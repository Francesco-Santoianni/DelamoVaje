class CSVFILE:
    
    def __init__(shampoo_sales, name):
        shampoo_sales.name = name

    def get_data(shampoo_sales):
        datalist1 = []
        try: 
            with open('karkoli_sales.txt') as x:
                for line in x:
                    datalist2 = line.strip().split(',')
                    if (datalist2[0] == 'Date'):
                        continue
                    datalist1.append(datalist2)
            return(datalist1)
        except Exception as e: 
            e = 'Errore: hai cercato di aprire un file non esistente!'
            return e
    
object1 = CSVFILE('shampoo_sales.txt')

#print(object1.name)
print(object1.get_data())
