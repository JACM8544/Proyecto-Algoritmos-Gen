from Individuo import Individuo
import random
import matplotlib.pyplot as plt
from matplotlib import colors

import numpy as np
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
    h1=p1[:x]+p2[x:]
    h2=p2[:x]+p1[x:]
    return h1, h2

def Cruza_Punto(poblacion):
        
    Hijos = []

    for i in range(0,len(poblacion),2):
        hijo1 = Individuo()
        hijo2 = Individuo()
        hijo1.genotipo, hijo2.genotipo = Cpunto(poblacion[i].genotipo, poblacion[i+1].genotipo)
        Hijos.append(hijo1)
        Hijos.append(hijo2)

    return Hijos

def mutacion_scramble(ind):
    #aux=[]
    inf=random.randint(0,len(ind.genotipo)-1)
    sup=random.randint(inf,len(ind.genotipo)-1)
    random.shuffle(ind.genotipo[inf:sup:])
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
    
    st.sidebar.title('Parametros de generacion')
    
    
    num_poblacion = st.sidebar.text_input('Número de población: ',value='0')
    num_poblacion = int(num_poblacion)
    
    # num_generacion = st.sidebar.text_input('Número de Generaciones',value='0')
    # num_generacion = int(num_generacion)
    
    # num_reinas = st.sidebar.text_input('Tamaño de los alelos',value='0')
    # num_reinas = int(num_reinas)    
    
    poblacion = []
    
    poblacion = Generar_poblacion(num_poblacion,num_reinas)
    
        
    mejores=[]

    while(len(poblacion)>2):
          
        seleccion = []
        Hijos = []

        seleccion=Seleccion_Torneo(poblacion)
        
        Hijos = Cruza_Punto(seleccion)
 

        mutacion_scramble(peorIndividuo(Hijos))

        for ind in Hijos:
            ind.Generar_Aptitud() 
        
        aux=[]
        for i in range(0,len(Hijos)):
            if seleccion[i].aptitud < Hijos[i].aptitud:
                aux.append(seleccion[i])
            else:
                aux.append(Hijos[i])

        poblacion = aux

        mejor_gen=mejorIndividuo(poblacion)
        mejores.append(mejor_gen)
        if mejor_gen.aptitud==0:
            break


    if(mejorIndividuo(poblacion).aptitud < mejorIndividuo(mejores).aptitud):
        solucion=mejorIndividuo(poblacion)
    else:
        solucion=mejorIndividuo(mejores)



    if solucion.aptitud==0:
        st.write(f'''
                    Solucion Encontrada!!!
                    ''')
    else:
        st.write(f'''
                    Solución no encontrada: Mostrando individuo mas cercano a la solucion
                    ''')
    for col in range(0,len(solucion.genotipo)):
        fila=solucion.genotipo[col]-1
        tablero[fila][col]=2
    fig, ax = plt.subplots()
    im = ax.imshow(tablero, cmap, aspect="equal")
    st.pyplot(fig)


    
    