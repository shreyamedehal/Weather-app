from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid='+'api_key'+'&units=metric').read()
        json_data = json.loads(res)
        data = {
            "country" : str(json_data['name'])+ ', '+ str(json_data['sys']['country']),
            "icon": str(json_data['weather'][0]['icon']),
            "temprature" : str(json_data['main']['temp'])+ " \N{DEGREE SIGN}"+"C",
            "main": str(json_data['weather'][0]['main']),
            "minTemp" : str(json_data['main']['temp_min'])+ " \N{DEGREE SIGN}"+"C",
            "maxTemp" : str(json_data['main']['temp_max'])+ " \N{DEGREE SIGN}"+"C",

        }
    else:
        data ={}
    
    return render(request, 'index.html',{'data':data})
