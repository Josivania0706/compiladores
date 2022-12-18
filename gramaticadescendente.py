padrao = "ccb"
i = 0
retorno = 0

def match(token):
    
    global i
    print('token ', token)
    print('padrao ', padrao[i])

    if token == padrao[i]:
        print('ok')
        i = i + 1
    else:
        print("erro")
        exit(-1)

def prox(): 
    return padrao[i]

def S1():
    if prox() == 'd':
        match('d')
    elif prox() == 'b':
        match('b')
    else: 
        print("Erro no else do s1")
        exit(-1)

def A1():
    if prox() == 'a':
        match('a')
        match('b')
        A1()

def A():
    match('c')
    A1()

def S():
    
    
    match('c')
    A()
    #i = retorno
    S1()
    print("Sucesso!!!!!")

S()