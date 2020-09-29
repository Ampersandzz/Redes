# LEVANTAMIENTO DE CONTENEDORES MYSQL-CLIENT Y MYSQL-SERVER


1. Primero se debe levantar el contenedor servidor. Para esto se deben seguir los pasos a continuación.
    - Se debe ir a la carpeta server
    - Luego se debe hacer el build de la imagen. Esto se puede hacer con 
    `sudo docker build --tag mysql:server .`.
    - Luego se debe crear y correr un contenedor con la imagen anterior. Esto se puede hacer con `sudo docker run -it mysql:server` .
    - Opcionalmente se puede verificar que el proceso mysqld este efectivamente corriendo. Esto se puede hacer con `ps aux` .

2. Ahora se levantará el contenedor cliente. Para esto se deben seguir los pasos a continuación. 
    - Se debe ir a la carpeta client.
    - Luego se debe hacer el build de la imagen. Esto se puede hacer con 
    `sudo docker build --tag mysql:client .`.
    - Luego se debe crear y correr un contenedor con la imagen anterior. Se debe pasar el host como variable de entorno.
    - Para obtener la IP host primero se debe conocer la id del contenedor servidor. esto se puede hacer mediante `sudo docker ps` (el contenedor servidor debe estar corriendo). Luego, mediante el siguiente comando, se puede obtener la IP del host `docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' container_id`.
    - Ya teniendo el host, se debe correr el contenedor cliente. Esto se puede hacer con  `sudo docker run -it -e "MYSQL_HOST=ip_host mysql:client"` con ip_host la IP del contenedor servidor.
    - Con lo anterior, ya se debería entrar a la shell de MySQL.
