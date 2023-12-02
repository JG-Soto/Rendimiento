import psutil

def mostrar_rendimiento_red():
    interfaces_red = psutil.net_io_counters(pernic=True)

    print("Rendimiento de la red:")
    for interfaz, datos in interfaces_red.items():
        print(f"  Interfaz: {interfaz}")
        print(f"    Bytes enviados: {datos.bytes_sent / (1024 ** 2):.2f} MB")
        print(f"    Bytes recibidos: {datos.bytes_recv / (1024 ** 2):.2f} MB")
        print(f"    Paquetes enviados: {datos.packets_sent}")
        print(f"    Paquetes recibidos: {datos.packets_recv}")
        print()

if __name__ == "__main__":
    mostrar_rendimiento_red()