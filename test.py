# import requests

# BASE = "http://127.0.0.1:5000/"

# response = requests.get(BASE + "data")
# print(response.json())

#---------------------------------------------------

# import pickle

# pickle_in = open("./model/heart-dieases.pickle","rb")
# classifier=pickle.load(pickle_in)

# print(classifier.predict([[63, 1, 3, 145, 233, 1, 0, 150, 0, 2.3, 0, 0, 1]]))

#---------------------------------------------------

import requests


BASE = "http://127.0.0.1:8000/predict"
input_data = [63, 1, 3, 145, 233, 1, 0, 150, 0, 2.3, 0, 0, 1]

response = requests.post(BASE, input_data)
print(response.json())