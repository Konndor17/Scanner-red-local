
Este programa en Python realiza varias funciones para obtener y mostrar información relacionada con la red y el sistema operativo Windows. Aquí está una descripción de lo que hace cada función:

obtener_informacion_red(): Obtiene y muestra el nombre del host y la dirección IP de la máquina actual utilizando el módulo socket.

obtener_informacion_dns(): Muestra la información de los servidores DNS configurados en la máquina actual utilizando el módulo socket.

obtener_informacion_gateways(): Muestra la información de las puertas de enlace (gateways) de red utilizando el comando ipconfig a través de subprocess.

obtener_conexiones_activas(): Muestra las conexiones de red activas en la máquina utilizando el módulo psutil.

obtener_informacion_interfaces(): Muestra información sobre las interfaces de red físicas y virtuales, incluido el estado y la velocidad, utilizando el módulo psutil.

obtener_informacion_proxy(): Muestra la configuración del proxy si está habilitada, utilizando el módulo winreg para acceder al Registro de Windows.

obtener_informacion_firewall(): Muestra información sobre el cortafuegos y las reglas de red utilizando el comando netsh a través de subprocess.

obtener_uso_ancho_de_banda(): Muestra el uso de ancho de banda actual, mostrando la cantidad de bytes enviados y recibidos cada 5 segundos, utilizando el módulo psutil.

