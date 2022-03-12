# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 00:22:22 2022

@author: Cochinitavinil
"""


import requests 
from functools import lru_cache

# la funcion que hace que nuestra funcion guarde en momeoria todos las eces que llamamos a funcion 
@lru_cache() 
def Clima(api_key,origin,destination,OriLat,OriLon,DesLat,DesLon):
    """
    

    Parameters
    ----------
    api_key : Es una cadena.De caracteres del teclado que parecen al azar.
        DESCRIPTION: Esta cadena es la Key que nos da OpenWeather para poder hacer
        los requests, donde las Key son individuales, ya que estan limitadas en los
        requests.
    origin : es un string de 3 letras mayusculas.
        DESCRIPTION: Estas 3 letras son las Iniciales en formato IATA, del 
    aeropuerto de origen es decir representan el aeropuerto del que partio.
    destination : es un string de 3 letras mayusculas.
        DESCRIPTION: Estas 3 letras son las Iniciales en formato IATA, del 
    aeropuerto de destino, es decir,  representan el aeropuerto de llegada del vuelo.
    OriLat : Es una cadena, que contiene un numero flotante.
        DESCRIPTION. Representa la latitud del lugar de origen.
    OriLon : Es una cadena, que contiene un numero flotante.
        DESCRIPTION. Representa la longuitud del lugar de origen.
    DesLat : Es una cadena, que contiene un numero flotante.
        DESCRIPTION.Representan la latitud del lugar de llegada.
    DesLon : Es una cadena, que contiene un numero flotante.
        DESCRIPTION. Representa la longuitud del lugar de llegada.

    Returns
    -------
    Nos regres un diccionario que presenta la siguiente estrutura:
        4 keys:
        
        1). "coord" = Que es un diccionario con las coordendas, como se muestra
        a continuacion:
            -------------'coord': {'lon': 99.0721, 'lat': 19.4363} ----------------
            
            
        2) 'weather': que nos regresa una lista con un diccionario dentro de esta
        como el que se muestra a continuacion:
            -------------'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}]------------
        
        
        3) 'base' = es una cadena con la el string stations, como se ve a continuacion:
                        -------------'base': 'stations'-------------
        
        
        4) "main"= es un diccionario que contiene un diccionario con la informacion 
        mas relevante del clima, como se ve en el siguiente ejemplo:
          --------  main': {'temp': 296.28, 'feels_like': 296.06, 'temp_min': 292.97, 'temp_max': 296.28,
          'pressure': 1012, 'humidity': 54, 'sea_level': 1012, 'grnd_level': 951}, 'visibility': 10000,
          'wind': {'speed': 0.86, 'deg': 328, 'gust': 0.89}, 'clouds': {'all': 20}, 'dt': 1646252239, 
          'sys': {'type': 2, 'id': 2041966, 'country': 'TH', 'sunrise': 1646264533, 'sunset': 1646306976}, 
          'timezone': 25200, 'id': 1153673, 'name': 'Chiang Dao', 'cod': 200}  --------
        
    Extra:
    -------
    Este codigo fue basado en gran medida, en lo realizado en el siguiente 
    video:https://www.youtube.com/watch?v=_jBeFdqnNAU
    
    El codigo funciona en principio con 3 entradas, la Key, latitud y longuitud. Con 
    estos datos pormos hacer el requests y este nos regresa un un formato JSON, que 
    un diccionaro de donde pormos extraer toda la informacion de el lugar que deseemos.       

    """
    
    urlOri= f"http://api.openweathermap.org/data/2.5/weather?lat={OriLat}&lon={OriLon}&appid={api_key}&units=metric&lang=sp"
    respuestaOri=requests.get(urlOri).json()
    temperaturaOri=respuestaOri["main"]["temp"]
    sensacionOri=respuestaOri["main"]["feels_like"]
    temmaxOri=respuestaOri["main"]["temp_max"]
    temminOri=respuestaOri["main"]["temp_min"]
    presOri=respuestaOri["main"]["pressure"]
    humedadOri= respuestaOri["main"]["humidity"]
    
    
    urlDes= f"http://api.openweathermap.org/data/2.5/weather?lat={DesLat}&lon={DesLon}&appid={api_key}&units=metric&lang=sp"
    respuestaDes=requests.get(urlDes).json()
    temperaturaDes=respuestaDes["main"]["temp"]
    sensacionDes=respuestaDes["main"]["feels_like"]
    temmaxDes=respuestaDes["main"]["temp_max"]
    temminDes=respuestaDes["main"]["temp_min"]
    presDes=respuestaDes["main"]["pressure"]
    humedadDes= respuestaDes["main"]["humidity"]
    
    print("-------------------------------------------")
    print("Ciudad de Origen: ",origin,"\nLatitud : ",OriLat," , Longuitud: ",OriLon,"\nTemperatura: ",temperaturaOri,"°c","\nSensación Termica: ",sensacionOri,"°c","\nTemperatura Maxima: ",temmaxOri,"°c","\nTemperatura Minima: ",temminOri,"°c","´\nPresión Atmosferica: ",presOri,"hPA","\nHumedad : ",humedadOri,"%","\n     ",
          "\nCiudad de Destino: ",destination,"\nLatitud : ",DesLat," , Longuitud: ",DesLon,"\nTemperatura: ",temperaturaDes,"°c","\nSensación Termica: ",sensacionDes,"°c","\nTemperatura Maxima: ",temmaxDes,"°c","\nTemperatura Minima: ",temminDes,"°c","´\nPresión Atmosferica: ",presDes,"hPA","\nHumedad : ",humedadDes,"%")
    print("-------------------------------------------")
