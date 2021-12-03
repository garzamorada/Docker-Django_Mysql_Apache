# INSTRUCCIONES EQUIPO 8

Las claves que estan son por defecto, deberian cada uno cambiarlas en su propio docker si lo van a poner publico en algun momento.
Se cambian en el ``` docker-compose.yml ```, en ``` equipo8/settings.py ``` y en ``` initial.sql ``` 
(ahi arme un usuario multihost para el phpmyadmin y por si se quieren conectar desde otra maquina de su red).

Tambien hay un superusuario de django que accede desde ``` localhost:8000/admin ```

Una vez que sincronizan con el git, antes de ejecutar los contenedores, corran estos comandos:
``` docker-compose run web python manage.py migrate ``` para crear las tablas de django y este  ``` docker-compose run web python manage.py createsuperuser ``` para crar el superusuario de administracion, finalemte ejecutan ``` docker-compose up ```

Esta configuracion les va a permitir tener su frontend y conectarlo con el backend en django. 
También deje todo preparado para conectar django a un apache para manejar las conexiones, no lo configuré aún pero estan los plugins instalados.

La idea es hacer 2 aplicaciones la primera para gestión de usuarios, la segunda de gestión de contenido.

# Gestión de Usuarios
>> recibir del frontend un formulario de registro para el alta
>> permitir a un admin ver los usuarios
>> permitir a los usuarios loguearse en el sistema
>> permitir a cada usuario modificar sus datos y/o opciones y darse de baja

# Gestión de Contenido
>> Permitir a un administrador cargar, modificar y eliminar contenido
>> Crear un formulario para tales fines que ademas permita subir archivos (imagenes)
>> Entregar al frontend un json con los datos y las imagenes que se requieran