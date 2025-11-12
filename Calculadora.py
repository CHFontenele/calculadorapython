# Importa bibliotecas necessárias
import math  # Para funções matemáticas (ex: raiz quadrada)
import os    # Para limpar a tela do terminal (compatível com Windows/Linux)

# Lista para armazenar o histórico das operações realizadas
historico = []

# Função para limpar a tela conforme o sistema operacional
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função responsável por exibir o menu principal da calculadora
def mostrar_menu():
    print("=" * 40)
    print(f"{'CALCULADORA PYTHON':^40}")  # Centraliza o título
    print("=" * 40)
    print("Operações disponíveis:")
    print("[1] Adição (+)")
    print("[2] Subtração (-)")
    print("[3] Multiplicação (*)")
    print("[4] Divisão (/)")
    print("[5] Porcentagem (%)")
    print("[6] Raiz Quadrada (√)")
    print("[7] Mostrar histórico")
    print("[0] Sair")
    print("=" * 40)

# Loop principal — mantém o programa rodando até o usuário decidir sair
while True:
    mostrar_menu()  # Exibe o menu de opções
    opcao = input("Escolha uma opção: ")  # Lê a escolha do usuário

    # Opção 0: encerra o programa
    if opcao == '0':
        print("\nEncerrando... 👋")
        break  # Sai do loop e finaliza o programa

    # Opção 7: exibe o histórico de operações realizadas
    elif opcao == '7':
        if not historico:  # Verifica se o histórico está vazio
            print("📜 Histórico vazio.")
        else:
            print("\n📖 HISTÓRICO DE OPERAÇÕES:")
            for item in historico:  # Percorre e mostra cada operação
                print(item)
        input("\nPressione ENTER para continuar...")
        limpar_tela()
        continue  # Volta ao início do loop

    # Opção 6: calcula raiz quadrada
    elif opcao == '6':
        try:
            n = float(input("Digite o número: "))  # Recebe o número
            resultado = math.sqrt(n)  # Calcula a raiz quadrada
            print(f"√{n} = {resultado:.2f}")
            # Armazena a operação no histórico
            historico.append(f"√{n} = {resultado:.2f}")
        except ValueError:
            print("❌ Valor inválido.")  # Caso o valor digitado não seja numérico
        input("\nPressione ENTER para continuar...")
        limpar_tela()
        continue  # Volta ao início do loop

    # Outras operações matemáticas (+, -, *, /, %)
    else:
        try:
            # Recebe dois números do usuário
            n1 = float(input("Digite o primeiro número: "))
            n2 = float(input("Digite o segundo número: "))

            # Verifica qual operação foi escolhida
            if opcao == '1' or opcao == '+':
                resultado = n1 + n2
                operacao = '+'
            elif opcao == '2' or opcao == '-':
                resultado = n1 - n2
                operacao = '-'
            elif opcao == '3' or opcao == '*':
                resultado = n1 * n2
                operacao = '*'
            elif opcao == '4' or opcao == '/':
                # Evita erro de divisão por zero
                if n2 == 0:
                    print("❌ Erro: divisão por zero!")
                    continue
                resultado = n1 / n2
                operacao = '/'
            elif opcao == '5' or opcao == '%':
                # Calcula porcentagem: n1% de n2
                resultado = (n1 * n2) / 100
                operacao = '%'
            else:
                print("⚠️ Opção inválida!")
                continue

            # Exibe o resultado formatado
            print(f"{n1} {operacao} {n2} = {resultado:.2f}")
            # Adiciona a operação ao histórico
            historico.append(f"{n1} {operacao} {n2} = {resultado:.2f}")

        except ValueError:
            # Caso o usuário digite algo que não seja número
            print("⚠️ Entrada inválida! Digite apenas números.")

    # Pausa até o usuário apertar ENTER e limpa a tela
    input("\nPressione ENTER para continuar...")
    limpar_tela()
