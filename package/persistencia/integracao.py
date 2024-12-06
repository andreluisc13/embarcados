import serial
import time
import os
from datetime import datetime

SERIAL_PORT = "/dev/ttyS3" #ttyS3 faz a referencia a com4(emulada no virtual box) que esta com  ESP32 
BAUD_RATE = 9600
DATA_FILE = "distancias.txt"

def init_file():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as f:
            f.write("Registro de distâncias maiores que 10cm:\n")

def log_distance(distancia):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(DATA_FILE, "a") as f:
        f.write(f"{timestamp} - Distância maior que 10cm registrada: {distancia} cm\n")

def main():
    init_file()
    try:
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        while True:
            line = ser.readline().decode("utf-8").strip()
            if line.startswith("Distância:"):
                _, dist_str = line.split(":")
                distancia = float(dist_str.strip().split(" ")[0])
                if distancia > 10:
                    log_distance(distancia)
            time.sleep(0.1)
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()

