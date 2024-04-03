import psutil
import socket
import subprocess
import os
import winreg
import time
import pyfiglet
#pip install psutil
#pip install pyfiglet
def obtener_informacion_red():
    # Obtener información de la red a la que estás conectado
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        print(f"Nombre de host: {hostname}")
        print(f"Dirección IP: {ip_address}")
    except socket.gaierror as e:
        print("No se pudo obtener la información de red:", e)

def obtener_informacion_dns():
    try:
        resolvers = socket.gethostbyname_ex(socket.gethostname())
        print("\nInformación de servidores DNS:")
        print(f"  Servidores DNS configurados:")
        for dns_server in resolvers[2]:
            print(f"    {dns_server}")
    except socket.gaierror as e:
        print("No se pudo obtener la información de DNS:", e)

def obtener_informacion_gateways():
    try:
        result = subprocess.check_output(["ipconfig", "/all"], shell=True, encoding='latin-1')
        print("\nInformación de puertas de enlace (Gateways):")
        index = result.find("Default Gateway")
        while index != -1:
            start = result.rfind("\n", 0, index) + 1
            end = result.find("\n", index)
            gateway_info = result[start:end].strip()
            print(f"  {gateway_info}")
            index = result.find("Default Gateway", end)
    except subprocess.CalledProcessError as e:
        print("No se pudo obtener la información de puertas de enlace:", e)

def obtener_conexiones_activas():
    try:
        conexiones = psutil.net_connections(kind='inet')
        print("\nConexiones de red activas:")
        for conn in conexiones:
            print(f"  Tipo de conexión: {conn.type}")
            print(f"  Local Address: {format_ipv6(conn.laddr)}")
            print(f"  Remote Address: {format_ipv6(conn.raddr)}")
    except psutil.Error as e:
        print("No se pudo obtener la información de conexiones activas:", e)

def format_ipv6(ip):
    # Formatear direcciones IPv6 en una representación legible
    if ":" in ip:
        return f"[{ip}]"
    return ip

def obtener_informacion_interfaces():
    interfaces = psutil.net_if_stats()
    print("\nInformación de interfaces de red físicas y virtuales:")
    for nombre, stats in interfaces.items():
        print(f"  Nombre de interfaz: {nombre}")
        print(f"    Estado: {'Activa' if stats.isup else 'Inactiva'}")
        print(f"    Tipo: {'Ethernet' if stats.isup else 'Desconocido'}")
        print(f"    Velocidad: {stats.speed} Mbps")

def obtener_informacion_proxy():
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Internet Settings") as key:
            proxy_enabled = winreg.QueryValueEx(key, "ProxyEnable")[0]
            proxy_server = winreg.QueryValueEx(key, "ProxyServer")[0]
            if proxy_enabled == 1:
                print("\nConfiguración de Proxy habilitada:")
                print(f"  Servidor Proxy: {proxy_server}")
            else:
                print("\nConfiguración de Proxy deshabilitada")
    except FileNotFoundError:
        print("\nConfiguración de Proxy no encontrada")

def obtener_informacion_firewall():
    try:
        firewall_info = subprocess.check_output(["netsh", "advfirewall", "show", "allprofiles"]).decode("latin-1")
        print("\nInformación del cortafuegos y reglas de red:")
        print(firewall_info)
    except subprocess.CalledProcessError as e:
        print("No se pudo obtener la información del cortafuegos y reglas de red:", e)

def obtener_uso_ancho_de_banda():
    try:
        while True:
            net_io = psutil.net_io_counters()
            print("\nUso de ancho de banda:")
            print(f"  Bytes enviados: {net_io.bytes_sent} bytes")
            print(f"  Bytes recibidos: {net_io.bytes_recv} bytes")
            time.sleep(5)  # Actualizar cada 5 segundos
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    # Generar y mostrar el arte ASCII con pyfiglet
    ascii_art = pyfiglet.figlet_format("@S3s1N0")
    print(ascii_art)

    obtener_informacion_red()
    obtener_informacion_dns()
    obtener_informacion_gateways()
    obtener_conexiones_activas()
    obtener_informacion_interfaces()
    obtener_informacion_proxy()
    obtener_informacion_firewall()
    obtener_uso_ancho_de_banda()
