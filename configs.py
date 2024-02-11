1.0
# Este archivo va a contener valores de variables para una manipulacion de datos más comoda
# ----- VARIABLES PARA LA BASE DE DATOS ------------
host = "localhost"
port = 3306
user = "root"
password= ""
database = "usuarios_la_salle"

# ----- VARIABLES GENERALES -----------
puerto_web = 3000
version = "1.0"
directorio_usuarios = "static/rostros" # ruta para acceder a los rostros - CADA IMAGEN DEBE TENER EL DNI DEL USUARIO
numero_camara = 0 # EL NUMERO DE CAMARA ES EL NÚMERO DE CAMARA QUE SERÁ ASIGNADA PARA EL DETECTOR, POR DEFECTO, ES 0, ES DECIR, LA CAMARA QUE VIENE POR DEFECTO EN LA LAPTOP
puerto_web = 3000 # EL PUERTO EN EL QUE SE VA A EJECUTAR LA PAGINA WEB
debug_status = False # EL ESTADO DEL DEBUG, SE USA PARA ANALIZAR PROBLEMAS [PERO CON EL VIDEO, AL ACTIVAR EL DEBUG, NO SE VA A PROCESAR LA IMAGEN CORRECTAMENTE]
lista_consejos = ["Es mejor fallar en el intento, que no intentarlo.", 
            "La práctica hace al maestro.", 
            "La única persona que no comete errores, es la que no hace nada.", 
            "La mejor forma de resolver problemas es enfrentándolos.", 
            "Vive cada día de tu vida como si llegase a ser el último.",
            "Me pregunto... ¿Existe algo realmente aleatorio?.",
            "La vida no tiene sentido, el sentido lo pones tú mismo!.",
            "Una persona aprende más haciendo preguntas, que ofreciendo respuestas.",
            "Eres el resultado de tus propias decisiones.",
            "Las oportunidades pasan, no repasan.",
            "Nunca te dejes limitar por la limitada imaginación de los demás.",
            "Mira tus fracasos como un principio o el medio, pero nunca como un fin.",
            "La única forma de hacer las cosas bien, es hacerlo tú mismo."]

# ----------------- DEFINIENDO COLORES A LOS CUADROS -> BLUE, GREEN, RED -> BGR ----------------------
verde = (0, 255, 0)
azul = (255, 0, 0)
amarillo = (0, 255, 255)
morado = (255, 0, 255)
celeste = (255, 255, 0)
dorado = (0, 215, 255)
gris = (128, 128, 128)
negro = (0, 0, 0)
rojo = (0, 0, 255)
naranja = (0, 140, 255)

# -------------- TIPOS DE PRIVILEGIOS EN LA DETECCIÓN DEL ROSTRO DE LOS USUARIOS ---------------------
privilegios = {
    "Estudiante": verde,
    "Profesor": celeste,
    "Director": amarillo,
    "PP_FF": morado,
    "Personal_adicional": azul,
    "Auxiliar": naranja,
}

# --------- NOMBRES DE LAS TABLAS ---------
tabla_asistencia = "registro_asistencia"
tabla_usuarios = "data_users"