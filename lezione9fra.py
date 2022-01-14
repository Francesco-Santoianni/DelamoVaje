class Model():

    def fit(self, data):
        pass

    def predict(self, data):
        pass

class IncrementModel(Model):

    def compute_avg_increment(self, data):

        prev_item = None

        increments = 0
        
        for item in data:

            if prev_item is not None:
                increments += item - prev_item

            prev_item = item

        avg_increment = increments / (len(data)-1)
        
        return avg_increment

    def predict(self, predict_data):

        avg_increment = self.compute_avg_increment(predict_data)

        return predict_data[-1] + avg_increment

class FitIncrementModel(IncrementModel):

    def fit(self, fit_data):
        self.global_avg_increment = self.compute_avg_increment(fit_data)

    def predict(self, predict_data):
        parent_prediction = super().predict(predict_data)

        parent_predict_increment = parent_prediction - predict_data[-1]

        parent_increment = (self.global_avg_increment + parent_predict_increment)/2

        prediction = predict_data[-1] + parent_increment

        return prediction

shampoo_sales = [8, 19, 31, 41, 50, 52, 60]
fit_increment_model = FitIncrementModel(shampoo_sales)
fit_increment_model.fit(shampoo_sales)
print(fit_increment_model)
