import pandas as pd

tabela  = {
    "S 0":["0", "A", "1"],
    "S b":["B"],
    "A a":["a", "A"],
    "A 1":["_"],
    "B b":["b"]
}
tabelaSintatica = []
terminais = ["a", "0", "1", "b"]
cadeia = '0aa1$'
pilha = ['S', '$']
acao = ''

def algoritmo():
    global  acao
    indexCadeia = 0
    elemPilha =  pilha[0]
    a = ''
    while(elemPilha != "$"):
        a = cadeia[indexCadeia]

        if(elemPilha == a):
            acao = f'Match({a})'
            tabelaSintatica.append([str(pilha).strip('[]'), cadeia[indexCadeia:], acao])
            indexCadeia = indexCadeia + 1
            pilha.pop(0) 
        elif elemPilha in terminais:
            print("Cadeia não aceitaa")
            exit(1)
        elif tabela.get(f'{elemPilha} {a}') == None:
            print("Cadeia não aceitaaa")
            exit(1)
        else:
            listaAux = tabela.get(f'{elemPilha} {a}')
            acao = f'{elemPilha} -> {listaAux}'
            tabelaSintatica.append([str(pilha).strip('[]'), cadeia[indexCadeia:], acao])
            pilha.pop(0)
            
            for i in range(0,len(listaAux)):#salvar  a gramatica na pilha
                if listaAux[i] != "_":
                    pilha.insert(i, listaAux[i])

        elemPilha = pilha[0]
    
    a = cadeia[indexCadeia]
    if elemPilha == "$" and  a  == "$": 
        acao = "ok"
        tabelaSintatica.append([str(pilha).strip('[]'), cadeia[indexCadeia:], acao])  
    else:
        print("Cadeia não aceita")

    df = pd.DataFrame(tabelaSintatica, columns = ['Pilha','Cadeia','Acao'])
    print (df)
    
algoritmo()