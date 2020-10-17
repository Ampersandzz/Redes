# LEVANTAMIENTO DE CONTENEDORES MYSQL-CLIENT Y MYSQL-SERVER


1. Primero se debe levantar el contenedor servidor. Para esto se deben seguir los pasos a continuación.
    - Se debe ir a la carpeta server
    - Luego se debe hacer el build de la imagen. Esto se puede hacer con  
    `sudo docker build --tag mysql:server .` .  
    - Luego se debe crear y correr un contenedor con la imagen anterior. Esto se puede hacer con `sudo docker run -it mysql:server` . Con esto ya se debería entrar al contenedor y el servidor mysql se iniciaría de forma automática.

2. Ahora se levantará el contenedor cliente. Para esto se deben seguir los pasos a continuación. 
    - Se debe ir a la carpeta client.
    - Luego se debe hacer el build de la imagen. Esto se puede hacer con  
    `sudo docker build --tag mysql:client .` .  
    - Luego se debe crear y correr un contenedor con la imagen anterior. Se debe pasar el host como variable de entorno.
    - Para obtener la IP host primero se debe conocer la id del contenedor servidor. esto se puede hacer mediante `sudo docker ps` (el contenedor servidor debe estar corriendo). Luego, mediante el siguiente comando, se puede obtener la IP del host `docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' container_id`.
    - Ya teniendo el host, se debe correr el contenedor cliente. Esto se puede hacer con  `sudo docker run -it -e "MYSQL_HOST=ip_host" mysql:client` con ip_host la IP del contenedor servidor.
    - Con lo anterior, ya se debería entrar a MySQL.


<b>ADVERTENCIA:</b> La imagen del servidor pesa 14.4gb 

A continuación se presenta un [video](https://youtu.be/RU4R7Q54NLw) que se encuentra en este repositorio (Patrones-MySQL.mvk), en el cual se pueden ver patrones de tráfico encontrados en el protocolo MySQL. 

<a href="https://youtu.be/RU4R7Q54NLw" target="_blank"><img src="https://img.youtube.com/vi/RU4R7Q54NLw/maxresdefault.jpg" 
alt="IMAGE ALT TEXT HERE" width="400" height="225"/></a>

También se adjunta un [video](https://youtu.be/ipPNsHhFE0M) en donde se modifica el tráfico mediante la herramienta [Polymorph](https://github.com/shramos/polymorph).

<a href="https://youtu.be/ipPNsHhFE0M" target="_blank"><img src="https://img.youtube.com/vi/ipPNsHhFE0M/maxresdefault.jpg" 
alt="IMAGE ALT TEXT HERE" width="400" height="225"/></a>
