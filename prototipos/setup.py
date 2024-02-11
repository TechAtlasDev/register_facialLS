""" Prototipo incompleto del detector facial PROGRAMADO EN TKINTER - Python"""
# Importando modulos
#import cv2
import tkinter
#import imutils
from PIL import Image, ImageTk
#import face_recognition as fr # Se encarga de detectar rostros con un modelo preentrenado
#import numpy as np # Nos permite analizar matrices de las imagenes
#import cv2 # Operar con vision artificial
#import os # Operar con el sistema operativo
#import random



"""
# Variables necesarias para su uso (Si es necesario, cambiar las variables)
directorio_usuarios = "rostros" # Nombre del directorio que contendrá los rostros de los usuarios
clases_usuarios = []
lista_usuarios = os.listdir(directorio_usuarios)
imagenes = []
"""
fondo_info = "white"
informacion = "Procura estar en un lugar bien iluminado, mira frente la cámara, y procura no usar mucho maquillaje o accesorios que interfiera con la detección de tu rostro completo."
ventana = tkinter.Tk()
"""
# Leyendo los rostros de la base de datos
for usuarios in lista_usuarios:
    imagen_leida = cv2.imread("{}/{}".format(directorio_usuarios, usuarios))
    # Guardando las imagenes leidas en la lista
    imagenes.append(imagen_leida)
    # Guardando las clases en la lista
    clases_usuarios.append(os.path.splitext(usuarios)[0])

# Procesando las imagenes de los rostros
def procesar(imagenes):
    rostros_procesados = []
    for rostro in imagenes:
        # Haciendo en una escala de grises
        rostro = cv2.cvtColor(rostro, cv2.COLOR_BGR2RGB)
        # Codificando los rostros con el reconocedor de rostros
        imagen_codificada = fr.face_encodings(rostro)[0]
        rostros_procesados.append(imagen_codificada)

    # La funcion regresa una lista de datos procesados
    return rostros_procesados

# Haciendo un llamado de la funcion para procesar los datos con las imagenes guardadas
rostros_codificados_db = procesar(imagenes)

"""
# - Ajustando dimensiones de la imagen -
# Abriendo imagen
imagen_normal = Image.open("insignia.png")
# Ajustando la imagen a las dimensiones de 200x200, se usa el atributo antialias para indicarle al sistema que cuando se minimice la imagen, no pierda su calidad de imagen
imagen_procesada = imagen_normal.resize((175,150))#, Image.ANTIALIAS)

# Indicando titulo a la ventana
ventana.title("SISTEMA DE REGISTRO FACIAL")

# Indicando las dimensiones de la ventana
ventana.geometry("1370x700")

# Indicando variables receptoras
respuesta = tkinter.IntVar()
multiplicador = tkinter.IntVar()
resultado = tkinter.IntVar()

# Creando funciones para calcular valores
def calcular(a, b):
    resultado.set(a*b)

# Crear un widget Canvas
canvas = tkinter.Canvas(ventana, width=1370, height=700)

# Cargar una imagen en el Canvas
imagen = tkinter.PhotoImage(file="fondo.png")
canvas.create_image(0, 0, anchor=tkinter.NW, image=imagen)
# Mostrar el Canvas en la ventana
canvas.pack()

#imagenF = tkinter.PhotoImage(file="Fondo.png")
#background = tkinter.Label(image = imagenF, text = "Fondo")
#background.place(x = 0, y = 0, relwidth = 1, relheight = 1)


# Indicando labels principales
intro = tkinter.Label(ventana, text="SI NO DETECTA TU ROSTRO, USA UNA EXPRESIÓN DE ROSTRO NEUTRA", font=("Cursive", 25), fg="black")
intro.place(x=100, y=10)

#entrada = tkinter.Entry(ventana, textvariable=respuesta).place(x=120, y=10)

# Indicando la impresion de la imagen con Pillow (ImageTk)
imagen_lista = ImageTk.PhotoImage(imagen_procesada)
tkinter.Label(ventana, image=imagen_lista).place(x=20, y=70)

# Indicando información adicional
intro = tkinter.Label(ventana, text=informacion, font=("Verdana", 16), fg="black")
intro.config(bg=fondo_info, width=10, height=20)
intro.place(x=100, y=10)


# Creando RadioButtons, cada uno multiplica lo indicado
#x2 = tkinter.Radiobutton(ventana, text="X2", value=2, variable=multiplicador).place(x=30, y=40)
#x3 = tkinter.Radiobutton(ventana, text="X3", value=3, variable=multiplicador).place(x=30, y=80)
#x4 = tkinter.Radiobutton(ventana, text="X4", value=4, variable=multiplicador).place(x=90, y=40)
#x5 = tkinter.Radiobutton(ventana, text="X5", value=5, variable=multiplicador).place(x=90, y=80)

