from Individuo import Individuo
import random
import matplotlib.pyplot as plt
from matplotlib import colors

import numpy as np
import pandas as pd
import streamlit as st 



def create_colormap(rgb):
    cell_colors=[(0,0,0),(255,255,255),rgb]
    cell_colors=[(float(element[0])/255.0, float(element[1])/255.0,float(element[2])/255.0) for element in cell_colors]
    cmap=colors.ListedColormap(cell_colors)
    return cmap


def Generar_poblacion(num_poblacion, num_reinas):
    
    cromosoma = []
    poblacion = []

    for i in range(1, (num_poblacion*num_reinas)+1):

        if i % num_reinas == 0:

            cromosoma.append(random.randint(1,num_reinas))

            ind = Individuo(cromosoma)
            #ind.Generar_fenotipo()
            ind.Generar_Aptitud()
            poblacion.append(ind)
            cromosoma = []
        else:
            cromosoma.append(random.randint(1,num_reinas))

    return poblacion

def Seleccion_Torneo(poblacion):
    
    seleccion = []
    
    for i in range(0,len(poblacion),2):
        
        contrincante_1 = poblacion.pop()
        contrincante_2 = poblacion.pop()
        
        if contrincante_1.aptitud <= contrincante_2.aptitud:
            
            seleccion.append(contrincante_1)
        else:
            seleccion.append(contrincante_2)
            
    if len(seleccion)%2:
        seleccion.append(contrincante_2)
    
    return seleccion

def Cpunto(p1,p2):
    
    x = random.randint(1, (len(p1)-1))
    h1 = [] 
    h2 = []
    for i in range(x):
        h1.append(p1[i]) 
        h2.append(p2[i])
    for n in range(x,len(p2)): 
        h1.append(p2[n])
        h2.append(p1[n])
    return h1, h2

def Cruza_Punto(poblacion):
        
    Hijos = []

    for i in range(len(poblacion)):
        if i%2 == 0:
            hijo1 = Individuo()
            hijo2 = Individuo()
            hijo1.genotipo, hijo2.genotipo = Cpunto(poblacion[i-1].genotipo, poblacion[i].genotipo)
           
            Hijos.append(hijo1)
            Hijos.append(hijo2)

    return Hijos

def mutacion_scramble(ind):
    #aux=[]
    inf=random.randint(0,len(ind.genotipo)-1)
    sup=random.randint(inf,len(ind.genotipo)-1)
    random.shuffle(ind.genotipo[inf:sup:])
    # for i in range(inf,sup):
    #     ind.genotipo[i]=aux.pop()
    ind.Generar_Aptitud()
    
def mejorIndividuo(poblation):
    spob=poblation
    spob=sorted(spob)
    return spob[0]

def peorIndividuo(poblation):
    spob=poblation
    spob=sorted(spob)
    return spob[len(poblation)-1]


if __name__ == "__main__":

    num_reinas=8

    a=[1, 0, 1, 0 ,1, 0, 1, 0,
    0, 1, 0, 1, 0, 1, 0, 1,
    1, 0, 1, 0 ,1, 0, 1, 0,
    0, 1, 0, 1, 0, 1, 0, 1,
    1, 0, 1, 0 ,1, 0, 1, 0,
    0, 1, 0, 1, 0, 1, 0, 1,
    1, 0, 1, 0 ,1, 0, 1, 0,
    0, 1, 0, 1, 0, 1, 0, 1]

    tablero=np.reshape(a,(8,8))

    cmap=create_colormap((255,0,0))

    st.title('Practica 3 Algoritmos Geneticos')
    st.text('''Equipo: 
                Contreras Mercado Jorge Armando
                Jesús Eduardo Angeles Hernandez
                Alexia Monserrat Rodríguez Peña
                Seleccion por torneo, Cruza por un punto y Mutación scramble''')

    
    CRUZA = 0.8
    MUTACION = 1-CRUZA
    
    # opc = int(input('''

    #         Selecciona la función (escribe número).

    #         1. f(x) = x^2
    #         2. f(X) = |(x-5)/2+sin(x)|
    #         3. f(x) = (e^x - e^-x) 
    # '''))
    st.sidebar.title('Parametros de generacion')
    
    # opc = st.sidebar.selectbox('''

    #         Selecciona la función fitness\n

    #         1. f(x) = x^2\n
    #         2. f(X) = |(x-5)/2+sin(x)|\n
    #         3. f(x) = (e^x - e^-x) \n
    # ''',
    # (1,2,3)
    # )

    # num_poblacion = int(input("Número de población \n"))
    # num_generacion =  int(input("Numero de Generaciones \n"))
    # num_reinas =  int(input("Tamaño de los alelos \n"))
    
    num_poblacion = st.sidebar.text_input('Número de población: ',value='0')
    num_poblacion = int(num_poblacion)
    
    # num_generacion = st.sidebar.text_input('Número de Generaciones',value='0')
    # num_generacion = int(num_generacion)
    
    # num_reinas = st.sidebar.text_input('Tamaño de los alelos',value='0')
    # num_reinas = int(num_reinas)    
    
    poblacion = []
    
    poblacion = Generar_poblacion(num_poblacion,num_reinas)
    
    # for ind in poblacion:
    #     print(ind.genotipo, ind.fenotipo, ind.aptitud)
        
    mejores=[]

    while(len(poblacion)>2):
          
        seleccion = []
        Hijos = []

        seleccion=Seleccion_Torneo(poblacion)
        
        # print("Individuos seleccionados: ")
        # for ind in seleccion:
        #     print(ind.genotipo, ind.fenotipo, ind.aptitud)
        
        Hijos = Cruza_Punto(seleccion)
 

        mutacion_scramble(peorIndividuo(Hijos))

        for ind in Hijos:
            ind.Generar_Aptitud() 
        
        # st.write(f"Hijos de la generacion {i+1}")
        # print(ind.genotipo, ind.fenotipo, ind.aptitud)

        # print(f"Mutantes de la generacion {i+1}")

        poblacion = Hijos

        #print("Aptitud maxima local de población",max(aptitudes))
        #print("Aptitud minima local de población",min(aptitudes))

        mejor_gen=mejorIndividuo(poblacion)
        mejores.append(mejor_gen)
        if mejor_gen.aptitud==0:
            print("ENCONTRADO")
            break


    if(mejorIndividuo(poblacion).aptitud < mejorIndividuo(mejores).aptitud):
        solucion=mejorIndividuo(poblacion)
    else:
        solucion=mejorIndividuo(mejores)



            
    #if solucion:


    if solucion.aptitud==0:
        st.write(f'''
                    Solucion
                    ''')
    else:
        st.write(f'''
                    Individuo mas cercano a la solucion
                    ''')
    print(solucion.aptitud)
    print(solucion.genotipo)
    for i in mejores:
        print(i.aptitud)
    for col in range(0,len(solucion.genotipo)):
        fila=solucion.genotipo[col]-1
        tablero[fila][col]=2
    fig, ax = plt.subplots()
    im = ax.imshow(tablero, cmap, aspect="equal")
    st.pyplot(fig)


    # else:
    #     st.write(f'''

    #                 NO se encontro
            
    #               ''')
    
    