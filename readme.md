# Info
Lambda function to make an api call to open weather api 

## Main function

```
import json
from urllib.request import Request, urlopen


def request weather(location:str,api_key:str)->str:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&cnt={1}&appid={api_key}"
    req = Request(url)
    resp =urlopen(req)
    response = resp.read().decode('utf-8')
    response_json = json.loads(response)

    if response_json['cod'] == 200:
        #response_json = response.json()
        chance_rain =  response_json['weather'][0]['description']
        mean_temp =  float(response_json['main']['temp'])
        if ((chance_rain != 'clear sky') & (mean_temp < 15)):
            return {
                'statusCode': 200,
                'body': json.dumps('Jacket Required')
            }
        else:
            return {
                'statusCode': 200,
                'body': json.dumps('No Jacket Required')
            }
    else:
        return {
            'statusCode': 200,
            'body': json.dumps('May be you should wear jacket or may be you should not; Could not Establish connection to api, try latter')
        }
```

### Brief info on What function does:
It simply make the api call and determines whether person should 
wear a jacket or not:
    Condition to wear a jacket is determined by average weather and if weather description. **Since I couldn't find a probability of rain so I just used any weather description other than *clear sky*. I guess this is/could be a  problem**. As is, it simply prints to aws logs although it can be accessed via API gateway if need be.

### Breifly about Aws Lambda creation steps
I mostly used web interface not create lambda and uses python 3.7. All the library are already included by default so there is no other dependencies. 

