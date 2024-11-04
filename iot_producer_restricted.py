import time
import random
from kafka import KafkaProducer

# Configuración del productor Kafka
server = '164.92.76.15:9092'
topic = '21053'

producer = KafkaProducer(
    bootstrap_servers=server
)

# Función para codificar los datos en 3 bytes
def encode_message(temperature, humidity, wind_direction):
    # Convertir temperatura a entero (0 - 11000)
    temp_int = int(round(temperature * 100))
    temp_int = max(0, min(11000, temp_int))

    # Asegurar que la humedad esté entre 0 y 100
    humidity_int = int(humidity)
    humidity_int = max(0, min(100, humidity_int))

    # Mapear la dirección del viento a un número de 3 bits
    wind_directions = {
        "N": 0,
        "NE": 1,
        "E": 2,
        "SE": 3,
        "S": 4,
        "SO": 5,
        "O": 6,
        "NO": 7
    }
    wind_int = wind_directions[wind_direction]

    # Empaquetar en 24 bits: temperatura (14 bits), humedad (7 bits), dirección del viento (3 bits)
    data = (temp_int << 10) | (humidity_int << 3) | wind_int

    # Convertir a 3 bytes
    byte_array = data.to_bytes(3, byteorder='big')
    return byte_array

# Generador de datos de sensores
def generar_telemetria():
    # Generación de datos con una distribución gaussiana
    temperatura = round(random.gauss(55, 15), 2)
    temperatura = max(0, min(110, temperatura)) 

    humedad = int(random.gauss(50, 20))
    humedad = max(0, min(100, humedad))  

    direccion_viento = random.choice(["N", "NE", "E", "SE", "S", "SO", "O", "NO"])

    return temperatura, humedad, direccion_viento

# Envío de datos cada 15-30 segundos
try:
    while True:
        temperatura, humedad, direccion_viento = generar_telemetria()
        payload = encode_message(temperatura, humedad, direccion_viento)
        producer.send(topic, key=b'sensor1', value=payload)
        print(f"Datos enviados: temperatura={temperatura}, humedad={humedad}, direccion_viento={direccion_viento}")
        
        # Espera de 15 a 30 segundos antes de enviar otro dato
        time.sleep(random.randint(2, 5))
except KeyboardInterrupt:
    print("Interrumpido manualmente")
finally:
    producer.close()
