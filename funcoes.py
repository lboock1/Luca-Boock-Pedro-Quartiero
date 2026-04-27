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

 
    