# Indicando el resultado:
#resultado_label = tkinter.Label(ventana, text="Resultado").place(x=170, y=60)
#resultado_entry = tkinter.Entry(ventana, textvariable=resultado, state="disable").place(x=230, y=60)

# Boton receptor de Informacion
#boton_rst = tkinter.Button(ventana, text="Calcular!", command=lambda: calcular(respuesta.get(), multiplicador.get())).place(x=40, y=120)


# Funcion iniciar
def iniciar():
    global camara
    # Elegimos la camara
    camara = cv2.VideoCapture(0)
    visualizar()
    print("El sistema fué iniciado")

# Funcion Visualizar
def visualizar():
    # Leemos la videocaptura
    if camara is not None:
        tipo_de_camara, camara_procesada = camara.read()

        # Si es correcta
        if tipo_de_camara == True:
            comp1 = 100
            # Redimensionando las imagenes
            camara_redimensionada = cv2.resize(camara_procesada, (0,0), None, 0.25, 0.25)
            # Conversion de color
            colores = cv2.cvtColor(camara_redimensionada, cv2.COLOR_BGR2RGB)
            # Buscando los rostros con face_recognition
            rostros = fr.face_locations(colores)
            # Codificando rostros encontrados
            rostros_codificados = fr.face_encodings(colores, rostros)

            # Clasificando los rostros encontrados para hacer una comparación con datos almacenados
            for rostro_codificado, rostro_localizacion in zip(rostros_codificados, rostros):
                # Comparando los rostros captados en la camara y en la carpeta
                resultado = fr.compare_faces(rostros_codificados_db, rostro_codificado)
                # Calculando la similitud entre los rostros
                similitud = fr.face_distance(rostros_codificados_db, rostro_codificado)
        #        print (similitud)
                # Buscando el valor más bajo (mientras más bajo, es más parecido al rostro)
                minimo_valor = np.argmin(similitud)

                if resultado[minimo_valor]:
                    dni_encontrado = clases_usuarios[minimo_valor].upper()
        #           print (dni_encontrado)
                    # Extrayendo coordenadas
                    y1, x2, y2, x1 = rostro_localizacion
                    # Escala
                    y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
                    indice = resultado.index(True)

                    # Hora de la comparación de los rostros
                    if comp1 != indice:
                        comp1 = indice
                    
                    if comp1 == indice:
                        cv2.rectangle(camara_procesada, (x1, y1), (x2, y2), (0, 255, 0), 3)
                        cv2.rectangle(camara_procesada, (x1, y2-35), (x2, y2), (0, 255, 0), cv2.FILLED)
                        cv2.putText(camara_procesada, dni_encontrado, (x1+6, y2-6), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

                else:
                    y1, x2, y2, x1 = rostro_localizacion
                    # Escala
                    y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
                    cv2.rectangle(camara_procesada, (x1, y1), (x2, y2), (0, 0, 255), 3)
                    cv2.rectangle(camara_procesada, (x1, y2-35), (x2, y2), (0, 0, 255), cv2.FILLED)
                    cv2.putText(camara_procesada, "DESCONOCIDO", (x1+6, y2-6), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)


#            cv2.imshow("Reconocimiento Facial", camara_procesada)
            camara_procesada = cv2.cvtColor(camara_procesada, cv2.COLOR_BGR2RGB)
            # Rendimensionamos el video
#            camara_procesada = imutils.resize(camara_procesada, width=640)

            # Convertimos el video
            im = Image.fromarray(camara_procesada)
            img = ImageTk.PhotoImage(image=im)

            # Mostramos en el GUI
            lblVideo.configure(image=img)
            lblVideo.image = img
            lblVideo.after(10, visualizar)

        else:
            camara.release()

# Iniciar Video
#imagenBI = tkinter.PhotoImage(file="Inicio.png")
#inicio = tkinter.Button(ventana, text="Iniciar", image=imagenBI, height="40", width="200", command=iniciar)
#inicio.place(x = 100, y = 580)


# Configurando la pantalla
ventana.configure(bg='#001e9e')

# Video
lblVideo = tkinter.Label(ventana)
lblVideo.place(x = 320, y = 50)

#lblVideo2 = tkinter.Label(ventana)
#lblVideo2.place(x = 470, y = 500)


# Mostrando ventana
ventana.mainloop()