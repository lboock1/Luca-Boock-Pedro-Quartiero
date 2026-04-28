import random 
def rolar_dados(quantidade):
    resultado = []
    for _ in range(quantidade):
        resultado.append(random.randint(1, 6))
    return resultado   

def guardar_dado(dados_r, dados_g, indice):
    dado= dados_r.pop(indice)
    dados_g.append(dado)
    return [dados_r, dados_g]

def remover_dado(dados_r, dados_g, indice):
    dado= dados_g.pop(indice)
    dados_r.append(dado)
    return [dados_r, dados_g]

def calcula_pontos_regra_simples(faces_r):
    pontos={}
    for face in range(1,7):
        soma=0
        for dado in faces_r:
            if dado==face:
                soma +=dado
        pontos[face]=soma
    return pontos

def calcula_pontos_soma(faces_r):
    total=0
    for dado in faces_r:
        total +=dado
    return total
 
def calcula_pontos_sequencia_baixa(faces_r):
    if 1 in faces_r and 2 in faces_r and 3 in faces_r and 4 in faces_r:
        return 15
    if 2 in faces_r and 3 in faces_r and 4 in faces_r and 5 in faces_r:
        return 15
    if 3 in faces_r and 4 in faces_r and 5 in faces_r and 6 in faces_r:
        return 15
    return 0

def calcula_pontos_sequencia_alta(faces_r):
    if 1 in faces_r and 2 in faces_r and 3 in faces_r and 4 in faces_r and 5 in faces_r:
        return 30
    if 2 in faces_r and 3 in faces_r and 4 in faces_r and 5 in faces_r and 6 in faces_r:
        return 30
    return 0

def calcula_pontos_full_house(faces_r):
    c={}
    for dado in faces_r:
        if dado in c:
            c[dado] += 1
        else:
            c[dado] = 1
    valores = list(c.values())
    if 3 in valores and 2 in valores:
        total = 0
        for f in faces_r:
            total += f
        return total
    return 0

def calcula_pontos_quadra(faces_r):
    c={} 
    for dado in faces_r:
        if dado in c:
            c[dado] += 1
        else:
            c[dado] = 1
    for valor in c:
        if c[valor] >=4:
            total= 0
            for f in faces_r:
                total+=f
            return total
    return 0

def calcula_pontos_quina(faces_r):  
    c={} 
    for dado in faces_r:
        if dado in c:
            c[dado] += 1
        else:
            c[dado] = 1
    for valor in c:
        if c[valor] >=5:
            return 50
    return 0

def calcula_pontos_regra_avancada(faces_r):
    return {
        'cinco_iguais': calcula_pontos_quina(faces_r),
        'full_house': calcula_pontos_full_house(faces_r),
        'quadra': calcula_pontos_quadra(faces_r),
        'sem_combinacao': calcula_pontos_soma(faces_r),
        'sequencia_alta': calcula_pontos_sequencia_alta(faces_r),
        'sequencia_baixa': calcula_pontos_sequencia_baixa(faces_r)
    }

def faz_jogada(dados,categoria, cartela):
    if categoria in ["1", "2", "3", "4", "5", "6"]:
        numero = int(categoria)
        pontos = calcula_pontos_regra_simples(dados, numero)
        cartela["regra_simples"][numero]= pontos
    else:
        pontos= calcula_pontos_regra_avancada(dados, categoria)
        cartela["regra_avancada"][categoria]= pontos
    return cartela

        






 
    