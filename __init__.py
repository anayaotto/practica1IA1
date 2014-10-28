import sys
import csv
from random import randint
li1=[]
li2=[]
li3=[]
li4=[]
li5=[]
liTheta=[]
arregloThetas=[]
def main():


    if len(sys.argv)>4:
        #print sys.argv[1]
        #print sys.argv[2]
        #print sys.argv[3]
        #print sys.argv[4]
        #print sys.argv[5]
        filex = sys.argv[1]
        filey = sys.argv[2]
        alpha = sys.argv[3]
        iteracion = sys.argv[4]
        tolerancia = sys.argv[5]
        #Leyendo X
        fx = open(filex)
        tetaX=0
        for line in fx:
            line=line.replace("\n","")
            linex=line.split(",")
            tetaX=len(linex)
            li1.append(linex)
        #Leyendo Y
        fy=open(filey)
        for line in fy:
            line=line.replace("\n","")
            linex=line.split(",")
            li2.append(linex)


        #recorrer listas
        i=0
        j=0
        m=len(li1)
        print "contenido en lista 1: ",len(li1)
        while i< len(li1):
            while j<(len(li1[i])):
                print li1[i][j]
                j+=1
            i+=1

        #Ejecucion
        #Generando Thetas
        i = 0
        while i<tetaX:
            thetasInit=randint(0,10)
            liTheta.append(thetasInit)
            print("Theta Generada: ",thetasInit)
            i=i+1
        #i=0
        #while i<len(liTheta):
        #    print("Theta en lista: ",liTheta[i])
        #    i=i+1
        cont = 0
        cont1 = 0
        the=0.0
        contador=0
        while contador<iteracion:
            while cont<m:
                while cont1<len(liTheta):
                    the=the+int(liTheta[cont])*(float(li1[cont][cont1]))
                    cont1+=1
                the=the-(float(li2[cont][0]))
                the=the*float(li1[cont][0])
                the=the*float(alpha)*(1/float(m))
                cont+=1
                arregloThetas.append(the)
                print "Thetas salientes: " ,the
            contador+=1



    else:
        print("Debe ingresar la ruta de dos archivos CSV, un paramametro numerico Alpha, un parametro de numero de iteraciones y una tolerancia\n")


if __name__ == '__main__':
    main()
