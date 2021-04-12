import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
import random
import numpy as np

class Cromosoma:
        genotype=''
        fenotype=''
        aptitud=''
        pc=''

        def __init__(self,genotype,fenotype,aptitud):
            self.genotype=genotype
            self.fenotype=fenotype
            self.aptitud=aptitud

        def mostrar(self):
            print(self.genotype + '-'+str(self.fenotype) + '-'+str(self.aptitud) + '-'+str(self.pc))

        def __gt__(self, cromosoma):
            return self.aptitud > cromosoma.aptitud

class ag_estandar(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("Interfaz.ui", self)
        self.generacional.clicked.connect(self.evaluacionGeneracional)
    
    def calculateFenotype_gray(self,genotype):
        aux_bin=genotype[0]
        for bit in range(1,len(genotype)):
            aux_bin+=str(int(aux_bin[bit-1])^int(genotype[bit]))
        return int(aux_bin,2)

    def generateGenotype_gray(self, ran):
        len_cromosoma=round(np.log2(ran))
        genotype=""
        for alelo in range(len_cromosoma):
            aux=random.random()
            if aux>0.5:
                genotype+='1'
            else:
                genotype+='0'
        return genotype

    def generatePrimGen(self,len_poblation,len_cromosoma,f):
        poblation=[]
        for cromosoma in range(len_poblation):
            genotype=generateGenotype_gray(len_cromosoma)
            x=calculateFenotype_gray(genotype)
            aptitud=eval(f)
            cromosoma=Cromosoma(genotype,x,aptitud)
            poblation.append(cromosoma)
        return poblation

    def cruza(self,fathers):
        nextgensons=[]
        for father in range(0,len(fathers),2):
            pcorte=random.randint(1,len(fathers[father].genotype)-1)
            #print(pcorte)
            son=Cromosoma(fathers[father].genotype[:pcorte] + fathers[father+1].genotype[pcorte:],'','')
            son2=Cromosoma(fathers[father+1].genotype[:pcorte] + fathers[father].genotype[pcorte:],'','')
            nextgensons.append(son)
            nextgensons.append(son2)
        return nextgensons

    def mutacionbit(self,poblation):
        for individuo in poblation:
            for bit in range(0,len(individuo.genotype)):
                pm=random.random()
                if pm<0.3:
                    individuo.genotype=individuo.genotype[:bit]+str(int(individuo.genotype[bit])^1)+individuo.genotype[bit+1:]
                #print(individuo.genotype,'-',pm,'-',bit)
        return poblation

    def peoresIndividuos(self,poblation):
        spob=poblation
        spob=sorted(spob)
        return spob[0]

    def newGeneration(self,poblation,f):
        probaCruza(poblation)
        fathersnextgen=[]
        while len(fathersnextgen) < len(poblation):
            pemp=random.random()
            sumpemp=0
            for individuo in poblation:
                if sumpemp<pemp and pemp<individuo.pc:
                    #print(pemp," ",sumpemp," ",individuo.pc)
                    fathersnextgen.append(individuo)
                    break
                sumpemp+=individuo.pc
        pcnextgen=random.random()
        if pcnextgen>0.7:
            return fathersnextgen
        nextgen=cruza(fathersnextgen)
        nextgen=mutacionbit(nextgen)
        for individuo in nextgen:
            individuo.fenotype=calculateFenotype_gray(individuo.genotype)
            x=individuo.fenotype
            individuo.aptitud=eval(f)
        return nextgen

    def probaCruza(self,poblation):
        sumpc=0
        for individuo in poblation:
            sumpc+=individuo.aptitud
        for individuo in poblation:
            individuo.pc=individuo.aptitud/sumpc

    def evalucionExtintiva(self,tam_poblation,rango):
        ##
        return

    def evaluacionGeneracional(self):
        f='x**2'
        tam_poblation=int(self.t_pob_gen.text())
        rango=int(self.rango_gen.text())
        generations=int(self.ngeneraciones.text())
        minimos=[]
        generation=generatePrimGen(tam_poblation,rango,f)
        minimos.append(peoresIndividuos(generation))
        while len(minimos)<=generations:
            nextgeneration=newGeneration(generation,f)
            minimos.append(peoresIndividuos(nextgeneration))
            generation=nextgeneration
        print(minimos)
        return minimos

#Abre la ventana gráfica
if __name__=='__main__':
    app = QApplication(sys.argv)
    GUI = ag_estandar()
    GUI.show()
    sys.exit(app.exec_())
