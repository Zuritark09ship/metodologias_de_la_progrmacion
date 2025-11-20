import network
import socket
from machine import Pin, PWM
import time

# -------------------------------
# CONFIGURACIÓN DE MOTORES
# -------------------------------
IN1 = Pin(26, Pin.OUT)
IN2 = Pin(25, Pin.OUT)
ENA = PWM(Pin(27), freq=1000)

IN3 = Pin(12, Pin.OUT)
IN4 = Pin(13, Pin.OUT)
ENB = PWM(Pin(14), freq=1000)

def move_motor(in1, in2, en, speed):
    if speed > 0:
        in1.value(1)
        in2.value(0)
    elif speed < 0:
        in1.value(0)
        in2.value(1)
    else:
        in1.value(0)
        in2.value(0)
    en.duty(abs(speed))

# -------------------------------
# CONFIGURACIÓN WIFI
# -------------------------------
SSID = "ESP32-CAR"
PASSWORD = "12345678"
CAR_IP = "192.168.4.2"
GATEWAY = "192.168.4.1"
SUBNET = "255.255.255.0"

wifi = network.WLAN(network.STA_IF)
wifi.active(True)

connected = False
while not connected:
    try:
        wifi.ifconfig((CAR_IP, SUBNET, GATEWAY, "8.8.8.8"))
        wifi.connect(SSID, PASSWORD)
        print("Intentando conectar a WiFi...")
        timeout = 0
        while not wifi.isconnected() and timeout < 10:
            time.sleep(1)
            timeout += 1
        if wifi.isconnected():
            connected = True
    except OSError as e:
        print("Error WiFi, reintentando...", e)
        time.sleep(2)

print("Conectado al AP:", wifi.ifconfig())

# -------------------------------
# CONFIGURACIÓN UDP
# -------------------------------
UDP_PORT = 4210
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((CAR_IP, UDP_PORT))
print("Esperando datos del joystick...")

# -------------------------------
# BUCLE PRINCIPAL
# -------------------------------
while True:
    try:
        data, addr = sock.recvfrom(32)
        msg = data.decode().strip()
        x, y = map(int, msg.split(","))
    except Exception:
        continue

    print("Joystick -> X:", x, "Y:", y)

    left_speed = (y - x) * 10
    right_speed = (y + x) * 10

    left_speed = max(min(left_speed, 1023), -1023)
    right_speed = max(min(right_speed, 1023), -1023)

    move_motor(IN1, IN2, ENA, left_speed)
    move_motor(IN3, IN4, ENB, right_speed)





##controlador 


import network
import socket
from machine import ADC, Pin
import time

# -------------------------------
# CONFIGURACIÓN JOYSTICK
# -------------------------------
joy_x = ADC(Pin(34))
joy_y = ADC(Pin(35))
joy_x.atten(ADC.ATTN_11DB)  # Rango completo 0-4095
joy_y.atten(ADC.ATTN_11DB)

# -------------------------------
# CONFIGURACIÓN PUNTO DE ACCESO
# -------------------------------
SSID = "ESP32-CAR"
PASSWORD = "12345678"

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=SSID, password=PASSWORD)
print("Punto de acceso creado:", ap.ifconfig())

# -------------------------------
# CONFIGURACIÓN UDP
# -------------------------------
UDP_PORT = 4210
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
CAR_IP = "192.168.4.2"  # IP del carro

# -------------------------------
# FUNCIÓN PARA MAPEAR RANGO
# -------------------------------
def map_range(value, in_min, in_max, out_min, out_max):
    return int((value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

# -------------------------------
# BUCLE PRINCIPAL
# -------------------------------
while True:
    try:
        x = joy_x.read()
        y = joy_y.read()

        # Mapear a -100 a 100
        mx = map_range(x, 0, 4095, -100, 100)
        my = map_range(y, 0, 4095, -100, 100)

        # Crear paquete de datos
        data = f"{mx},{my}"
        sock.sendto(data.encode(), (CAR_IP, UDP_PORT))

        print("Enviado:", data)
        time.sleep(0.05)  # 50 ms
    except Exception as e:
        print("Error:", e)
        time.sleep(0.5)

