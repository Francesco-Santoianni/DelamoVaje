class Model():

    def __init__(self, data):
        self.data = data

    def fit(self, data):
        raise NotImplementedError('Metodo non implementato')

    def predict(self, data):
        raise NotImplementedError('Metodo non implementato')

class IncrementedModel(Model):

    def predict(self, data):
        prediction = 0
        counter = 0
        current_item = 0
        previous_item = 0
        increment = 0
        for i, item in enumerate(data):

            if i > 0:
                current_item = data[i]
                previous_item = data[i-1]
                increment += current_item - previous_item
                if i <= 1:
                    continue
                else:
                    prediction = (increment/(i)) + item 
        return prediction


lista1 = IncrementedModel(None)
print(lista1.predict(data=[8,19,31,41,50,52,60]))