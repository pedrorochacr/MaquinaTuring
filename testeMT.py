import json
import sys
# Posição inicial da cabeça de leitura/escrita
cabecote = 1
listTrilhas = []
maquinaEstados = 0
mt = {}

def run_maquina_de_turing(palavra):
    global listTrilhas
    global cabecote
    global maquinaEstados
    global mt
    
    for simbolo in palavra:
        if simbolo not in mt[2]:
            return False
         
    listPalavra = list(palavra)
    listPalavra.insert(0, mt[4]) #insere >
    listPalavra.append(mt[5]) # insere U
    listTrilhas = [listPalavra]  # Inicializa a fita na primeira trilha com a palavra fornecida
    tamanhotrilha = len(listPalavra)
    trilhaGenerica = [mt[5]] * tamanhotrilha

    for _ in range(mt[0]-1):
        listTrilhas.append(trilhaGenerica)
    maquinaEstados = mt[7]  # Estado inicial

    transicoes = mt[6]

    while True:
        tem_transicao = False

        #percorra a lista transicao e a maquina de multiplas trilhas e compara se a trasicao é válida
        for transicao in transicoes: 
            if transicao[0] == maquinaEstados:
                variavel = 0
                for i in range(len(listTrilhas)):
                    if listTrilhas[i][cabecote] == transicao[i+1]:
                        variavel += 1
                    else: 
                        break
            if variavel == len(listTrilhas):
                realizaTransicao(transicao)
                tem_transicao = True
                variavel = 0
                break
        if tem_transicao == False: # transição indefinida
            break
    return maquinaEstados in mt[8]
   
def adicionar_branco(): # Fita ilimitada à direita
    global listTrilhas
    global mt

    for i in range(len(listTrilhas)):
        listTrilhas[i].append(mt[5])

def realizaTransicao(transicao):        
    global listTrilhas
    global cabecote
    global maquinaEstados
    for i in range(len(listTrilhas)):
        listTrilhas[i][cabecote] = transicao[len(listTrilhas)+2+i]

    if transicao[-1] == ">": 
        cabecote += 1

        if cabecote == len(listTrilhas):
            adicionar_branco()
    else:
        cabecote -= 1
    
    maquinaEstados = transicao[len(listTrilhas)+1]
    
def main():
    argumento = sys.argv
    if len(argumento) != 3:
        print("python3 testeMT.py [MT] [Word]")
        exit()
    try:
        global mt
        # Abre o arquivo JSON e carrega as informações da máquina de Turing
        with open(argumento[1]) as file:
            mt = json.load(file)["mt"]

        # Executa a máquina de Turing com a palavra de entrada fornecida
        result = run_maquina_de_turing(argumento[2])

        if result:
            print("Sim")
        else:
            print("Não")

    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except json.JSONDecodeError:
        print("Erro ao decodificar o arquivo JSON.")

main()