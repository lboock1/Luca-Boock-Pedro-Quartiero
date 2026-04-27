import random 
def rolar_dados(quantidade):
    resultado = []
    for _ in range(quantidade):
        resultado.append(random.randint(1, 6))
    return resultado    
    