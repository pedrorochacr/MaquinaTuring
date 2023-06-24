import json

def run_turing_machine(mt, word):
    tape = {0: {0: word}}  # Inicializa a fita na primeira trilha com a palavra fornecida
    head = 0  # Posição inicial da cabeça de leitura/escrita

    current_state = mt['i']  # Estado inicial

    while True:
        # Verifica se o estado atual é um estado final
        if current_state in mt['f']:
            return True  # A palavra pertence à linguagem

        # Obtém o símbolo atual sob a cabeça de leitura/escrita
        current_symbol = tape[head].get(0, '_')

        # Obtém a próxima transição com base no estado atual e símbolo atual
        transitions = mt[6]
        next_transition = None
        for transition in transitions:
            if transition[0] == current_state and transition[1] == current_symbol:
                next_transition = transition
                break

        if next_transition is None:
            return False  # A palavra não pertence à linguagem

        # Atualiza o estado atual
        current_state = next_transition[3]

        # Atualiza o símbolo sob a cabeça de leitura/escrita
        tape[head][0] = next_transition[4]

        # Move a cabeça de leitura/escrita para a próxima posição
        if next_transition[5] == '>':
            head += 1
        elif next_transition[5] == '<':
            head -= 1

        # Cria uma nova trilha se necessário
        if head not in tape:
            tape[head] = {}

def main():
    # Obtém o caminho do arquivo JSON
    json_file = input("Digite o caminho do arquivo JSON: ")

    # Obtém a palavra de entrada
    word = input("Digite a palavra de entrada: ")

    try:
        # Abre o arquivo JSON e carrega as informações da máquina de Turing
        with open(json_file) as file:
            mt = json.load(file)

        # Executa a máquina de Turing com a palavra de entrada fornecida
        result = run_turing_machine(mt, word)

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
