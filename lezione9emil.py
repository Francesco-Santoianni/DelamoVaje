class Model():
    def __init__(self,data):
        self.data= data
    
    def fit(self, data):
        raise NotImplementedError ('Metodo non implementato')
    def predict (self,data): 
        raise NotImplementedError ('Metodo non implementato')

class IncrementModel(Model):
    def increment(self,data):
        prev_item = None
        next_item = 0
        for item in data:
            if prev_item is not None:
                next_item+= item - prev_item
            prev_item = item
        avg_increment = next_item /(len(data)-1)          
        return avg_increment
    
    def predict(self,predict_data):
        avg_increment = self.increment(predict_data)
        return predict_data[-1]+ avg_increment


class FitIncrementModel(IncrementModel):

    def __str__(self):
        return 'FitIncrementModel'

    def fit(self, fit_data):

        # Calcolo l'incremento medio sui dati di fit
        self.global_avg_increment = self.compute_avg_increment(fit_data)

    def predict(self, predict_data):
        
        # Chiamo la predict della classe genitore "IncrementModel"
        parent_prediction = super().predict(predict_data)

        # Sottraggo l'ultimo valore alla predizione del genitore
        # cosi' da avre l'incremento "originale"
        parent_predict_increment = parent_prediction - predict_data[-1]

        # Ora medio l'incremento del fit con quello della predict
        prediction_increment = (self.global_avg_increment + parent_predict_increment) / 2

        # E lo ri-sommo all'ultimo elemento
        prediction = predict_data[-1] + prediction_increment

        return prediction

    
prediction = FitIncrementModel(None)
print(prediction.predict([8, 19, 31, 41, 50, 52, 60]))
        