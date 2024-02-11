""" ARCHIVO QUE SE ENCARGA DE EJECUTAR TODO EL PROYECTO """
# Conteo de inasistencias
# Backup de bases de datos
# conteo de datos para registrar a los usuarios
import dataexc
import configs
import sys

# Verificando si el dispositivo cuenta con internet
if dataexc.tiene_internet():
    # Verificando si la version del sistema está actualizada
    resultado = dataexc.version_desact()
    if resultado: # Si el sistema está desactualizado
        
        import sys
        import tkinter as tk
        import git

        def actualizar():
            print ("Actualizando")
            root.destroy()

            # Clonamos el repositorio
            repo = git.Repo.clone_from('https://github.com/gjimenezdeza/facial_detector', '.')
            print ("Comando repo hecho")
            # Hacemos un pull para actualizar el repositorio local
            repo.remotes.origin.pull()
            print ("Comando pull hecho")

            # Hacemos un commit de los cambios
            repo.git.add('--all')
            print ("Comando all hecho")
            repo.git.commit('-m "Actualizando el repositorio"')
            print ("Comando -m hecho")

            # Hacemos un push de los cambios al repositorio remoto
            repo.remotes.origin.push()
            print ("Comando push hecho")
            sys.exit()
        def no_actualizar():
            root.destroy()

        root = tk.Tk()
        root.title("Actualización disponible")
        root.geometry("500x100")

        label = tk.Label(root, text="Se encontró una nueva versión de éste proyecto, basado en github. \n¿Quieres actualizarlo a la última versión?")
        label.pack()

        boton_si = tk.Button(root, text="Sí", command=actualizar)
        boton_si.pack(side="left")

        boton_no = tk.Button(root, text="No", command=no_actualizar)
        boton_no.pack(side="right")

        root.mainloop()

    
import tkinter
# Crea una ventana principal
ventana = tkinter.Tk()

# Crea una función para manejar el evento del botón
def salir_programa():
    ventana.destroy()
    sys.exit()

# Establece el título de la ventana
ventana.title("CONFIGURACIÓN DEL TEXTO EN INTERFAZ")
ventana.geometry("1000x100")

# Indicando variables receptoras
tipo = tkinter.StringVar()
respuesta = tkinter.StringVar()

# DISEÑANDO LOS LABEL
intro = tkinter.Label(ventana, text="Pon lo que quieras que haya en el comunicado:").place(x=20, y=10)
entrada = tkinter.Entry(ventana, textvariable=respuesta).place(x=280, y=10, width=690)
comunicado = tkinter.Radiobutton(ventana, text="COMUNICADO (fondo rojo)", value="rojo", variable=tipo).place(x=20, y=40)
recordatorio = tkinter.Radiobutton(ventana, text="RECORDATORIO (fondo verde)", value="verde", variable=tipo).place(x=320, y=40)
aviso = tkinter.Radiobutton(ventana, text="AVISO (fondo amarillo)", value="amarillo", variable=tipo).place(x=600, y=40)

# Crea un botón que cierre la ventana cuando se presione
boton_cerrar = tkinter.Button(ventana, text="GUARDAR Y CERRAR", command=ventana.destroy).place(x=850, y=65)

# Crea un botón que cierre la ventana cuando se presione
boton_cerrar = tkinter.Button(ventana, text="CANCELAR", command=salir_programa).place(x=750, y=65)

# Bucle principal de Tkinter
ventana.mainloop()

tipo_f = tipo.get()
respuesta_f = respuesta.get()

import datetime, time
import configs

