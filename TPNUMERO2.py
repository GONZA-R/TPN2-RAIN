
#***********************************************************************************************
#***********************************************************************************************
# Aqui comienza las funciones del punto 1

import os
import nltk
import re



##################
import unicodedata
def eliminar_acentos(cadena):
    #Función que recibe una cadena de texto y retorna la misma cadena sin acentos.
    return ''.join(c for c in unicodedata.normalize('NFD', cadena) if unicodedata.category(c) != 'Mn')

##################

def separar_oraciones(parrafo):
    # Tokenizar el párrafo en oraciones
    oraciones = nltk.sent_tokenize(parrafo, language='spanish')
    return oraciones
########################################################
def tokenizar_oraciones(oraciones):
    # Tokenización de cada elemento de la lista
    for i in range(len(oraciones)):
        oraciones[i] = oraciones[i].split()
########################################################



from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk import FreqDist

def procesar_texto(lista_tokenizada, idioma='spanish'):
    # Obtener la frecuencia de cada término en la lista tokenizada
    fd = FreqDist([palabra for oracion in lista_tokenizada for palabra in oracion if palabra.strip() != ''])
    frecuencias = fd.most_common()

    return frecuencias
#############################################################################################################

def eliminar_puntuacion(lista_tokenizada):
    # Expresión regular para coincidir con signos de puntuación en español
    puntuacion_regex = r'[^\w\sáéíóúüñ]'
    
    # Iterar sobre cada lista tokenizada
    for i in range(len(lista_tokenizada)):
        # Reemplazar cada signo de puntuación por una cadena vacía y eliminar espacios en blanco
        lista_tokenizada[i] = [re.sub(puntuacion_regex, '', palabra).strip() for palabra in lista_tokenizada[i]]
    
    return lista_tokenizada


#############################################################################################################
####################################################################

# Aqui guarda los resultado en un archivo de texto

def guardar_frecuencias(frecuencias, nombre_archivo):
    with open(nombre_archivo, 'w') as archivo:
        # Encontrar la longitud de la palabra más larga en la lista
        longitud_maxima = max(len(termino) for termino, frecuencia in frecuencias)
        archivo.write("Frecuencia de cada PALABRA en forma DESCENDENTE\n\n")
        for termino, frecuencia in frecuencias:
            # Ajustar la cantidad de espacios de acuerdo a la longitud de la palabra más larga
            espacios = ' ' * (longitud_maxima - len(termino))
            linea=f'Palabra: "{termino}"{espacios}   Frecuencia: {frecuencia}\n'
            archivo.write(linea)

####################################################################
def eliminar_stopwords(lista_tokenizada, idioma='spanish'):

    stopwords_lista = set(stopwords.words(idioma))
    
    # Filtrar las stopwords de la lista tokenizada
    lista_filtrada = [[palabra for palabra in oracion if palabra.lower() not in stopwords_lista] for oracion in lista_tokenizada]
    
    return lista_filtrada
#####################################################################
############################
#Borrar pantalla
def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')
############################

#Aqui termina las funciones del punto 1

#***********************************************************************************************
#***********************************************************************************************



#Aqui comienza las funciones del punto 2

import nltk
import string
from nltk.corpus import stopwords

def eliminar_puntuaciones(tokens):
    # Obtener los signos de puntuación
    signos_puntuacion = set(string.punctuation)
    
    # Crear una nueva lista sin signos de puntuación
    tokens_sin_puntuacion = [token for token in tokens if token not in signos_puntuacion]
    
    return tokens_sin_puntuacion

####################################################################
def eliminar_stopwords_ingles(tokens):
    # Obtener las stop words en inglés
    stop_words = set(stopwords.words('english'))
    
    # Crear una nueva lista sin stop words
    tokens_sin_stopwords = [token for token in tokens if token.lower() not in stop_words]
    
    return tokens_sin_stopwords
#####################################################################
from nltk.stem import PorterStemmer

def algoritmo_porter(tokens):
    stemmer = PorterStemmer()
    tokens_stemmeado_porter = [stemmer.stem(token) for token in tokens]
    return tokens_stemmeado_porter

#################################################################

from nltk.stem import LancasterStemmer

def algoritmo_lancaster(tokens):
    stemmer = LancasterStemmer()
    tokens_stemmed_lancaster = [stemmer.stem(token) for token in tokens]
    return tokens_stemmed_lancaster

