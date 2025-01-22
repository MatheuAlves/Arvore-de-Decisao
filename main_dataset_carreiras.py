import pandas as pd

df = pd.read_csv('dataset_carreiras.csv')

print('Vamos começar o Quiz, responda com 1 para sim ou 0 para não')

try:
    equipe = int(input('Pergunta 1: Você gosta de trabalhar em equipe? (1 para Sim, 0 para Não): '))
    if equipe not in [0, 1]:
        raise ValueError("A resposta deve ser 1 ou 0.")
except ValueError:
    print("Entrada inválida. Use 1 para Sim ou 0 para Não.")
    equipe = int(input('Pergunta 1: Você gosta de trabalhar em equipe? (1 para Sim, 0 para Não): '))

try:
    ar_livre = int(input('Pergunta 2: Você gosta de trabalhar ao ar livre? (1 para Sim, 0 para Não): '))
    if ar_livre not in [0, 1]:
        raise ValueError("A resposta deve ser 1 ou 0.")
except ValueError:
    print("Entrada inválida. Use 1 para Sim ou 0 para Não.")
    ar_livre = int(input('Pergunta 2: Você gosta de trabalhar ao ar livre? (1 para Sim, 0 para Não): '))

try:
    numeros = int(input('Pergunta 3: Você gosta de trabalhar com números? (1 para Sim, 0 para Não): '))
    if numeros not in [0, 1]:
        raise ValueError("A resposta deve ser 1 ou 0.")
except ValueError:
    print("Entrada inválida. Use 1 para Sim ou 0 para Não.")
    numeros = int(input('Pergunta 3: Você gosta de trabalhar com números? (1 para Sim, 0 para Não): '))

try:
    artes = int(input('Pergunta 4: Você gosta de trabalhar com artes? (1 para Sim, 0 para Não): '))
    if artes not in [0, 1]:
        raise ValueError("A resposta deve ser 1 ou 0.")
except ValueError:
    print("Entrada inválida. Use 1 para Sim ou 0 para Não.")
    artes = int(input('Pergunta 4: Você gosta de trabalhar com artes? (1 para Sim, 0 para Não): '))

try:
    tecnologia = int(input('Pergunta 5: Você gosta de trabalhar com tecnologia? (1 para Sim, 0 para Não): '))
    if tecnologia not in [0, 1]:
        raise ValueError("A resposta deve ser 1 ou 0.")
except ValueError:
    print("Entrada inválida. Use 1 para Sim ou 0 para Não.")
    tecnologia = int(input('Pergunta 5: Você gosta de trabalhar com tecnologia? (1 para Sim, 0 para Não): '))

try:
    complexo = int(input('Pergunta 6: Você gosta de trabalhar com problemas complexos? (1 para Sim, 0 para Não): '))
    if complexo not in [0, 1]:
        raise ValueError("A resposta deve ser 1 ou 0.")
except ValueError:
    print("Entrada inválida. Use 1 para Sim ou 0 para Não.")
    complexo = int(input('Pergunta 6: Você gosta de trabalhar com problemas complexos? (1 para Sim, 0 para Não): '))

try:
    comunicacao = int(input('Pergunta 7: Você gosta de trabalhar com comunicação? (1 para Sim, 0 para Não): '))
    if comunicacao not in [0, 1]:
        raise ValueError("A resposta deve ser 1 ou 0.")
except ValueError:
    print("Entrada inválida. Use 1 para Sim ou 0 para Não.")
    comunicacao = int(input('Pergunta 7: Você gosta de trabalhar com comunicação? (1 para Sim, 0 para Não): '))

try:
    cuidar_pessoa = int(input('Pergunta 8: Você gosta de trabalhar cuidando de pessoas? (1 para Sim, 0 para Não): '))
    if cuidar_pessoa not in [0, 1]:
        raise ValueError("A resposta deve ser 1 ou 0.")
except ValueError:
    print("Entrada inválida. Use 1 para Sim ou 0 para Não.")
    cuidar_pessoa = int(input('Pergunta 8: Você gosta de trabalhar cuidando de pessoas? (1 para Sim, 0 para Não): '))

try:
    fisico = int(input('Pergunta 9: Você gosta de trabalho de esforço físico? (1 para Sim, 0 para Não): '))
    if fisico not in [0, 1]:
        raise ValueError("A resposta deve ser 1 ou 0.")
except ValueError:
    print("Entrada inválida. Use 1 para Sim ou 0 para Não.")
    fisico = int(input('Pergunta 9: Você gosta de trabalho de esforço físico? (1 para Sim, 0 para Não): '))

try:
    organizado = int(input('Pergunta 10: Você gosta de trabalho organizado? (1 para Sim, 0 para Não): '))
    if organizado not in [0, 1]:
        raise ValueError("A resposta deve ser 1 ou 0.")
except ValueError:
    print("Entrada inválida. Use 1 para Sim ou 0 para Não.")
    organizado = int(input('Pergunta 10: Você gosta de trabalho organizado? (1 para Sim, 0 para Não): '))

print(f"\nSuas respostas: {equipe, ar_livre, numeros, artes, tecnologia, complexo, comunicacao, cuidar_pessoa, fisico, organizado}")

filtro_equipe = df['equipe'] == equipe
filtro_ar_livre = df['ar_livre'] == ar_livre
filtro_numeros = df['numeros'] == numeros
filtro_artes = df['artes'] == artes
filtro_tecnologia = df['tecnologia'] == tecnologia
filtro_complexo = df['complexo'] == complexo
filtro_comunicacao = df['comunicacao'] == comunicacao
filtro_cuidar_pessoa = df['cuidar_pessoa'] == cuidar_pessoa
filtro_fisico = df['fisico'] == fisico
filtro_organizado = df['organizado'] == organizado

resultado = df[filtro_equipe & filtro_ar_livre & filtro_numeros & filtro_artes & filtro_tecnologia & filtro_complexo & filtro_comunicacao & filtro_cuidar_pessoa & filtro_fisico & filtro_organizado]

if not resultado.empty:
    profissao = resultado.iloc[0]['profissao'] 
    print(f'\nSua profissão ideal é: {profissao}')
else:
    print('\nNão foi possível identificar uma profissão com base em suas respostas.')
