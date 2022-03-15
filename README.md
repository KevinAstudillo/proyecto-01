--- Proyecto 1: Web Service ---

Profesor: José de Jesús Galaviz Casas

Integrantes: 
- Joel Haidd Reyes Cedillo
- Eduardo Montaño Gómez
- Kevin Hernandez Astudillo

Programa que permite obtener los datos del clima de las ciudades
a partir de los datos de latitud y longitud de la ciudad a partir
de un archivo en formato .csv

Antes de ejecutar el programa debes de crear un archivo llamado
'config.py' en la carpeta src y dentro de este archivo debes de
escribir lo siguiente: 
```
api_key = "TU_API_KEY"
```


donde `TU_API_KEY` la debes reemplazar por tu api key.

Para correr el programa es necesario ejecutar el archivo 
"proyecto01.py" de la carpeta src en la terminal con python, 
seguido de la ruta absoluta del archivo .csv de donde se quiere
obtener los datos del clima, por ejemplo: 


```
python 3 proyecto01.py ~/proyecto01/datos/dataset1.csv 
```

TEST:
Para realizar el test de la clase Clima debe de colocarse en la carpeta 'test' y ejecutar lo siguiente en la terminal de comandos:

```
$python3 test_lectorCSV.py.
```


Si no lo hace de este modo, no podra ejecutar las pruebas.

Si no tienes instalado python3, deberás de instalarlo.
