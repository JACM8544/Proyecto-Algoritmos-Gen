

class Individuo:

    def __init__(self, genotipo = [], fenotipo=0,aptitud = 0 ,apto_cruza = False, prob = 0.0):
        self.genotipo = genotipo
        self.fenotipo = fenotipo
        self.aptitud = aptitud
        self.apto_cruza = apto_cruza
        self.prob = prob


    def Generar_fenotipo(self):
        str_bin = "".join(map(str, self.genotipo))
        self.fenotipo = int(str_bin,2)

    def Generar_Aptitud(self):
        cont_filas=0
        diag_positiva=[]
        cont_diag_pos=0
        diag_negativa=[]
        cont_diag_neg=0
        for col in range(0,len(self.genotipo)):
            cont=self.genotipo.count(self.genotipo[col]) 
            if cont > 1:
                cont_filas+=1
            diag_pos=(col+1)+self.genotipo[col]
            if diag_pos in diag_positiva:
                cont_diag_pos+=1
            else:
                diag_positiva.append(diag_pos)
            diag_neg=(col+1)-self.genotipo[col]
            if diag_neg in diag_negativa:
                cont_diag_neg+=1
            else:
                diag_negativa.append(diag_neg)
        self.aptitud=cont_filas+cont_diag_pos+cont_diag_neg

    def __lt__(self, cromosoma):
        return self.aptitud < cromosoma.aptitud
            

            
        


        
