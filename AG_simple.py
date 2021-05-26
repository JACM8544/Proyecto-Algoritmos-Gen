from Individuo import Individuo
from Funciones_seleccion import *
from Funciones_Cruza import *
from Funciones_Mutacion import *
from Funciones_math import *
import math
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd
import streamlit as st 

def Generar_poblacion(num_poblacion, num_alelos, opc):
    
    cromosoma = []
    poblacion = []

    for i in range(1, (num_poblacion*num_alelos)+1):

        if i % num_alelos == 0:

            if random.random() > 0.5:
                cromosoma.append(1)
            else:
                cromosoma.append(0)

            ind = Individuo(cromosoma)
            ind.Generar_fenotipo()
            ind.Generar_Aptitud(opc)
            poblacion.append(ind)
            cromosoma = []
        else:
            if random.random() > 0.5:
                cromosoma.append(1)
            else:
                cromosoma.append(0)

    return poblacion

    

if __name__ == "__main__":

    st.title('Practica 2 Algoritmos Geneticos')
    st.text('''Equipo: 
                Contreras Mercado Jorge Armando
                Jesús Eduardo Angeles Hernandez
                Alexia Monserrat Rodríguez Peña
Sobrante estocástico con reemplazo, Cruza por dos puntos y Mutación heurística''')

    
    CRUZA = 0.8
    MUTACION = 1-CRUZA
    
    # opc = int(input('''

    #         Selecciona la función (escribe número).

    #         1. f(x) = x^2
    #         2. f(X) = |(x-5)/2+sin(x)|
    #         3. f(x) = (e^x - e^-x) 
    # '''))
    st.sidebar.title('Parametros de generacion')
    
    opc = st.sidebar.selectbox('''

            Selecciona la función fitness\n

            1. f(x) = x^2\n
            2. f(X) = |(x-5)/2+sin(x)|\n
            3. f(x) = (e^x - e^-x) \n
    ''',
    (1,2,3)
    )

    # num_poblacion = int(input("Número de población \n"))
    # num_generacion =  int(input("Numero de Generaciones \n"))
    # num_alelos =  int(input("Tamaño de los alelos \n"))
    
    num_poblacion = st.sidebar.text_input('Número de población: ',value='0')
    num_poblacion = int(num_poblacion)
    
    num_generacion = st.sidebar.text_input('Número de Generaciones',value='0')
    num_generacion = int(num_generacion)
    
    num_alelos = st.sidebar.text_input('Tamaño de los alelos',value='0')
    num_alelos = int(num_alelos)
    
    
    opc_seleccion = 3
    
    
    opc_cruza = 2


    opc_mutacion = 5
    
    
    
    poblacion = []
    
    poblacion = Generar_poblacion(num_poblacion,num_alelos,opc)
    
    # for ind in poblacion:
    #     print(ind.genotipo, ind.fenotipo, ind.aptitud)
        
    maximostotales=[]

    for i in range(num_generacion):
        
        st.write(f'''
                
                Generacion numero {i+1}
            
              ''')
          
        seleccion = []
        Hijos = []
        
        # opc_seleccion = int(input('''
        #                       Elige el tipo de seleccion:
                              
        #                       1. Ruleta.
        #                       2. Sobrante estocástico sin reemplazo.
        #                       3. Sobrante estocástico con reemplazo.
        #                       4. Seleccion por torneo.

        #                       '''))
          

        if opc_seleccion == 1:
            seleccion = Seleccion_ruleta(poblacion)
        elif opc_seleccion == 2:
            seleccion = Seleccion_SobranteEstocastico_sinReemplazo(poblacion)
        elif opc_seleccion == 3:
            seleccion = Seleccion_SobranteEstocastico_conReemplazo(poblacion)
        elif opc_seleccion == 4:
            seleccion = Seleccion_Torneo(poblacion)
        
        # print("Individuos seleccionados: ")
        # for ind in seleccion:
        #     print(ind.genotipo, ind.fenotipo, ind.aptitud)
            
        seleccion_cruza = seleccion[:int(len(seleccion) * CRUZA)].copy()
        seleccion_mutacion = seleccion[int(len(seleccion) * CRUZA):].copy()
        
        
        # opc_cruza = int(input('''

        #                     Selecciona el tipo de cruza:

        #                     1. Cruza por un punto.
        #                     2. Cruza por dos puntos.
        #                     3. Cruza uniforme
        #                 '''))

        if opc_cruza == 1:

            Hijos = Cruza_Punto(seleccion_cruza)

            # opc_mutacion = int(input('''

            #                 Selecciona el tipo de mutacion:

            #                 1. Mutación aleatoria.
            #                 2. Mutación por intercambio de bit.
            #                 3. Mutación por Inserción.
            #                 4. Mutación por Inserción recíproca.
            #                 5. Mutación heurística.
            #                 '''))        

            if opc_mutacion == 1:

                for ind in seleccion_mutacion:
                    mutacion_desplazamiento(ind)

            elif opc_mutacion == 2:

                for ind in seleccion_mutacion:
                    CMintercambio(ind)

            elif opc_mutacion == 3:

                for ind in seleccion_mutacion:
                    mutacionInsercion(ind)
            
            elif opc_mutacion == 4:
                 for ind in seleccion_mutacion:
                        mutacion_IR(ind)
            
            elif opc_mutacion == 5:
                for ind in seleccion_mutacion:
                        mutacion_IR(ind)   

        elif opc_cruza == 2:

            Hijos = Cruza_Punto(seleccion_cruza)

            # opc_mutacion = int(input('''

            #                 Selecciona el tipo de mutacion:

            #                 1. Mutación aleatoria.
            #                 2. Mutación por intercambio de bit.
            #                 3. Mutación por Inserción.
            #                 4. Mutación por Inserción recíproca.
            #                 5. Mutación heurística.
            #                 '''))

            if opc_mutacion == 1:

                for ind in seleccion_mutacion:
                    mutacion_desplazamiento(ind)

            elif opc_mutacion == 2:

                for ind in seleccion_mutacion:
                    CMintercambio(ind)

            elif opc_mutacion == 3:

                for ind in seleccion_mutacion:
                    mutacionInsercion(ind)
            
            elif opc_mutacion == 4:
                 for ind in seleccion_mutacion:
                        mutacion_IR(ind)
            
            elif opc_mutacion == 5:
                for ind in seleccion_mutacion:
                        mutacion_IR(ind)   
        
        elif opc_cruza == 3:
            
            Hijos = Cruza_Uniforme(seleccion_cruza)

            # opc_mutacion = int(input('''

            #                 Selecciona el tipo de mutacion:

            #                 1. Mutación aleatoria.
            #                 2. Mutación por intercambio de bit.
            #                 3. Mutación por Inserción.
            #                 4. Mutación por Inserción recíproca.
            #                 5. Mutación heurística.
            #                 '''))

            if opc_mutacion == 1:

                for ind in seleccion_mutacion:
                    mutacion_desplazamiento(ind)

            elif opc_mutacion == 2:

                for ind in seleccion_mutacion:
                    CMintercambio(ind)

            elif opc_mutacion == 3:

                for ind in seleccion_mutacion:
                    mutacionInsercion(ind)
            
            elif opc_mutacion == 4:
                 for ind in seleccion_mutacion:
                        mutacion_IR(ind)
            
            elif opc_mutacion == 5:
                for ind in seleccion_mutacion:
                        mutacion_IR(ind)                
                
        
        # st.write(f"Hijos de la generacion {i+1}")
        for ind in Hijos:
            ind.Generar_Aptitud(opc)
            # print(ind.genotipo, ind.fenotipo, ind.aptitud)

        # print(f"Mutantes de la generacion {i+1}")
        for ind in seleccion_mutacion:
            ind.Generar_Aptitud(opc)
            

        Hijos.extend(seleccion_mutacion)
        poblacion = Hijos.copy()

        aptitudes = []
        for i in poblacion:
          aptitudes.append(i.aptitud)   
        
        #print("Aptitud maxima local de población",max(aptitudes))
        #print("Aptitud minima local de población",min(aptitudes))
        maximostotales.append(max(aptitudes))

        graficar(poblacion)
        
        col1, col2 = st.beta_columns(2)
        
        with col1:
        
            df = pd.DataFrame(columns=['Fenotipo','Genotipo','Aptitud'], index=range(len(poblacion)))
            
            for i in range(len(poblacion)):
                df.iloc[i] = [poblacion[i].fenotipo, poblacion[i].genotipo, poblacion[i].aptitud]     

            df
        
        with col2:
            
            st.line_chart(aptitudes)
            
        
        
        random.shuffle(poblacion)

    st.write(f'''
                
                Maximos obtenidos
            
              ''')
    
    arreglo_y = maximostotales
    arreglo_x = [i for i in range(0,num_generacion)]

    col1, col2 = st.beta_columns(2)
        
    with col1:
        
        df = pd.DataFrame(columns=['Aptitud'], index=range(0, num_generacion))
            
        for i in range(0, num_generacion):
            df.iloc[i] = [maximostotales[i]]     

        df
            
    with col2:
            
        st.line_chart(maximostotales, use_container_width=True)
    
    