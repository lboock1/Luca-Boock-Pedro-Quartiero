from funcoes import *

cartela = {
    'regra_simples': {i: -1 for i in range(1,7)},
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

for rodada in range(12):
    dados_rolados = rolar_dados(5)
    dados_guardados = []
    rerrolagens = 2

    while True:
        print(f"Dados rolados: {dados_rolados}")
        print(f"Dados guardados: {dados_guardados}")
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")

        opcao = input()

        if opcao == "1":
            print("Digite o índice do dado a ser guardado (0 a 4):")
            i = int(input())
            dados_rolados, dados_guardados = guardar_dado(dados_rolados, dados_guardados, i)

        elif opcao == "2":
            print("Digite o índice do dado a ser removido (0 a 4):")
            i = int(input())
            dados_rolados, dados_guardados = remover_dado(dados_rolados, dados_guardados, i)

        elif opcao == "3":
            if rerrolagens > 0:
                dados_rolados = rolar_dados(5 - len(dados_guardados))
                rerrolagens -= 1
            else:
                print("Você já usou todas as rerrolagens.")

        elif opcao == "4":
            imprime_cartela(cartela)

        elif opcao == "0":
            while True:
                print("Digite a combinação desejada:")
                categoria = input()

                if categoria.isdigit() and int(categoria) in cartela['regra_simples']:
                    if cartela['regra_simples'][int(categoria)] == -1:
                        faz_jogada(dados_rolados + dados_guardados, categoria, cartela)
                        break
                    else:
                        print("Essa combinação já foi utilizada.")

                elif categoria in cartela['regra_avancada']:
                    if cartela['regra_avancada'][categoria] == -1:
                        faz_jogada(dados_rolados + dados_guardados, categoria, cartela)
                        break
                    else:
                        print("Essa combinação já foi utilizada.")
                else:
                    print("Combinação inválida. Tente novamente.")

            break

        else:
            print("Opção inválida. Tente novamente.")


imprime_cartela(cartela)


soma_simples = sum(v for v in cartela['regra_simples'].values() if v != -1)

bonus = 35 if soma_simples >= 63 else 0


total = soma_simples + bonus + sum(v for v in cartela['regra_avancada'].values() if v != -1)

print(f"Pontuação total: {total}")