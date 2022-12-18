m  = {
    "E (":["T", "E'"],
    "E id":["T", "E'"],
    "E' +":["+","T", "E'"],
    "E' )":["_"],
    "E' $":["_"],
    "T (":["F", "T'"],
    "T id":["F", "T'"],
    "T' +":["_"],
    "T' *":["*", "F", "T'"],
    "T' )":["_"],
    "T' $":["_"],
    "F (":["(", "E", ")"],
    "F id":["id"]
}

terminais = {"id", "(", " )", "+", "*"}
w = ['id', "+", "id", "*", "id", "$"]
posEntrada = 0
pilha = ['E', '$']

def algoritmo():
    global posEntrada
    ip = 0

    X =  pilha[0]
    while( X[0] != "$"):
        a = w[ip]
        if(X == a):
            ip = ip + 1
            pilha.pop(0) 
        elif X in terminais:
            exit(1)
        elif m.get(f'{X} {a}') == None:
            exit(1)
        else:
            pilha.pop(0)
            listaAux = m.get(f'{X} {a}')
            for i in range(0,len(listaAux)):
                if listaAux[i] != "_":
                    pilha.insert(i, listaAux[i])
        print("Pilha ", pilha)
        print("Entrada ", w[ip:]) 
        print()  
             
        X = pilha[0]
algoritmo()
