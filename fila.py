# Exercício Python 16: Para ter acesso a fila de prioridade, você deve ser idoso, gestante ou cadeirante. 
# Escreva um programa que pergunta a situação do usuário 
# (se é idoso, se é gestante, se é cadeirante ou nenhum destes) 
# e diga se ele pode ter acesso a fila prioridade ou não.

prioridade = int(input(f"qual a sua situação?\n1:idoso,\n2:gestante,\n3:cadeirante,\n4:não me encaixo em nenhuma das opções\ninsira:"))

if prioridade == 1 or prioridade == 2 or prioridade == 3:
    print("va para a fila portaria")
else:
    print("va para a fila comun")