--- Proyecto 1: Web Service ---

Profesor: José de Jesús Galaviz Casas

Integrantes: 
- Joel Haidd Reyes Cedillo
- Eduardo Montaño Gómez
- Kevin Hernandez Astudillo

Programa que permite obtener los datos del clima de las ciudades
a partir de los datos de latitud y longitud de la ciudad a partir
de un archivo en formato .csv

Requisitos:
El programa ha sido diseñado para correr en un sistema operativo
de tipo Unix con una terminal integrada, no se ha garantizado el
funcionamiento en sistemas operativos distintos, por lo que es
altamente recomendable que siga los requisitos aquí descritos o
de lo contrario el programa podría no funcionar correctamente.  
El programa está escrito en el lenguaje de programación python por
lo que es necesario que en su equipo tenga instalado una versión
reciente de phyton 3, así como pip que es necesario para la 
instalación de módulos que no vienen incluidos por defecto 
en la instalación normal de python.
En concreto, se debe descargar e instalar el módulo `requests`
de python usando `pip` para poder realizar correctamente una
llamada a la API y obtener los datos del clima.

(en caso de ya tener instalado requests omita el siguiente párrafo)
Para instalar el módulo requests dirigase a su terminal 
y ejecute el comando: 
```pip install requests```
O de forma alternativa también puede hacerlo con:
```python -m pip install requests```
(Si tiene python 3 los comandos son idénticos salvo que debe
colocar phyton3 en vez de python)

De igual manera el archivo donde se obtengan los datos deberá ser
de tipo .csv con el formato de columnas siguiente:
```origin,destination,origin_latitude,origin_longitude,destination_latitude,destination_longitude
<IATA Origen>,<IATA Destino>,<Latitud Origen>,<Longitud Origen>,<Latitud Destino>,<Longitud Origen>
```

Antes de correr el programa es necesario abrir el archivo `key.txt` 
en la carpeta src y colocar ahí su apiKey de la página OpenWeather 
(en caso de no tenerla favor de dirigirse a ```https://openweathermap.org/ ```
y obtener una). Favor de colocar únicamente su apikey en la segunda
linea de texto, en caso de no hacerlo el programa no podrá funcionar.

Para correr el programa es necesario ubicarse en la carpeta src
que está contenida en el proyecto y desde la terminal ejecute el
programa "proyecto01.py" con python, seguido de la ruta absoluta
del archivo .csv de donde se quiere obtener el clima, por ejemplo: 
```python 3 proyecto01.py ~/proyecto01/datos/dataset1.csv ```

TEST: Para realizar el test de la clase Clima debe de colocarse 
en la carpeta 'test' y ejecutar lo siguiente en la terminal de comandos:

```$python3 test_lectorCSV.py.```

Si no lo hace de este modo, no podra ejecutar las pruebas.



