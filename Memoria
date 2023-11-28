import psutil

def mostrar_rendimiento_memoria():
    memoria = psutil.virtual_memory()

    print("Rendimiento de la memoria:")
    print(f"  Total: {memoria.total / (1024 ** 3):.2f} GB")
    print(f"  Disponible: {memoria.available / (1024 ** 3):.2f} GB")
    print(f"  Usado: {memoria.used / (1024 ** 3):.2f} GB")
    print(f"  Porcentaje de uso: {memoria.percent}%")

if __name__ == "__main__":
    mostrar_rendimiento_memoria()
