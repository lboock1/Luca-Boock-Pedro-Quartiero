from funcoes import *

cartela = {
    'regra_simples': {i: -1 for i in range(1, 7)},
    'regra_avancada': {
        'sem_combinacao': -1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}

imprime_cartela(cartela)

while True:

    # parar exatamente quando a cartela estiver completa
    if all(v != -1 for v in cartela['regra_simples'].values()) and \
       all(v != -1 for v in cartela['regra_avancada'].values()):
        break

    dados_rolados = rolar_dados(5)
    dados_guardados = []
    rerrolagens = 0

    while True:
        print(f"Dados rolados: {dados_rolados}")
        print(f"Dados guardados: {dados_guardados}")
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")

        opcao = input()

        if opcao == "1":
            print("Digite o índice do dado a ser guardado (0 a 4):")
            indice = int(input())
            if 0 <= indice < len(dados_rolados):
                guardar_dado(dados_rolados, dados_guardados, indice)
            else:
                print("Opção inválida. Tente novamente.")

        elif opcao == "2":
            print("Digite o índice do dado a ser removido (0 a 4):")
            indice = int(input())
            if 0 <= indice < len(dados_guardados):
                remover_dado(dados_rolados, dados_guardados, indice)
            else:
                print("Opção inválida. Tente novamente.")

        elif opcao == "3":
            if rerrolagens < 2:
                dados_rolados = rolar_dados(len(dados_rolados))
                rerrolagens += 1
            else:
                print("Você já usou todas as rerrolagens.")

        elif opcao == "4":
            imprime_cartela(cartela)

        elif opcao == "0":

            
            while True:
                print("Digite a combinação desejada:")
                categoria = input()

                if categoria in [str(i) for i in range(1,7)]:
                    if cartela['regra_simples'][int(categoria)] != -1:
                        print("Essa combinação já foi utilizada.")
                    else:
                        faz_jogada(dados_rolados + dados_guardados, categoria, cartela)
                        break

                elif categoria in cartela['regra_avancada']:
                    if cartela['regra_avancada'][categoria] != -1:
                        print("Essa combinação já foi utilizada.")
                    else:
                        faz_jogada(dados_rolados + dados_guardados, categoria, cartela)
                        break

                else:
                    print("Combinação inválida. Tente novamente.")

            break

        else:
            print("Opção inválida. Tente novamente.")


imprime_cartela(cartela)

pontuacao = 0

soma_simples = sum(cartela['regra_simples'].values())
pontuacao += soma_simples

if soma_simples >= 63:
    pontuacao += 35

pontuacao += sum(cartela['regra_avancada'].values())

print(f"Pontuação total: {pontuacao}")