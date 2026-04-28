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
    }}
imprime_cartela(cartela)
for rodada in range(12):
    dados = rolar_dados(5)
    guardados = []
    rerrolagens = 0
    jogada_feita = False
    while jogada_feita == False:
        print(f"Dados rolados: {dados}")
        print(f"Dados guardados: {guardados}")
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
        opcao = input()
        if opcao == "1":
            print("Digite o índice do dado a ser guardado (0 a 4):")
            i = int(input())
            if 0 <= i < len(dados):
                dados, guardados = guardar_dado(dados, guardados, i)
        elif opcao == "2":
            print("Digite o índice do dado a ser removido (0 a 4):")
            i = int(input())
            if 0 <= i < len(guardados):
                dados, guardados = remover_dado(dados, guardados, i)
        elif opcao == "3":
            if rerrolagens < 2:
                dados = rolar_dados(5 - len(guardados))
                rerrolagens += 1
            else:
                print("Você já usou todas as rerrolagens.")
        elif opcao == "4":
            imprime_cartela(cartela)
        elif opcao == "0":
            while True:
                print("Digite a combinação desejada:")
                categoria = input()
                if categoria in ["1","2","3","4","5","6"]:
                    numero = int(categoria)
                    if cartela['regra_simples'][numero] != -1:
                        print("Essa combinação já foi utilizada.")
                    else:
                        faz_jogada(dados + guardados, categoria, cartela)
                        jogada_feita = True
                        break
                elif categoria in cartela['regra_avancada']:
                    if cartela['regra_avancada'][categoria] != -1:
                        print("Essa combinação já foi utilizada.")
                    else:
                        faz_jogada(dados + guardados, categoria, cartela)
                        jogada_feita = True
                        break
                else:
                    print("Combinação inválida. Tente novamente.")
        else:
            print("Opção inválida. Tente novamente.")
imprime_cartela(cartela)
total = 0
soma_simples = 0
for v in cartela['regra_simples'].values():
    if v != -1:
        soma_simples += v
        total += v
if soma_simples >= 63:
    total += 35
for v in cartela['regra_avancada'].values():
    if v != -1:
        total += v
print(f"Pontuação total: {total}")