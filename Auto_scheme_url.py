__author__ = 'CyberIOps'
__mail__ = ''
__project_url__ = 'https://github.com/CyberIOps/auto_url_scheme'
__date__ = '2024'
__version__ = '1.0.0'
__description__ = 'Processes a list of paths from a text file and generates complete URLs by appending a specified domain and scheme (http)'

# VERSIONES:
# 1.0.0 version inicial.

# INSTALACION:

# SUGERENCIAS:

# BUGS DETECTADOS:

# Solicitar al usuario el dominio
import os

def esquema_url(txt_source, txt_final, dominio):
    try:
        # Comprobar si existe el archivo de entrada o source
        if not os.path.exists(txt_source):
            print(f"El archivo {txt_source} no existe.")
            return

        # Abrir el source en modo lectura
        with open(txt_source, 'r') as txt_entrada:
            # Abrir el archivo de salida para escribir
            with open(txt_final, 'w') as txt_salida:
                # Recorremos cada linea del source para sanearla
                for linea in txt_entrada:
                    # Eliminar espacios y saltos de línea
                    ruta = linea.strip()

                    # Si hay lineas en blanco se ignoran
                    if not ruta:
                        continue

                    if dominio:
                        url_completa = f"http://{dominio}/{ruta}"
                    else:
                        # Si no se hay dominio, se añade solo el esquema a la URL original
                        url_completa = f"http://{ruta}"

                    # Escribir la URL completa en el txt de salida
                    txt_salida.write(url_completa + '\n')

        print(f"Proceso completado. Las URLs generadas se han guardado en {txt_final}")

    except Exception as e:
        print(f"Error: {e}")
        print(f"Proceso completado. Las URLs generadas se han guardado en {txt_final}")


# Configuración de los archivos y el dominio
txt_fuente = "doms.txt"
txt_resultados = "schemed_doms.txt"
ver = "1.0.0"
print(f"\nAuto URL Scheme {ver}\n")
dominio = input("Introduce el dominio (e.g., dominio.tld) o déjalo en blanco: ")

# Llamar a la función para procesar las rutas
esquema_url(txt_fuente, txt_resultados, dominio)
