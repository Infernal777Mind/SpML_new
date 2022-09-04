import requests


payload = {'sepal_length': 0, 'sepal_width': 0, 'petal_length': 0, 'petal_width': 0}

r = requests.post("http://0.0.0.0:5000/predict", json=payload)

print(r.json())