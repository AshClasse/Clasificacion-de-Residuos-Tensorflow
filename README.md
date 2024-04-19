# Clasificacion-de-Residuos-Tensorflow

INSTRUCCIONES DE USO DEL PROYECTO: Clasificación de Residuos EcoAI

Este proyecto consta de dos scripts:

1. modelTraining.py para entrenar un modelo de clasificación de imágenes
2. modelTesting.py para detectar objetos en tiempo real utilizando una cámara.

REQUISITOS DE SOFTWARE:

- Python 3.x
- Bibliotecas Python: TensorFlow, matplotlib, numpy, tkinter, Pillow (PIL), OpenCV

INSTALACIÓN DE DEPENDENCIAS:

Instala las bibliotecas Python requeridas ejecutando el siguiente comando en tu terminal o símbolo del sistema:
- pip install tensorflow
- pip install matplotlib
- pip install numpy
- pip install opencv-python-headless
- pip install pillow

ENTRENAMIENTO DEL MODELO
1. Coloca tus datos de entrenamiento en la carpeta garbage_classification.
2. Organiza tus imágenes en subcarpetas donde cada subcarpeta representa una clase de objeto.
3. Ejecuta el script modelTraining.py para entrenar el modelo. Este script generará un modelo entrenado y lo guardará en el directorio modelo_entrenado.

USO DEL MODELO ENTRENADO
1. Ejecuta el script modelTesting.py para iniciar la aplicación de detección de objetos.
2. Haz clic en el botón "Detectar Objetos" para abrir la cámara y comenzar a detectar objetos en tiempo real.
3. La aplicación mostrará el video de la cámara y, en tiempo real, clasificará los objetos detectados en la parte inferior de la ventana.
