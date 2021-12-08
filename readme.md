# TWEEPY TEST
Extrae tweets desde la API de Twitter usando Tweepy.

### REQUISITOS:
1. Tener una cuenta de developer en Twitter (https://developer.twitter.com/).
2. Crear una App en el dasboard de developers (https://developer.twitter.com/).
3. Tener instalado Python3
4. Instalar la libreria tweepy (con el comando `pip3 install tweepy`) y python-dotenv (con el comando `pip3 install -U python-dotenv`)

### PASOS:

1. Renombrar el archivo oculto .env.example a .env
2. Ingresar al archivo .env , luego ingresar las credenciales de la App creada en el item 2 de requisitos.
3. Ejecutar el script principal con el comando `python3 main.py`


### CAMBIOS DE QUERY PARA BÚSQUEDA Y CANTIDAD DE TWEETS A BUSCAR
1. Ingresar al archivo main.py , buscar la línea 59. En la invocación de la función get_principal_tweets() cambiar los 2 #hashtags por el término a buscar sin eliminar las instrucciones `-filter:retweets AND -filter:replies`.

2. En el mismo archivo main.py  se puede cambiar la cantidad de tweets principal a buscar y la cantidad de comentarios a buscar. 
+ En la línea 59, en la invocación de la función get_principal_tweets() cambiar el número 100.

3. En el mismo archivo main.py  se puede cambiar la cantidad de comentarios de un tweet a buscar.
+ En la línea 71, en la invocacion de la función get_replies_tweet() cambiar el número 10.
