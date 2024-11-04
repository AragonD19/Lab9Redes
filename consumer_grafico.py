from kafka import KafkaConsumer
import json
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import datetime

# Configuración del consumidor Kafka
consumer = KafkaConsumer(
    'telemetria',
    bootstrap_servers='164.92.76.15:9092',
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

# Variables para almacenar los datos de los gráficos
tiempos = []
temperaturas = []
humedades = []
presiones = []

# Función de actualización de gráficos en tiempo real
def actualizar_grafico(i):
    for message in consumer:
        datos = message.value
        print(f"Recibido: {datos}")

        # Añadir los datos a las listas
        tiempo = datetime.datetime.now().strftime('%H:%M:%S')
        tiempos.append(tiempo)
        temperaturas.append(datos["temperatura"])
        humedades.append(datos["humedad"])
        presiones.append(datos["presion"])

        # Limitar el tamaño de las listas para que no crezcan indefinidamente
        if len(tiempos) > 20:
            tiempos.pop(0)
            temperaturas.pop(0)
            humedades.pop(0)
            presiones.pop(0)

        # Limpiar y actualizar gráficos
        plt.clf()
        
        plt.subplot(3, 1, 1)
        plt.plot(tiempos, temperaturas, label="Temperatura (°C)", color='r')
        plt.legend(loc='upper left')
        plt.xticks(rotation=45, ha='right')
        
        plt.subplot(3, 1, 2)
        plt.plot(tiempos, humedades, label="Humedad (%)", color='b')
        plt.legend(loc='upper left')
        plt.xticks(rotation=45, ha='right')
        
        plt.subplot(3, 1, 3)
        plt.plot(tiempos, presiones, label="Presión (hPa)", color='g')
        plt.legend(loc='upper left')
        plt.xticks(rotation=45, ha='right')
        
        plt.tight_layout()
        break  # Salir del bucle para permitir la animación en tiempo real

# Configuración de la animación en tiempo real
fig = plt.figure()
ani = FuncAnimation(fig, actualizar_grafico, interval=1000)
plt.show()
