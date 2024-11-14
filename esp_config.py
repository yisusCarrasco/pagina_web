import time
from machine import I2C, Pin
import ujson

class accel:
    def __init__(self, i2c, addr=0x68):
        self.i2c = i2c
        self.addr = addr
        self.i2c.start()
        self.i2c.writeto(self.addr, bytearray([107, 0]))
        self.i2c.stop()

    def get_raw_values(self):
        self.i2c.start()
        data = self.i2c.readfrom_mem(self.addr, 0x3B, 14)
        self.i2c.stop()
        return data

    def get_values(self):
        raw_data = self.get_raw_values()
        return {
            "AcX": int.from_bytes(raw_data[0:2], 'big'),
            "AcY": int.from_bytes(raw_data[2:4], 'big'),
            "AcZ": int.from_bytes(raw_data[4:6], 'big'),
            "Tmp": int.from_bytes(raw_data[6:8], 'big') / 340.00 + 36.53,
            "GyX": int.from_bytes(raw_data[8:10], 'big'),
            "GyY": int.from_bytes(raw_data[10:12], 'big'),
            "GyZ": int.from_bytes(raw_data[12:14], 'big')
        }

# Configura el I2C y MPU6050
i2c = I2C(scl=Pin(22), sda=Pin(21))  # Ajusta los pines según tu ESP32
mpu = accel(i2c)

while True:
    values = mpu.get_values()  # Obtiene los datos del acelerómetro
    json_data = ujson.dumps(values)  # Convierte los datos a JSON
    print(json_data)  # Envío de los datos vía serial
    time.sleep(0.5)  # Ajusta la frecuencia de envío según sea necesario
