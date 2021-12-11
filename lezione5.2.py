class CSVFILE:
    
    def __init__(shampoo_sales, name):
        shampoo_sales.name = name

    def get_data(shampoo_sales):
        datalist1 = []
        datalist2 = []
        with open('shampoo_sales.txt') as x:
            for line in x:
                datalist2 = line.strip().split(',')
                if (datalist2[0] == 'Date'):
                    continue
                datalist1.append(datalist2)
        return(datalist1)

class NumericalCSVFILE(CSVFILE):

    def get_data1(shampoo_sales):
        
        with open('shampoo_sales.txt') as x:
            for line in x:
                datalist2 = line.strip().split(',')
                if (datalist2[0] == 'Date'):
                    continue
                print(float(datalist2[1]))       
                

#print(object1.name)
#print(object1.get_data())

object1 = NumericalCSVFILE('shampoo_sales.txt')

#print(object1.name)
#print(object1.get_data())

object1.get_data1()