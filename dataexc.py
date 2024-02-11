""" ARCHIVO QUE VA A TENER FUNCIONES DESTINADAS A USAR LA BASE DE DATOS """
# Este archivo va a contener funciones para operar con la base de datos
#import mariadb
import configs
import datetime
import requests

def conectarse():
    # Creando la conexion de la db
    conector = mariadb.connect(
        host = configs.host,
        port = configs.port,
        user = configs.user,
        password= configs.password,
        database = configs.database,
    )

    # Creando el cursor
    cursor = conector.cursor()
    return cursor, conector

# ------------- DISEÑANDO LAS FUNCIONES PARA EL SISTEMA --------------

# Funcion para buscar x datos de las columnas de las bases de datos
# Ésta funcion puede usarse cuando se quiere buscar datos de un usuario
def busqueda(data, columna, user_data): # DATA DEBE SER UNA LISTA DE LO QUE SE BUSCA
    cursor, conector = conectarse() # Con esta operacion extraemos el cursor y el conector de la database
    data = ", ".join(data)
    consulta = "SELECT {} FROM {} WHERE {} = {}".format(data, configs.tabla_usuarios, columna, user_data)
    cursor.execute(consulta)
    # Indexando los resultados
    indexador = cursor.fetchall()
    cursor.close()
    conector.close()
    return indexador[0] # RETORNA UNA LISTA DE DATOS EN ORDEN RESPECTIVO A LOS SOLICITADOS


# Funcion para verificar si un usuario se registró un mismo día o no
def verificar_asistencia(busqueda_data, valor_data, columna_fecha):
    cursor, conector = conectarse() # Con esta operacion extraemos el cursor y el conector de la database
    consulta = "SELECT COUNT(*) FROM {} WHERE {}='{}' AND {} = {};".format(configs.tabla_asistencia, busqueda_data, valor_data, columna_fecha, "CURDATE()") # Consulta
    cursor.execute(consulta) # Se realiza la consulta de los datos necesarios
    # Obtiene el resultado de la consulta
    resultado = cursor.fetchone()
    # Cierra el cursor y la conexión a la base de datos
    cursor.close()
    conector.close()
    # Si el resultado es mayor que cero, significa que el usuario ya se ha registrado en esa fecha
    if resultado[0] > 0:
        return True # El usuario ya está registrado
    else:
        return False # El usuario no se ha registrado


# Funcion para registrar la asistencia al usuario detectado
def registrar_asistencia(data, dni): # Data debe ser una lista de datos que se va a insertar Ejemplo: ["dni", "fecha_registro", "hora_registro"]
    status_usuario = verificar_asistencia("dni", dni, "fecha_registro")
    if status_usuario:
        return True
    else:
        cursor, conector = conectarse() # Con esta operacion extraemos el cursor y el conector de la database
        data = ", ".join(data)
        try:
            consulta = "INSERT INTO {} ({}) VALUES ({}, curdate(), curtime());".format(configs.tabla_asistencia, data, dni) # Consulta
            cursor.execute(consulta) # Se realiza la consulta de los datos necesarios
            conector.commit()
            cursor.close()
            conector.close()
        except Exception as data:
            print (False, "Ocurrió un error en la base de datos", data)
            return False # Si ocurrió un error durante el proceso, se retornará False
        else:
            return True # Caso contrario, se retornará True


# Funcion para verificar si una persona asistió o faltó
def asistencia_conteo():
    cursor, conector = conectarse() # Con esta operacion extraemos el cursor y el conector de la database
    # Seleccionamos el DNI de todos los estudiantes registrados
    consulta = "SELECT dni FROM {} WHERE cargo='Estudiante'".format(configs.tabla_usuarios)
    # Iteramos el resultado
    cursor.execute(consulta)
    iterador = cursor.fetchall()
    # Calcula la fecha de ayer
    ayer = datetime.datetime.now() - datetime.timedelta(days=1)
    fecha_ayer = ayer.strftime('%Y-%m-%d')
    # Verificando si cada DNI de cada estudiante estuvo registrado el día de hoy
    for estudiante in iterador:
        estudiante = estudiante[0]
        consulta = "SELECT COUNT(*) FROM {} WHERE dni='{}' AND fecha_registro = '{}'".format(configs.tabla_asistencia, estudiante, fecha_ayer)
        cursor.execute(consulta) # Se realiza la consulta de los datos necesarios
        # Obtiene el resultado de la consulta
        resultado = cursor.fetchone()
        if resultado[0] > 0:
            query = f"UPDATE {configs.tabla_usuarios} SET asistencias = asistencias + 1 WHERE dni = '{estudiante}'"
            cursor.execute(query)
            conector.commit()  # confirma la transacción
            conector.close()
            cursor.close()
            return True # El usuario ya está registrado
        else:
            query = f"UPDATE {configs.tabla_usuarios} SET inasistencias = inasistencias + 1 WHERE dni = '{estudiante}'"
            cursor.execute(query)
            conector.commit()  # confirma la transacción
            conector.close()
            cursor.close()
            return False # El usuario no se ha registrado

# Verificando si el dispositivo cuenta con internet
import urllib
def tiene_internet():
    try:
        urllib.request.urlopen("http://google.com", timeout=1)
        return True
    except urllib.request.URLError:
        return False

def version_desact():
    rsp = requests.get("https://raw.githubusercontent.com/gjimenezdeza/facial_detector/main/configs.py")
    # Iteramos sobre las líneas de la respuesta
    for line in rsp.iter_lines():
        primer_linea = line
        break
    
    if primer_linea.decode("utf-8") != configs.version:
        return True
    else:
        return False

def verificar_cumpleaños(data_sol):
    cursor, conector = conectarse() # Con esta operacion extraemos el cursor y el conector de la database
    fecha_actual = datetime.datetime.now() # Obtenemos la fecha actual
    fecha_formateada = fecha_actual.strftime('%Y-%m-%d') # Formateamos la fecha actual en el formato 'YYYY-MM-DD'
    data = fecha_formateada.split("-") # Separando los datos
    solicitud = "SELECT {} FROM {} WHERE MONTH(fecha_nacimiento) = {} AND DAY(fecha_nacimiento) = {};".format(data_sol, configs.tabla_usuarios, *data[1:3])
    cursor.execute(solicitud)
    # ---------  Indexador de datos ----------
    index = cursor.fetchall()
    # ---- Cerrando conexion ----------
    conector.close()
    cursor.close()
    if len(index) == 0:
        return (0, None)
    else:
        index_f = [ " ".join(sublista) for sublista in index ]
        return (len(index), index_f)
