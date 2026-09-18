import pandas as pd 
from sklearn.linear_model import LinearRegression
import pickle

data=pd.read_csv('../data/student.csv')

x=data[['hours','attendance']]
y=data['marks']
model = LinearRegression()
model.fit(x,y)
pickle.dump(model,open('model.pkl','wb'))
print("Model trained and saved")
                        