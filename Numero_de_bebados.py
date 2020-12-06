# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import random

B = int(50)  #número de bebados 
P = int(50)  #número de passos de cada bebado 
pe = 0  #numero de passos para a esquerda
pd = 0  #numero de passos para a direita
t = 1  #tamanho do passo do bebado 
dados = []
parte = 100000
parte_atual = parte
# ----- INICIO
def atual_datahora(modo):
    from datetime import datetime
    resultado = datetime.today()
    if modo == 1:
        resultado = resultado.strftime('%d-%m-%Y_%H-%M-%S-%f')
    else:
        resultado = resultado.strftime('%d/%m/%Y %H:%M:%S:%f')
    return resultado


# ----- FIM DEF
print(atual_datahora(2));
# Para cada bebado calculo as iterações para N passos 
for i in range(B):
    for j in range(P):
        rand = random.random()
        if rand > 0.5:
            pe += 1 
        else:
            pd += 1
    calc = (pd - pe) * t
    dados.append(calc) 
    pe = 0 
    pd = 0
    if i == parte_atual:
      parte_atual += parte
      print(atual_datahora(2) + " B: " + str(i))  
plt.hist(dados, 1000)
plt.title("B: " + str(B) + " P: " + str(P))
plt.show()
# ----- FIM CODIGO
