import random 

def listadic():
    global lista
    lista = []
    for i in range(10): 
        lista.append({i: random.randint(0,100)})
    return lista
    
def ordenar(): 
    may = sorted(lista, reverse=True, key=lambda dicts: max(list(dicts.values())))
    print("El mas viejo es: ", may[0])
    print("El mas joven es: ", may[9])
    print("Mayor a menor: " + str(may)) 
    return ("Ordenada ", lista)

print (listadic())
print (ordenar())
