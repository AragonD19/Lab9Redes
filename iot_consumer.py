from kafka import KafkaConsumer
import json
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import datetime
import threading

# Configuración del consumidor Kafka
consumer = KafkaConsumer(
    '21053',  
    bootstrap_servers='164.92.76.15:9092',
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

# Variables para almacenar los datos de los gráficos
tiempos = []
temperaturas = []
humedades = []
direcciones_viento = []

# Función para recibir datos en un hilo separado
def recibir_datos():
    for message in consumer:
        datos = message.value
        print(f"Recibido: {datos}")

        # Añadir los datos a las listas
        tiempo = datetime.datetime.now().strftime('%H:%M:%S')
        tiempos.append(tiempo)
        temperaturas.append(datos["temperatura"])
        humedades.append(datos["humedad"])
        direcciones_viento.append(datos["direccion_viento"])

        # Limitar el tamaño de las listas para que no crezcan indefinidamente
        if len(tiempos) > 20:
            tiempos.pop(0)
            temperaturas.pop(0)
            humedades.pop(0)
            direcciones_viento.pop(0)

# Función de actualización de gráficos en tiempo real
def actualizar_grafico(i):
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
    # Mostrar las direcciones del viento como lista
    plt.text(0.5, 0.5, ' ' + ', '.join(direcciones_viento), 
            fontsize=12, ha='center', va='center')
    plt.title("Direcciones del Viento")
    plt.axis('off')  # Ocultar los ejes

    
    plt.tight_layout()

# Iniciar el hilo para recibir datos
hilo_datos = threading.Thread(target=recibir_datos)
hilo_datos.daemon = True  # Permitir que el hilo se cierre al cerrar la aplicación
hilo_datos.start()

# Configuración de la animación en tiempo real
fig = plt.figure()
ani = FuncAnimation(fig, actualizar_grafico, interval=1000)

# Mostrar la gráfica
plt.show()
