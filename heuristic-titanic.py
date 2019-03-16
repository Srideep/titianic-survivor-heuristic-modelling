import numpy
import pandas
import statsmodels.api as sm

def custom_heuristic(file_path):
    

    predictions = {}
    df = pandas.read_csv(file_path)
    for passenger_index, passenger in df.iterrows():
        passenger_id = passenger['PassengerId']
        if (passenger['Sex'] == 'male'):
            predictions[passenger_id] = 0
        
        if (passenger['Sex'] == 'female' or passenger['Pclass']==1 and passenger['Age'] < 18 and passenger['Age'] == 80):
            predictions[passenger_id] = 1
        else:
            predictions[passenger_id] = 0
    return predictions
