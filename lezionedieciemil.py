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
    def fit(self, global_avg_increment):
        self.global_avg_increment = global_avg_increment
    
prediction = IncrementModel(None)
print(prediction.predict([8, 19, 31, 41, 50, 52, 60]))

