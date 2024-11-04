import json
import time
import random
from kafka import KafkaProducer

# Configuración del productor Kafka
server = '164.92.76.15:9092'
topic = '21053'  # Usa tu número de carné u otro identificador único para el topic

producer = KafkaProducer(
    bootstrap_servers=server,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Generador de datos de sensores
def generar_telemetria():
    # Generación de datos con una distribución gaussiana
    temperatura = round(random.gauss(55, 15), 2)
    temperatura = max(0, min(110, temperatura))  # Asegurar el rango [0, 110]

    humedad = int(random.gauss(50, 20))
    humedad = max(0, min(100, humedad))  # Asegurar el rango [0, 100]

    direccion_viento = random.choice(["N", "NO", "O", "SO", "S", "SE", "E", "NE"])

    return {
        "temperatura": temperatura,
        "humedad": humedad,
        "direccion_viento": direccion_viento
    }

# Envío de datos cada 15-30 segundos
try:
    while True:
        datos = generar_telemetria()
        producer.send(topic, key=b'sensor1', value=datos)
        print(f"Datos enviados: {datos}")
        
        # Espera de 15 a 30 segundos antes de enviar otro dato
        time.sleep(random.randint(15, 30))
except KeyboardInterrupt:
    print("Interrumpido manualmente")
finally:
    producer.close()
