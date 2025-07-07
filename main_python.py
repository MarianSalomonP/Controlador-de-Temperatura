import serial
import tkinter as tk
from tkinter import simpledialog
import matplotlib.pyplot as plt

puerto = serial.Serial('COM6', 9600)

# Crear ventana para pedir temperatura
root = tk.Tk()
root.withdraw()  # Oculta la ventana principal
temp_objetivo = simpledialog.askfloat("Interfaz de Usuario", "Introduce la temperatura objetivo (°C):")

histeresis = 1.0

# Ventana emergente para introducir t_obj
mensaje = f"SET:{temp_objetivo}\n"
puerto.write(mensaje.encode())
print("Temperatura enviada al Arduino:", mensaje.strip())

plt.ion()
fig, ax = plt.subplots()
temps_medidas = []
temps_objetivo = []

# Esperar confirmacion de Arduino (SET_OK)
while True:
    linea = puerto.readline().decode('utf-8', errors='ignore').strip()
    if linea.startswith("SET_OK:"):
        print("Arduino confirma temperatura objetivo:", linea)
        break

# Comenzar a leer datos de temperatura
print("\nLectura continua de temperatura actual (VAL):")
try:
    while True:
        linea = puerto.readline().decode('utf-8', errors='ignore').strip()
        print(linea)
        if linea.startswith("VAL:"):
            temp_dut = float(linea[4:])
            print(f"Temperatura actual: {temp_dut:.2f} °C")
            temps_medidas.append(temp_dut)
            temps_objetivo.append(temp_objetivo)

            # Grafica de comparacion
            ax.clear()
            ax.plot(temps_medidas, label="Temperatura del DUT", color='orange')
            ax.plot(temps_objetivo, label="Temperatura objetivo", color='blue')
            temps_sup = [temp_objetivo + histeresis] * len(temps_medidas)
            temps_inf = [temp_objetivo - histeresis] * len(temps_medidas)
            ax.plot(temps_sup, label="Limite superior (histeresis)", color='red', linestyle='--')
            ax.plot(temps_inf, label="Limite inferior (histeresis)", color='red', linestyle='--')
            ax.set_xlabel("Tiempo (muestras)")
            ax.set_ylabel("Temperatura (°C)")
            ax.set_title("Temperatura del DUT vs Temperatura objetivo")
            ax.legend()
            plt.pause(0.1)

except KeyboardInterrupt:
    print("\nLectura interrumpida por el usuario.")

finally:
    puerto.close()
    print("Puerto serie cerrado.")
