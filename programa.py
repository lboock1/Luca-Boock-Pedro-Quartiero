import random
from funcoes import *

def rolar_dados(n):
    return [random.randint(1, 6) for _ in range(n)]

# inicializa cartela
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

# jogo tem 12 rodadas
for rodada in range(12):
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
            i = int(input())
            if 0 <= i < len(dados_rolados):
                dados_guardados.append(dados_rolados.pop(i))

        elif opcao == "2":
            print("Digite o índice do dado a ser removido (0 a 4):")
            i = int(input())
            if 0 <= i < len(dados_guardados):
                dados_rolados.append(dados_guardados.pop(i))

        elif opcao == "3":
            if rerrolagens < 2:
                dados_rolados = rolar_dados(len(dados_rolados))
                rerrolagens += 1
            else:
                print("Você já usou todas as rerrolagens.")

        elif opcao == "4":
            imprime_cartela(cartela)

        elif opcao == "0":
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

        else:
            print("Opção inválida. Tente novamente.")

# cálculo da pontuação
total = 0

# soma regra simples
soma_simples = 0
for v in cartela['regra_simples'].values():
    if v != -1:
        total += v
        soma_simples += v

# bônus
if soma_simples >= 63:
    total += 35

# soma regra avançada
for v in cartela['regra_avancada'].values():
    if v != -1:
        total += v

# resultado final
imprime_cartela(cartela)
print(f"Pontuação total: {total}")