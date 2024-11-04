# Lab9Redes

# Proyecto: Productor y Consumidor Kafka para Estación Meteorológica IoT

## Descripción
Este proyecto implementa un productor de Kafka y un consumidor que simula un nodo de sensores de una estación meteorológica. El productor envía datos de temperatura, humedad y dirección del viento a un broker de Kafka, mientras que el consumidor recibe esos datos y los grafica en tiempo real.

## Requisitos

- Python 3.x
- Apache Kafka y Zookeeper en ejecución
- Librerías de Python:
  - `kafka-python`
  - `matplotlib` (solo para el consumidor)

## Instalación

1. **Instalar Python**:
   Asegúrate de tener Python 3 instalado en tu máquina. Puedes descargarlo desde [python.org](https://www.python.org/downloads/).

2. **Crear un entorno virtual**:
   Es recomendable usar un entorno virtual para gestionar las dependencias. Sigue estos pasos:
   ```bash
   # Navega a tu directorio de trabajo
   cd /ruta/a/tu/directorio

   # Crea un entorno virtual
   python -m venv venv

   # Activa el entorno virtual
   # En Windows
   venv\Scripts\activate
   # En macOS/Linux
   source venv/bin/activate

   # Proyecto: Productor y Consumidor Kafka para Estación Meteorológica IoT

## Instalación de Librerías

Con el entorno virtual activado, ejecuta el siguiente comando para instalar las librerías requeridas:

  `pip install kafka-python matplotlib`

Configuración del Broker Kafka
Asegúrate de que tu broker de Kafka esté en funcionamiento y accesible. Este proyecto está configurado para conectarse a lab9.alumchat.lol (IP: 164.92.76.15) en el puerto 9092.

Ejecución de los Archivos
1. Ejecutar el Productor
Archivo: iot_producer.py
Descripción: Este script genera datos de sensores y los envía a Kafka.

Pasos:

Abre una terminal.
Navega al directorio donde se encuentra iot_producer.py.
Ejecuta el siguiente comando:
  `python iot_producer.py`
  
El productor comenzará a enviar datos cada 15 a 30 segundos.
Para detener el productor, presiona Ctrl + C.

2. Ejecutar el Consumidor y Graficador
Archivo: consumer_grafico.py
Descripción: Este script recibe los datos de Kafka y los grafica en tiempo real.

Pasos:

Abre otra terminal.
Navega al directorio donde se encuentra consumer_grafico.py.
Ejecuta el siguiente comando:
  `python consumer_grafico.py`

El consumidor comenzará a recibir y graficar los datos en tiempo real.

3. Ejecutar el Productor Alternativo (si es necesario)
Archivo: producer.py
Descripción: Este script también actúa como productor de datos para Kafka.

Pasos:

Abre otra terminal (si deseas ejecutarlo en paralelo).
Navega al directorio donde se encuentra producer.py.
Ejecuta el siguiente comando:
  `python producer.py`
  
Este productor funcionará de manera similar al anterior, enviando datos al broker.

Notas Adicionales
Asegúrate de que el topic utilizado por los productores sea único para tu grupo para evitar conflictos.
Puedes modificar y expandir los scripts según tus necesidades.
