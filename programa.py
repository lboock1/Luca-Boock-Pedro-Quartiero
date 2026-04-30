from funcoes import (
rolar_dados,
guardar_dado,
remover_dado,
faz_jogada,
imprime_cartela,
calcula_pontos_regra_simples
)

# Inicializa a cartela com -1 (linhas não preenchidas)

cartela = {
‘regra_simples’: {1: -1, 2: -1, 3: -1, 4: -1, 5: -1, 6: -1},
‘regra_avancada’: {
‘sem_combinacao’: -1,
‘quadra’: -1,
‘full_house’: -1,
‘sequencia_baixa’: -1,
‘sequencia_alta’: -1,
‘cinco_iguais’: -1,
}
}

combinacoes_validas = [“1”, “2”, “3”, “4”, “5”, “6”,
“sem_combinacao”, “quadra”, “full_house”,
“sequencia_baixa”, “sequencia_alta”, “cinco_iguais”]

# 12 rodadas

for rodada in range(12):
dados_rolados = rolar_dados(5)
dados_guardados = []
rerrolagens = 0
jogada_feita = False


while not jogada_feita:
    print(f"Dados rolados: {dados_rolados}")
    print(f"Dados guardados: {dados_guardados}")
    print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
    opcao = input()

    if opcao == "1":
        print("Digite o índice do dado a ser guardado (0 a 4):")
        indice = int(input())
        dados_rolados, dados_guardados = guardar_dado(dados_rolados, dados_guardados, indice)

    elif opcao == "2":
        print("Digite o índice do dado a ser removido (0 a 4):")
        indice = int(input())
        dados_rolados, dados_guardados = remover_dado(dados_rolados, dados_guardados, indice)

    elif opcao == "3":
        if rerrolagens >= 2:
            print("Você já usou todas as rerrolagens.")
        else:
            quantidade = len(dados_rolados)
            dados_rolados = rolar_dados(quantidade)
            rerrolagens += 1

    elif opcao == "4":
        imprime_cartela(cartela)

    elif opcao == "0":
        while True:
            print("Digite a combinação desejada:")
            categoria = input()
            if categoria not in combinacoes_validas:
                print("Combinação inválida. Tente novamente.")
                continue
            # Verifica se a linha já foi preenchida
            if categoria in ["1", "2", "3", "4", "5", "6"]:
                if cartela['regra_simples'][int(categoria)] != -1:
                    print("Essa combinação já foi utilizada.")
                    continue
            else:
                if cartela['regra_avancada'][categoria] != -1:
                    print("Essa combinação já foi utilizada.")
                    continue
            # Categoria válida e linha vazia: faz a jogada
            dados_totais = dados_rolados + dados_guardados
            cartela = faz_jogada(dados_totais, categoria, cartela)
            jogada_feita = True
            break

    else:
        print("Opção inválida. Tente novamente.")


# Fim do jogo: imprime cartela e calcula pontuação total

imprime_cartela(cartela)

pontuacao = 0
soma_simples = 0
for i in range(1, 7):
if cartela[‘regra_simples’][i] != -1:
soma_simples += cartela[‘regra_simples’][i]

pontuacao += soma_simples

for chave in cartela[‘regra_avancada’]:
if cartela[‘regra_avancada’][chave] != -1:
pontuacao += cartela[‘regra_avancada’][chave]

# Bônus de 35 pontos se soma das regras simples >= 63

if soma_simples >= 63:
pontuacao += 35

print(f”Pontuação total: {pontuacao}”)