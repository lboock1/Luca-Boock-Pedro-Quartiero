from funcoes import (
    rolar_dados, guardar_dado, remover_dado,
    faz_jogada, imprime_cartela
)
 
def cria_cartela():
    return {
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
 
def combinacoes_validas(cartela):
    validas = [str(i) for i in range(1, 7)]
    validas += list(cartela['regra_avancada'].keys())
    return validas
 
def ja_utilizada(categoria, cartela):
    if categoria in [str(i) for i in range(1, 7)]:
        return cartela['regra_simples'][int(categoria)] != -1
    return cartela['regra_avancada'].get(categoria, -1) != -1
 
def exibe_estado(dados_r, dados_g):
    print(f"Dados rolados: {dados_r}")
    print(f"Dados guardados: {dados_g}")
    print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
 
def acao_marcar(dados_r, dados_g, cartela):
    """Trata a ação de marcar pontuação. Retorna True se marcou, False se deve continuar."""
    todos = dados_r + dados_g
    print("Digite a combinação desejada:")
    categoria = input(">")
    validas = combinacoes_validas(cartela)
 
    for _ in range(100):  
        if categoria not in validas:
            print("Combinação inválida. Tente novamente.")
            categoria = input(">")
        elif ja_utilizada(categoria, cartela):
            print("Essa combinação já foi utilizada.")
            categoria = input(">")
        else:
            faz_jogada(todos, categoria, cartela)
            return True
 
    return True  
 
def rodada(cartela):
    """Executa uma rodada completa. Retorna a cartela atualizada."""
    dados_r = rolar_dados(5)
    dados_g = []
    rerrolagens = 0
 
    exibe_estado(dados_r, dados_g)
 
    for _ in range(100): 
        opcao = input(">")
 
        if opcao == "1":
            print("Digite o índice do dado a ser guardado (0 a 4):")
            indice = int(input(">"))
            dados_r, dados_g = guardar_dado(dados_r, dados_g, indice)
 
        elif opcao == "2":
            print("Digite o índice do dado a ser removido (0 a 4):")
            indice = int(input(">"))
            dados_r, dados_g = remover_dado(dados_r, dados_g, indice)
 
        elif opcao == "3":
            if rerrolagens >= 2:
                print("Você já usou todas as rerrolagens.")
            else:
                dados_r = rolar_dados(len(dados_r))
                rerrolagens += 1
 
        elif opcao == "4":
            imprime_cartela(cartela)
 
        elif opcao == "0":
            marcou = acao_marcar(dados_r, dados_g, cartela)
            if marcou:
                return cartela
 
        else:
            print("Opção inválida. Tente novamente.")
            continue
 
        if opcao != "0":
            exibe_estado(dados_r, dados_g)
 
    return cartela
 
def calcula_pontuacao_final(cartela):
    total = 0
    soma_simples = 0
 
    for i in range(1, 7):
        v = cartela['regra_simples'][i]
        if v != -1:
            total += v
            soma_simples += v
 
    for v in cartela['regra_avancada'].values():
        if v != -1:
            total += v
 
    if soma_simples >= 63:
        total += 35
 
    return total
 
def main():
    cartela = cria_cartela()
    imprime_cartela(cartela)
 
    num_rodadas = 12
 
    for _ in range(num_rodadas):
        cartela = rodada(cartela)
 
    imprime_cartela(cartela)
    pontuacao = calcula_pontuacao_final(cartela)
    print(f"Pontuação total: {pontuacao}")
 
main()