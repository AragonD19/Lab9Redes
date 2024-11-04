from kafka import KafkaProducer
import json
import time
import random

# Configuración del productor Kafka
producer = KafkaProducer(
    bootstrap_servers='164.92.76.15:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def generar_telemetria():
    return {
        "temperatura": round(random.uniform(-10, 35), 2),
        "humedad": round(random.uniform(10, 90), 2),
        "presion": round(random.uniform(950, 1050), 2)
    }

# Envío de datos cada cierto intervalo
try:
    while True:
        datos = generar_telemetria()
        producer.send('telemetria', value=datos)
        print(f"Enviado: {datos}")
        time.sleep(5)  # Enviar cada 5 segundos
except KeyboardInterrupt:
    producer.close()
