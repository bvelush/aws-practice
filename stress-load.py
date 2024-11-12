import requests

for i in range(1000):
    result = requests.get('http://myapi-lb-1595571151.us-east-1.elb.amazonaws.com/api/load')
    print(i, result.text)