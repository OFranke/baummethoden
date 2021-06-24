import requests

url = 'http://127.0.0.1:5000/predict_multiple'
myobj = [
            {"input_1": "133", "input_2": "blabla"}, 
            {"input_1": "200", "input_2": "200 blabla"},
        ]

x = requests.post(url, json=myobj)

print(x.text)