# Funcion para hacer una animacion (Reemplazo de print)
def animacion(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(8. / 150)

# Interfaz Bienvenida terminal
GL = "\033[96;1m" # Blue aqua
BB = "\033[34;1m" # Blue light
YY = "\033[33;1m" # Yellow light
GG = "\033[32;1m" # Green light
WW = "\033[0;1m"  # White light
RR = "\033[31;1m" # Red light
CC = "\033[36;1m" # Cyan light
B = "\033[34m"    # Blue
G = "\033[32m"    # Green
R = "\033[31m"    # Rojo
M = "\033[35;1m"  # Morado

banner = CC+"""\n\n
                                                    ▄▄    ▄▄          
            ▀████▀                ▄█▀▀▀█▄█        ▀███  ▀███          
              ██                 ▄██    ▀█          ██    ██          
              ██      ▄█▀██▄     ▀███▄    ▄█▀██▄    ██    ██   ▄▄█▀██ 
              ██     ██   ██       ▀█████▄█   ██    ██    ██  ▄█▀   ██
              ██     ▄▄█████     ▄     ▀██▄█████    ██    ██  ██▀▀▀▀▀▀
              ██    ▄██   ██     ██     ███   ██    ██    ██  ██▄    ▄
            ██████████████▀██▄   █▀█████▀▀████▀██▄▄████▄▄████▄ ▀█████▀
                                                          """+WW
print (banner)                                                          

animacion("  Programado y diseñado con mucho aprecio de Giovanny Jimenez, promo 22.")
print (YY+"\n [ -- ] INFORMACIÓN DEL SISTEMA BASADO EN EL DOCUMENTO" + RR, "'configs.py'")
print (M+"\n -------------- CONFIGURACION DE LAS BASES DE DATOS ---------------")
print (YY+"["+CC+"+"+YY+"]"+WW,"HOST de la base de datos:", configs.host)
print (YY+"["+CC+"+"+YY+"]"+WW,"PUERTO de conexión de la base de datos:", configs.port)
print (YY+"["+CC+"+"+YY+"]"+WW,"USUARIO de conexion de la base de datos:", configs.user)
print (YY+"["+CC+"+"+YY+"]"+WW,"Nombre de la base de datos a conectar:", configs.database)
print (YY+"["+CC+"+"+YY+"]"+WW,"Nombre de la tabla de los usuarios:", configs.tabla_usuarios)
print (YY+"["+CC+"+"+YY+"]"+WW,"Nombre de la tabla de la asistencia", configs.tabla_asistencia)
print (M+"\n -------------- CONFIGURACION DE LOS DATOS ADICIONALES ---------------")
print (YY+"["+CC+"+"+YY+"]"+WW,"PUERTO de ejecución de la página web:", configs.puerto_web)
print (YY+"["+CC+"+"+YY+"]"+WW,"NÚMERO DE LA CÁMARA de proyección:", configs.numero_camara)
print (YY+"["+CC+"+"+YY+"]"+WW,"DIRECTORIO de los rostros de los usuarios:", configs.directorio_usuarios)
print (YY+"["+CC+"+"+YY+"]"+GG,"ESTADO DEL DEBUG DEL SISTEMA:"+CC, configs.debug_status)
print (YY+"["+CC+"+"+YY+"]"+WW,"HORA Y FECHA DE INICIO DEL BOT:", datetime.datetime.now())

print (RR+"SI QUIERES CAMBIAR LOS DATOS, EDITA EL DOCUMENTO "+ WW +"'configs.py'")

print (YY+"\n\n [ -- ] INICIANDO EL SISTEMA [ -- ]")

# Importando los modulos
from flask import Flask # Creacion de la aplicacion
from flask import render_template # Renderizar las paginas
from flask import Response # Crear conexiones entre los servicios (web y webcam)
import face_recognition as fr # Se encarga de detectar rostros con un modelo preentrenado
import numpy as np # Nos permite analizar arreglos
import cv2 # Operar con vision artificial
import os # Operar con el sistema operativo
import dataexc # Operar con el documento que permite operar con las bases de datos
import random # Hacer selecciones aleatorias
print (GG+"["+WW+"*"+GG+"] MODULOS IMPORTADOS SATISFACTORIAMENTE")

# Verificando el cumpleaños de los usuarios
respuesta = dataexc.verificar_cumpleaños("nombres, apellidos")
print (GG+"["+WW+"*"+GG+"] EL DÍA DE HOY HAY {} CUMPLEAÑOS.".format(respuesta[0]))

# Verificando si el día de ayer asistieron alumnos o no
respuesta = dataexc.asistencia_conteo()
print (GG+"["+WW+"*"+GG+"] SE REGISTRÓ LAS ASISTENCIAS E INASISTENCIAS CORRECTAMENTE DE CADA ALUMNO.")

# Configurando la aplicacion web
pagina = Flask(__name__)
print (GG+"["+WW+"*"+GG+"] PAGINA CONFIGURADA CON FLASK CORRECTAMENTE")

# ----------------------- LEYENDO LOS ROSTROS AMACENADOS EN LA CARPETA CON CV2 -----------------------------------
clases_usuarios = [] # SE VA A IDENTIFICAR EL DNI DE CADA ESTUDIANTE
lista_usuarios = os.listdir(configs.directorio_usuarios) # SE VA A ASIGNAR EN UNA VAARIABLE LOS ROSTROS ENCONTRADOS EN EL DIRECTORIO
imagenes = [] # LOS NOMBRES DE LAS IMAGENES
for usuarios in lista_usuarios:
    imagen_leida = cv2.imread("{}/{}".format(configs.directorio_usuarios, usuarios))
    # Guardando las imagenes leidas en la lista
    imagenes.append(imagen_leida)
    # Guardando las clases en la lista
    clases_usuarios.append(os.path.splitext(usuarios)[0])
print (GG+"["+WW+"*"+GG+"]", len(clases_usuarios),"ROSTROS ALMACENADOS EN UNA LISTA CORRECTAMENTE")

# Procesando las imagenes de los rostros
def procesar(imagenes):
    rostros_procesados = []
    for rostro in imagenes:
        # Haciendo en una escala de grises
        rostro = cv2.cvtColor(rostro, cv2.COLOR_BGR2RGB)
        # Codificando los rostros con el reconocedor de rostros
        imagen_codificada = fr.face_encodings(rostro)[0]
        rostros_procesados.append(imagen_codificada)

    # La funcion regresa una lista de rostros encontrados
    return rostros_procesados

# Haciendo un llamado de la funcion para procesar los datos con las imagenes guardadas
rostros_codificados_db = procesar(imagenes)
print (GG+"["+WW+"*"+GG+"] LOS", len(rostros_codificados_db),"ROSTROS DE LA CARPETA FUERON PROCESADOS DE MANERA EXITOSA")

# ------------------ INICIANDO LA CAPTURA DEL VIDEO -----------------------------
camara = cv2.VideoCapture(configs.numero_camara, cv2.CAP_DSHOW)

# ------------------------ DEFINIENDO LA FUNCION PARA ENCONTRAR ROSTROS --------------------------------
def detector_rostros():
    # Bucle infinito de lectura de camara
    while True:
        # Leyendo el video
        tipo_de_camara, camara_procesada = camara.read()
        # Evitando el efecto de espejo
        camara_procesada = cv2.flip(camara_procesada, 1)
        comparador = 100 # La variable comparador se utiliza en el código para comparar los índices de dos rostros y determinar si son iguales o no. Podemos comparar esto con una caja de frutas donde cada fruta tiene un índice asignado. La variable comparador sería una fruta que se saca de la caja para compararla con otra fruta que se saca de la caja. Si ambas frutas tienen el mismo índice, entonces comparador tendrá el valor del índice de la fruta con la que se comparó. De esta manera, el código puede determinar si dos rostros son iguales o no comparando sus índices a través de comparador.
        # Redimensionando las imagenes
        camara_redimensionada = cv2.resize(camara_procesada, (0,0), None, 0.25, 0.25)
        # Conversion de color
        colores = cv2.cvtColor(camara_redimensionada, cv2.COLOR_BGR2RGB)
        # Buscando los rostros con face_recognition
        rostros = fr.face_locations(colores)
        # Codificando rostros encontrados
        rostros_codificados = fr.face_encodings(colores, rostros)

        for rostro_codificado, rostro_localizacion in zip(rostros_codificados, rostros):
            # Comparando los rostros captados en la camara y en la carpeta
            resultado = fr.compare_faces(rostros_codificados_db, rostro_codificado)
            # Calculando la similitud entre los rostros
            similitud = fr.face_distance(rostros_codificados_db, rostro_codificado)
            # print (similitud)
            # Buscando el valor más bajo (mientras más bajo, es más parecido al rostro)
            minimo_valor = np.argmin(similitud) # En este caso, se está obteniendo el índice del rostro más similar en la base de datos de rostros a partir de la similitud calculada por face_distance. Esto permite determinar el rostro más parecido en la base de datos y, por lo tanto, identificar a la persona en el video.

            # SI HAY UN ROSTRO ENCONTRADO SE EJECUTA ÉSTA SENTENCIA CONDICIONAL
            if resultado[minimo_valor]: # Esto se utiliza para determinar si el rostro detectado coincide con alguno de los rostros almacenados previamente.
                dni_encontrado = clases_usuarios[minimo_valor].upper()
                dataexc.registrar_asistencia(["dni", "fecha_registro", "hora_registro"], dni_encontrado)
                data_list = dataexc.busqueda(["nombres", "cargo"], "dni", dni_encontrado) # Se hace la busqueda de los datos en la base de datos del usuario encontrado 
                y1, x2, y2, x1 = rostro_localizacion # Obteniendo las coordenadas del rostro encontrado
                # Se hace una escala porque se redimensionó el video para procesarlo
                y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
                indice = resultado.index(True) # Esta variable busca el index del primer True que encontró

                # Hora de la comparación de los rostros
                if comparador != indice:
                    comparador = indice

                # Si el comparador es igual al indice (Significa que se encontró un rostro)                
                if comparador == indice:
                    for llave in configs.privilegios: # Se usa datos del diccionario para proporcionar color a los cargos de los usuarios
                        if data_list[1] == llave:
                            color = configs.privilegios[llave]
                    cv2.rectangle(camara_procesada, (x1, y1), (x2, y2), color, 3) # SE hará un rectangulo alrededor del rostro encontrado
                    cv2.rectangle(camara_procesada, (x1, y2-35), (x2, y2), color, cv2.FILLED) # Se hara un rectangulo abajo del tostro encontrado, y se va a rellemar del color verde
                    cv2.putText(camara_procesada, data_list[0], (x1+6, y2-6), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2) # Se pondrá un texto que contendrá los nombres del usuario encontrado
                    status = dataexc.registrar_asistencia(["dni", "fecha_registro", "hora_registro"], dni_encontrado)
                    if status: # Si no ocurrió un error durante el proceso del registro, se mostrará lo siguiente
                        cv2.putText(camara_procesada, "Tu asistencia fue registrada!", (x1-6, y1-6), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2) # Se va a poner un texto de notificacion arriba del rostro encontrado
                    else: # Caso contrario, se le va a notificar
                        cv2.putText(camara_procesada, "OCURRIÓ UN ERROR AL REGISTRARTE", (x1-6, y1-6), cv2.FONT_HERSHEY_SIMPLEX, 0.6, configs.rojo, 2) # Se va a poner un texto de notificacion arriba del rostro encontrado

            # SI EL ROSTRO ENCONTRADO NO ESTÁ REGISTRADO se va a ejecutar éste Else
            else:
                y1, x2, y2, x1 = rostro_localizacion
                # Escala
                y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
                cv2.rectangle(camara_procesada, (x1, y1), (x2, y2), configs.rojo, 3)
                cv2.rectangle(camara_procesada, (x1, y2-35), (x2, y2), configs.rojo, cv2.FILLED)
                cv2.putText(camara_procesada, "DESCONOCIDO", (x1+6, y2-6), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        (respuesta_booleano, video_codificado) = cv2.imencode(".jpg", camara_procesada) # La función imencode() devuelve dos valores: un flag booleano que indica si la codificación fue exitosa o no y la imagen codificada en formato JPEG. Estos dos valores se asignan a las variables "respuesta_booleano" y "video_codificado", respectivamente.
        if not respuesta_booleano:
            continue
        yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(video_codificado) + b'\r\n') # La instrucción "yield" es lo que permite enviar la imagen codificada en JPEG a la aplicación web. La instrucción "yield" permite que la función generadora envíe un dato a la aplicación web y luego suspenda su ejecución hasta que se le pida enviar otro dato. De esta manera, la función generadora puede enviar datos en tiempo real a la aplicación web.

# ESCOGE UN CONSEJO ALEATORIO CADA VEZ QUE EL SISTEMA SEA INICIADO
consejo = random.choice(configs.lista_consejos)
print (GG+"["+WW+"*"+GG+"] UN CONSEJO DE LA LISTA FUÉ SELECCIONADO SATISFACTORIAMENTE.")

# -------------- COMENZANDO CON EL PROCESAMIENTO DE LA PÁGINA, Y EL VIDEO CON FLASK -------------------
@pagina.route('/') # Si alguien entra a la ruta / de la pagina, se va a ejecutar index.html
def index():
    return render_template('index.html', aviso=respuesta_f, consejo=consejo, color=tipo_f, mensaje_birth="El día de hoy hay "+str(respuesta[0])+" cumpleaños.", usuarios_cumpleaños=respuesta[1], conteo_birth=respuesta[0])

@pagina.route("/video_feed") # Esto hará que el video sea transmitido a base del detector de rostros
def video_feed():
    return Response(detector_rostros(),
        mimetype = "multipart/x-mixed-replace; boundary=frame")

# ----------------------------- INICIADOR DE LA PAGINA WEB ------------------
if __name__ == "__main__":
    print (GG+"["+WW+"*"+GG+"] LA PÁGINA FUÉ INICIADA SATISFACTORIAMENTE\n"+WW)
    pagina.run(port=configs.puerto_web, debug=configs.debug_status)

# En el código que se ha proporcionado, la función release() se llama después de que se haya procesado la imagen de la cámara web y se haya enviado a la aplicación web. De esta manera, se libera el recurso de la cámara una vez que ya no se necesita y se permite que otros programas puedan utilizarla.
camara.release()