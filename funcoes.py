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




 
    