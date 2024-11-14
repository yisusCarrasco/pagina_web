import tkinter as tk
import serial
import json

# Configura el puerto serial (ajusta el puerto según tu configuración)
ser = serial.Serial('COM3', 115200)  # Reemplaza 'COM3' por el puerto correspondiente

def update_values():
    try:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()
            values = json.loads(line)  # Convierte el JSON a un diccionario
            # Actualiza las etiquetas con los valores recibidos
            label_acx.config(text=f"AcX: {values['AcX']}")
            label_acy.config(text=f"AcY: {values['AcY']}")
            label_acz.config(text=f"AcZ: {values['AcZ']}")
            label_tmp.config(text=f"Temp: {(values['Tmp']/10):.2f} °C")
            label_gyx.config(text=f"GyX: {values['GyX']}")
            label_gyy.config(text=f"GyY: {values['GyY']}")
            label_gyz.config(text=f"GyZ: {values['GyZ']}")
    except Exception as e:
        print("Error al procesar los datos:", e)
    root.after(500, update_values)

# Configuración de la ventana principal
root = tk.Tk()
root.title("MPU6050 - Acelerómetro y Giroscopio")
root.geometry("300x200")

# Labels para mostrar los valores
label_acx = tk.Label(root, text="AcX: ---")
label_acx.pack()
label_acy = tk.Label(root, text="AcY: ---")
label_acy.pack()
label_acz = tk.Label(root, text="AcZ: ---")
label_acz.pack()
label_tmp = tk.Label(root, text="Temp: --- °C")
label_tmp.pack()
label_gyx = tk.Label(root, text="GyX: ---")
label_gyx.pack()
label_gyy = tk.Label(root, text="GyY: ---")
label_gyy.pack()
label_gyz = tk.Label(root, text="GyZ: ---")
label_gyz.pack()

# Inicia la actualización de valores
update_values()

# Ejecuta la aplicación
root.mainloop()
