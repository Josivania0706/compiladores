from numpy import append
import pandas as pd
gram = {
    "1": ["E", "+", "T"],
    "2": ["T"],
    "3": ["T", "*", "F"],
    "4": ["F"],
    "5": ["(", "E", ")"],
    "6": ["id"],
}
gram3 = {
    "1": ["TYPE", "ID"],
    "2": ["T", "E'"],
    "3": ["+", "E'"],
    "4": ["_"],
    "5": ["F", "T'"],
    "6": ["*", "T'"],
    "7": ["_"],
    "8": ["(", "E", ")"],
    "9": ["id"],
    "10": ["int"],
    "11":["float"],
    "12":["a"],
    "13":["b"],
    "14":["c"],
}

gram1 = {
    "1": "D",
    "2": "E",
    "3": "E'",
    "4": "E'",
    "5": "T",
    "6": "T'",
    "7": "T'",
    "8": "F",
    "9": "F",
    "10": "TYPE",
    "11": "TYPE",
    "12": "id",
    "13": "id",
    "14": "id",
}

tabela  = {
    "0 id": ["s", "5"],
    "0 (":  ["s", "4"],
    "0 E":   "1",
    "0 T":   "2",
    "0 F":   "3",
    "1 +":  ["s","6"],
    "1 $":   "ok",
    "2 +":  ["r","2"],
    "2 *":  ["s", "7"],
    "2 )":  ["r", "2"],
    "2 $":  ["r", "2"],
    "3 +":  ["r", "4"],
    "3 *":  ["r", "4"],
    "3 )":  ["r", "4"],
    "3 $":  ["r", "4"],
    "4 id": ["s", "5"],
    "4 (":  ["s", "4"],
    "4 E":   "8",
    "4 T":   "2",
    "4 F":   "3",
    "5 +":  ["r","6"],
    "5 *":  ["r","6"],
    "5 )":  ["r","6"],
    "5 $":  ["r","6"],
    "6 id": ["s", "5"],
    "6 (":  ["s","4"],
    "6 T":   "9",
    "6 F":   "3",
    "7 id": ["s","5"],
    "7 (":  ["s", "4"],
    "7 F":  "10",
    "8 +":  ["s", "6"],
    "8 )":  ["s", "11"],
    "9 +":  ["r", "1"],
    "9 *":  ["s", "7"],
    "9 )":  ["r", "1"],
    "9 $":  ["r", "1"],
    "10 +": ["r", "3"],
    "10 *": ["r", "3"],
    "10 )": ["r", "3"],
    "10 $": ["r","3"],
    "11 +": ["r", "5"],
    "11 *": ["r", "5"],
    "11 )": ["r", "5"],
    "11 $": ["r", "5"],
      
}


a = 1
b = 2
c = 3
cadeia = [a,"*", b,"*",c ,"$"]

#cadeia = ["(","id","*", "id",")","+","(","id","*", "id",")", "$"]
ip = 0
parada = ""
pilha = ['0']
simbolos = []
acao = []
tabelaBottonUp = []
def analiseLR():
    global ip, tabelaBottonUp
    a = cadeia[ip]
    
    tabelaBottonUp.append([str(pilha).strip('[]'), str(simbolos).strip('[]'), cadeia[ip:]]) 
    while(True):
        p = pilha[-1]
        
        if "s" in tabela.get(f'{p} {a}'):
            c = tabela.get(f'{p} {a}')
            acao.append(f'{c[0]}{c[1]}')
            pilha.append(c[-1])
            simbolos.append(a)
            ip = ip + 1
            a = cadeia[ip]
           
            tabelaBottonUp.append([str(pilha).strip('[]'), str(simbolos).strip('[]'), cadeia[ip:]]) 
            
        elif "r" in tabela.get(f'{p} {a}'):
            linhaReduz = tabela.get(f'{p} {a}')
            acao.append(f'{linhaReduz[0]}{linhaReduz[1]}')
            aux = linhaReduz[1]
            i = 0
            while i < len(gram.get(aux)) :
                pilha.pop(-1)
                simbolos.pop(-1)
                i= i +1
            simbolos.append(gram1.get(linhaReduz[1]))
            t = pilha[-1]

            pilha.append(tabela.get(f'{t} {simbolos[-1]}'))

            tabelaBottonUp.append([str(pilha).strip('[]'), str(simbolos).strip('[]'), cadeia[ip:]]) 
        elif tabela.get(f'{p} {a}') == "ok":
            print("ok")
            acao.append("ok")
            break
        else:
            exit(-1)
   
    df = pd.DataFrame(tabelaBottonUp, columns = ['Pilha','Simbolos','Cadeia'])
    print (df)
    print("acao:", acao)
    print()

analiseLR()   

