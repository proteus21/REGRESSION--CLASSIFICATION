import pandas as pd
from sklearn.ensemble import  RandomForestClassifier
from pydantic import BaseModel
import joblib

class IrisSpecies(BaseModel):
    sepal_length: float
    sepal_width:float
    petal_length:float
    petal_width:float

class IrisModel:
    def __init__(self):
        self.df=pd.read_csv('iris.csv')
        self.model_fname_='iris_model.pkl'
        try:
            self.model=joblib.open(self.model_fname_)
        except Exception as _:
            self.model= self.train_model()
            joblib.dump(self.model, self.model_fname_)

    def train_model(self):
        X=self.df.drop('species', axis=1)
        y=self.df['species']
        rfc=RandomForestClassifier()
        model=rfc.fit(X,y)
        return model

    def predict_species(self, sepal_length, sepal_width, pental_length, pental_width):
        data_in=[[sepal_length, sepal_width, pental_length, pental_width]]
        prediction=self.model.predict(data_in)
        probability=self.model.predict_proba(data_in).max()
        return prediction[0], probability