###################################################################################
def guardar_archivos(texto, nombre_archivo,nombre_algoritmo):
    with open(nombre_archivo, 'w') as archivo:
        archivo.write("El algoritmo stemming utilizado es "+nombre_algoritmo+'\r\n')
        archivo.write('\n'.join(texto))
###################################################################################

#Aqui termina las funciones del punto 2

#***********************************************************************************************
#***********************************************************************************************



# Aqui comienza las funciones del punto 3


def eliminar_stopwords_espanol(lista_palabras):
    # Obtenemos las stopwords para español
    stop_words = set(stopwords.words('spanish'))
    
    # Eliminamos las stopwords de la lista de palabras
    lista_sin_stopwords = [palabra for palabra in lista_palabras if not palabra.lower() in stop_words]
    
    return lista_sin_stopwords
###############################################################################################


from nltk.stem import SnowballStemmer

def algoritmo_snowball(lista_palabras):
    # Se crea una instancia del stemmer de Snowball para español
    stemmer = SnowballStemmer("spanish")
    # Aplicamos stemming a cada palabra
    stemmed = [stemmer.stem(palabra) for palabra in lista_palabras]
    
    return stemmed


# Aqui termina las funciones del punto 3

#***********************************************************************************************
#***********************************************************************************************

# Aqui comienza las funciones del punto 4

def obtener_ngramas(texto):
    # Convertimos el texto en una lista de palabras
    palabras = texto.split()
    # Obtenemos los 2-gramas
    bigramas = [palabras[i] + " " + palabras[i+1] for i in range(len(palabras)-1)]
    # Obtenemos los 3-gramas
    trigramas = [palabras[i] + " " + palabras[i+1] + " " + palabras[i+2] for i in range(len(palabras)-2)]
    return bigramas, trigramas


def guardar_ngramas(texto, nombre_archivo,nombre_grama):
    with open(nombre_archivo, 'w') as archivo:
        archivo.write("Resultado para "+nombre_grama+'\r\n')
        archivo.write('\n'.join(texto))





################


