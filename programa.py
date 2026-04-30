from funcoes import *
def nova_cartela():
    return {
        'regra_simples': {1: -1, 2: -1, 3: -1, 4: -1, 5: -1, 6: -1},
        'regra_avancada': {
            'sem_combinacao': -1,
            'quadra': -1,
            'full_house': -1,
            'sequencia_baixa': -1,
            'sequencia_alta': -1,
            'cinco_iguais': -1
        }}
def categoria_valida(categoria):
    validas = ['1','2','3','4','5','6',
               'sem_combinacao','quadra','full_house',
               'sequencia_baixa','sequencia_alta','cinco_iguais']
    return categoria in validas
def categoria_preenchida(categoria, cartela):
    if categoria in ['1','2','3','4','5','6']:
        return cartela['regra_simples'][int(categoria)] != -1
    else:
        return cartela['regra_avancada'][categoria] != -1
cartela = nova_cartela()
imprime_cartela(cartela)
for rodada in range(12):
    dados_r = rolar_dados(5)
    dados_g = []
    rerrolagens = 0
    print(f"Dados rolados: {dados_r}")
    print(f"Dados guardados: {dados_g}")
    print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")

    jogada_feita = False
    while not jogada_feita:
        opcao = input()
        if opcao == '1':
            print("Digite o índice do dado a ser guardado (0 a 4):")
            idx = int(input())
            resultado = guardar_dado(dados_r, dados_g, idx)
            dados_r = resultado[0]
            dados_g = resultado[1]
            print(f"Dados rolados: {dados_r}")
            print(f"Dados guardados: {dados_g}")
            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
 
        elif opcao == '2':
            print("Digite o índice do dado a ser removido (0 a 4):")
            idx = int(input())
            resultado = remover_dado(dados_r, dados_g, idx)
            dados_r = resultado[0]
            dados_g = resultado[1]
            print(f"Dados rolados: {dados_r}")
            print(f"Dados guardados: {dados_g}")
            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")

        elif opcao == '3':
            if rerrolagens >= 2:
                print("Você já usou todas as rerrolagens.")
                print(f"Dados rolados: {dados_r}")
                print(f"Dados guardados: {dados_g}")
                print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
            else:
                rerrolagens += 1
                dados_r = rolar_dados(len(dados_r))
                print(f"Dados rolados: {dados_r}")
                print(f"Dados guardados: {dados_g}")
                print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
 
        elif opcao == '4':
            imprime_cartela(cartela)
            print(f"Dados rolados: {dados_r}")
            print(f"Dados guardados: {dados_g}")
            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")

        elif opcao == '0':
            print("Digite a combinação desejada:")
            while True:
                categoria = input()
                if not categoria_valida(categoria):
                    print("Combinação inválida. Tente novamente.")
                    print("Digite a combinação desejada:")
                elif categoria_preenchida(categoria, cartela):
                    print("Essa combinação já foi utilizada.")
                    print("Digite a combinação desejada:")
                else:
                    todos = dados_r + dados_g
                    cartela = faz_jogada(todos, categoria, cartela)
                    jogada_feita = True
                    break
        else:
            print("Opção inválida. Tente novamente.")
            print(f"Dados rolados: {dados_r}")
            print(f"Dados guardados: {dados_g}")
            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")

pontuacao = 0
soma_simples = 0
for i in range(1, 7):
    v = cartela['regra_simples'][i]
    if v != -1:
        pontuacao += v
        soma_simples += v
for k in cartela['regra_avancada']:
    v = cartela['regra_avancada'][k]
    if v != -1:
        pontuacao += v
if soma_simples >= 63:
    pontuacao += 35
imprime_cartela(cartela)
print(f"Pontuação total: {pontuacao}")