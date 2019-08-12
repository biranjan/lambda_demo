import json
#import urllib
from urllib.request import Request, urlopen

api_key = "6f2a033cd8eeec74d282636adb7939ef"
location = "helsinki"
def lambda_handler(event,context):
    # TODO implement
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
        