from random import *

def matriz():

    fila=5
    columna=5
    numeros=[[randint(1,4) for a in range(fila)] for b in range(columna)]

    for c in range(fila):
        for d in range(columna):
            print(numeros[c][d], end=' ')
        print()

    for f in range(0,5):
        if (numeros[f][0] == numeros[f][1] and numeros[f][0] == numeros[f][2] and numeros[f][0] == numeros[f][3]):
            print ("Secuencia de 4 numeros iguales en forma horizontal encontrada desde la posición [",f+1,"][",1,"] hasta [",f+1,"][",4,"]")
        if (numeros[f][1] == numeros[f][2] and numeros[f][1] == numeros[f][3] and numeros[f][1] == numeros[f][4]):
            print ("Secuencia de 4 numeros iguales en forma horizontal encontrada desde la posición [",f+1,"][",2,"] hasta [",f+1,"][",5,"]")

    for h in range(0,5):
        if (numeros[0][h] == numeros[1][h] and numeros[0][h] == numeros[2][h] and numeros[0][h] == numeros[3][h]):
            print ("Secuencia de 4 numeros iguales en forma vertical encontrada desde la posición [",h+1,"][",1,"] hasta [",h+1,"][",4,"]")
        if (numeros[1][h] == numeros[2][h] and numeros[1][h] == numeros[3][h] and numeros[1][h] == numeros[4][h]):
            print ("Secuencia de 4 numeros iguales en forma vertical encontrada desde la posición [",h+1,"][",2,"] hasta [",h+1,"][",5,"]")

matriz()