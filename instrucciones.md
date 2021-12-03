# INSTRUCCIONES EQUIPO 8

Las claves que estan son por defecto, deberian cada uno cambiarlas en su propio docker si lo van a poner publico en algun momento.
Se cambian en el ``` docker-compose.yml ```, en ``` equipo8/settings.py ``` y en ``` initial.sql ``` 
(ahi arme un usuario multihost para el phpmyadmin y por si se quieren conectar desde otra maquina de su red).

Tambien hay un superusuario de django que accede desde ``` localhost:8000/admin ```

Una vez que sincronizan con el git, antes de ejecutar los contenedores, corran estos comandos:
``` docker-compose run web python manage.py migrate ``` para crear las tablas de django y este  ``` docker-compose run web python manage.py createsuperuser ``` para crar el superusuario de administracion, finalemte ejecutan ``` docker-compose up ```

Esta configuracion les va a permitir tener su frontend y conectarlo con el backend en django. 
También deje todo preparado para conectar django a un apache para manejar las conexiones, no lo configuré aún pero estan los plugins instalados.