from tkinter import *
from PIL import Image, ImageTk
import cv2
import numpy as np
import tensorflow as tf
from tensorflow import keras
import math

class ModeloTestingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Modelo Testing")
        self.root.geometry("1280x720")

        self.label = Label(root, text="Modelo de Testing")
        self.label.pack(pady=10)

        self.load_button = Button(root, text="Detectar Objetos", command=self.detectar_objetos)
        self.load_button.pack(pady=5)

        self.canvas = Canvas(root, width=640, height=480, bg='white')
        self.canvas.pack()

        self.label_objeto_detectado = Label(root, text="", bg='white')
        self.label_objeto_detectado.pack(pady=5)

        self.cap = None

        self.model = keras.models.load_model('modelo_entrenado/modelo.keras')

        self.img_height = 1280
        self.img_width = 1280

        self.class_names = ['battery', 'cardboard', 'glass', 'metal', 'paper', 'plastic', 'trash']

    def detectar_objetos(self):
        if self.cap is None:
            self.cap = cv2.VideoCapture(0)
            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
            self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
            self.mostrar_video()

    def mostrar_video(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.resize(frame, (self.img_width, self.img_height))
            img = Image.fromarray(frame)
            img = ImageTk.PhotoImage(image=img)
            self.canvas.create_image(0, 0, anchor=NW, image=img)
            self.canvas.image = img

            self.predecir_objetos(frame)

            self.root.after(10, self.mostrar_video)
        else:
            self.cap.release()
            self.cap = None

    def predecir_objetos(self, frame):
        img_array = cv2.resize(frame, (self.img_width, self.img_height))
        img_array = np.expand_dims(img_array, axis=0)

        predictions = self.model.predict(img_array)
        score = tf.nn.softmax(predictions[0])

        objeto_detectado = self.class_names[np.argmax(score)]
        confianza = 100 * np.max(score)

        self.label_objeto_detectado.config(text=f"Objeto: {objeto_detectado}, Confianza: {confianza:.2f}%")

def ventana_principal():
    root = Tk()
    app = ModeloTestingApp(root)
    root.mainloop()

if __name__ == "__main__":
    ventana_principal()
