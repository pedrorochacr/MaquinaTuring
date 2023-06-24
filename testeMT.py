import json
import sys

def run_turing_machine(mt, palavra):
    listPalavra = list(palavra)
    listPalavra.insert(0, mt[4]) #insere >
    listPalavra.append(mt[5]) # insere U
    listTrilhas = [listPalavra]  # Inicializa a fita na primeira trilha com a palavra fornecida
    tamanhotrilha = len(listPalavra)
    trilhaGenerica = [mt[5]] * tamanhotrilha
    for _ in range(mt[0]-1):
        listTrilhas.append(trilhaGenerica)
    cabecote = 1  # Posição inicial da cabeça de leitura/escrita
    print(listTrilhas)
    estados = mt[1]
    maquinaEstados = mt[7]  # Estado inicial

    transicoes = mt[6]
    while True:
    # Verifica se o estado atual é um estado final
        if maquinaEstados in mt[8] #e transicao é invalida:
            return True  # A palavra pertence à linguagem
        
        #percorra a lista transicao
        for transicao in transicoes: 
            if transicao[0] == maquinaEstados:
                
        

    

def main():
    argumento = sys.argv;
    print (argumento);
    try:
        # Abre o arquivo JSON e carrega as informações da máquina de Turing
        with open(argumento[1]) as file:
            mt = json.load(file)["mt"]

        # Executa a máquina de Turing com a palavra de entrada fornecida
        result = run_turing_machine(mt, argumento[2])

        if result:
            print("Sim")
        else:
            print("Não")

    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except json.JSONDecodeError:
        print("Erro ao decodificar o arquivo JSON.")

if __name__ == '__main__':
    main()
