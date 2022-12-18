padrao = ""
i = 0
retorno = 0
cont = 0

def match(token):
    global i
    global cont
   
    if token == padrao[i]:
        i = i + 1
        cont = cont + 1
    else:
        print("erro")
        exit(-1)

def prox(): 
    return padrao[i]

def A():
    if prox() == 'b':
        match('b')
        A()

#S-> aAa
#A-> bA | epsilon

def S():
    match('a')
    A()
    match('a')
    

def main():
    global padrao

    padrao = input("digite a cadeia\n")
    S()
    if cont == len(padrao):
        print("Sim") 
    else:
        print("Nao")
main()