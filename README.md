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

```bash
pip install kafka-python matplotlib



## Ejecuion de programas

```bash
python iot_producer.py

python consumer_grafico.py

python producer.py

