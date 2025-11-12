import math
import os

historico = []

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    print("=" * 40)
    print(f"{'CALCULADORA PYTHON':^40}")
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

while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == '0':
        print("\nEncerrando... 👋")
        break

    elif opcao == '7':
        if not historico:
            print("📜 Histórico vazio.")
        else:
            print("\n📖 HISTÓRICO DE OPERAÇÕES:")
            for item in historico:
                print(item)
        input("\nPressione ENTER para continuar...")
        limpar_tela()
        continue

    elif opcao == '6':
        try:
            n = float(input("Digite o número: "))
            resultado = math.sqrt(n)
            print(f"√{n} = {resultado:.2f}")
            historico.append(f"√{n} = {resultado:.2f}")
        except ValueError:
            print("❌ Valor inválido.")
        input("\nPressione ENTER para continuar...")
        limpar_tela()
        continue

    else:
        try:
            n1 = float(input("Digite o primeiro número: "))
            n2 = float(input("Digite o segundo número: "))

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
                if n2 == 0:
                    print("❌ Erro: divisão por zero!")
                    continue
                resultado = n1 / n2
                operacao = '/'
            elif opcao == '5' or opcao == '%':
                resultado = (n1 * n2) / 100
                operacao = '%'
            else:
                print("⚠️ Opção inválida!")
                continue

            print(f"{n1} {operacao} {n2} = {resultado:.2f}")
            historico.append(f"{n1} {operacao} {n2} = {resultado:.2f}")

        except ValueError:
            print("⚠️ Entrada inválida! Digite apenas números.")

    input("\nPressione ENTER para continuar...")
    limpar_tela()