while True:
    clear_screen()
    print("Trabajo Practico N°2 Introducción - 2da parte"+"\n\n")
    print("1. Punto 1: Eliminación de stop words y frecuencia de términos con NLTK")
    print("2. Punto 2: Comparación de Stemming en inglés con Porter y Lancaster")
    print("3. Punto 3: Procesamiento de Stemming en Texto 1 en español con NLTK")
    print("4. Punto 4: Obtención de 2-gramas y 3-gramas en el primer párrafo del Texto 1")
    print("5. Salir\n")

    opcion = input("Ingrese una opción: ")
    if opcion == "1":
        """1) Empleando la librería NLTK de Python, elimine las stop_words empleando el idioma español, 
        tokenize el texto anterior, y muestre el resultado con la frecuencia de cada término, ordenado 
        por frecuencia descendente.Tenga en cuenta el hecho de que existen oraciones y párrafos, 
        asegúrese de que el conjunto de términos está bien formado 
        y no se omiten oraciones."""

        clear_screen()

        #################################################################
        # Abre el archivo y lee su contenido
        with open('texto1.txt', 'r', encoding='utf-8') as archivo:
            texto = archivo.read()

        #################################################################

        #Aqui comienza el trabajo


        oraciones=separar_oraciones(texto)  # oraciones es una lista
        tokenizar_oraciones(oraciones) #tokeniza la lista de oraciones


        lista_filtrada = eliminar_stopwords(oraciones, idioma='spanish')#Elimina las stopword
        eliminar_puntuacion(lista_filtrada)#Elimina los signos de puntuacion


        frecuencias = procesar_texto(lista_filtrada)# Calculas las frecuencias

        # Encontrar la longitud de la palabra más larga en la lista
        longitud_maxima = max(len(termino) for termino, frecuencia in frecuencias)
        print("Frecuencia de cada PALABRA en forma DESCENDENTE\n")
        # Imprimir la frecuencia de cada término, ordenado por frecuencia descendente
        for termino, frecuencia in frecuencias:
        # Ajustar la cantidad de espacios de acuerdo a la longitud de la palabra más larga
            espacios = ' ' * (longitud_maxima - len(termino))
            print(f'Palabra: "{termino}"{espacios} Frecuencia: {frecuencia}')

        guardar_frecuencias(frecuencias,"Frecuencias_descendentes.txt")

        print("\nSe generaron archivos de texto...\n")
        input("Presione enter para continuar...")
        pass

    elif opcion == "2":
        """Del texto a continuación, aplique el proceso de eliminación de stop_words en inglés y 
        tokenización, a continuación emplee el proceso de Stemming con los algoritmos de 
        Porter y Lancaster, comparando los resultados de los dos procesos encolumnados(Texto 2):"""

        clear_screen()#Borra pantalla
        # Abre el archivo y lee su contenido
        with open('texto2.txt', 'r', encoding='utf-8') as archivo:
            texto = archivo.read()

        #################################################################

        texto_tokenizado = nltk.word_tokenize(texto)
        texto_tokenizado = eliminar_puntuaciones(texto_tokenizado)
        texto_tokenizado = eliminar_stopwords_ingles(texto_tokenizado)#Elimina las stopword
        #Aqui ya estoy aplicando el algorito de porter para hacer stemming de las palabras

        texto_stemmeado_porter=algoritmo_porter(texto_tokenizado)
        texto_stemmeado_lancaster=algoritmo_lancaster(texto_tokenizado)

        print("Proceso de stemming por el algoritmo de PORTER\n")
        print(texto_stemmeado_porter)
        guardar_archivos(texto_stemmeado_porter,"Stemming_Porter.txt","Algoritmo PORTER")
        print("\nProceso de stemming por el algoritmo de LANCASTER\n")
        print(texto_stemmeado_lancaster)
        guardar_archivos(texto_stemmeado_lancaster,"Stemming_Lancaster.txt","Algoritmo LANCASTER")

        print("\nSe generaron archivos de texto...\n")
        input("Presione enter para continuar...")

        pass


    elif opcion == "3":
        """Aplique el proceso de Stemming para el Texto 1 y muestre el resultado. 
        Advierta si los algoritmos de Porter y Lancaster en NLTK poseen la implementación para el 
        idioma español,sino es así, aplique otro algoritmo que si la posea."""

        clear_screen()
        
        # Abre el archivo y lee su contenido
        with open('texto1.txt', 'r', encoding='utf-8') as archivo:
            texto = archivo.read()

        #################################################################
        texto_tokenizado = nltk.word_tokenize(texto)
        texto_tokenizado = eliminar_puntuaciones(texto_tokenizado)

        
        texto_tokenizado = eliminar_stopwords_espanol(texto_tokenizado)#Elimina las stopword en espanol

        texto_stemmeado_porter=algoritmo_porter(texto_tokenizado)
        texto_stemmeado_lancaster=algoritmo_lancaster(texto_tokenizado)
        texto_stemmeado_snowball=algoritmo_snowball(texto_tokenizado)

        print("\nProceso de stemming del TEXTO 1 por el algoritmo de PORTER\n")
        print(texto_stemmeado_porter)
        guardar_archivos(texto_stemmeado_porter,"Stemming_Porter_texto1.txt","Algoritmo PORTER")

        print("\nProceso de stemming del TEXTO1 por el algoritmo de LANCASTER\n")
        print(texto_stemmeado_lancaster)
        guardar_archivos(texto_stemmeado_lancaster,"Stemming_Lancaster_texto1.txt","Algoritmo LANCASTER")

        print("\nProceso de stemming del TEXTO1 por el algoritmo de SNOWBALL\n")
        print(texto_stemmeado_snowball)
        guardar_archivos(texto_stemmeado_snowball,"Stemming_snowball_texto1.txt","Algoritmo SNOWBALL")
        print("\nSe generaron archivos de texto...\n")
        input("Presione enter para continuar...")

        pass

    elif opcion == "4":
        """Del primer párrafo del Texto 1, 
        obtenga 2-gramas y 3-gramas de palabras, 
        muestre los resultados en cada caso."""
        clear_screen()

        # Abre el archivo y lee su contenido
        with open('texto1.txt', 'r', encoding='utf-8') as archivo:
            texto = archivo.read()
        
        oraciones=separar_oraciones(texto)  # oraciones es una lista
        primer_parrafo=', '.join(oraciones[:7]) #Conseguir el primer parrafo del texto 1

        dosgramas,tresgramas=obtener_ngramas(primer_parrafo)
        print("2-gramas: \n\n",dosgramas)
        guardar_ngramas(dosgramas,"2-gramas.txt","2-gramas")
        print("\n\n")
        print("3-gramas: \n\n",tresgramas)
        guardar_ngramas(tresgramas,"3-gramas.txt","3-gramas")
    
        print("\nSe generaron archivos de texto...\n")
        input("\nPresione enter para continuar...")
        pass
    elif opcion == "5":
        clear_screen()
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida, por favor intente de nuevo.")
