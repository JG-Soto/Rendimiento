import psutil
def obtener_temperatura_cpu():
    try:
        temperaturas = psutil.sensors_temperatures()

        if 'coretemp' in temperaturas:
            temperaturas_cpu = temperaturas['coretemp']
            print("Temperatura del CPU:")
            for entrada in temperaturas_cpu:
                print(f"  {entrada.label}: {entrada.current}°C")
        else:
            print("No se encontró información de temperatura del CPU.")

    except Exception as e:
        print(f"No se pudo obtener la temperatura del CPU: {e}")

if __name__ == "__main__":
    obtener_temperatura_cpu()
