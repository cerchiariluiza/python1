# #exemplos de listas ()
# def variaveis_locais():
#     lista = ['Julia','Marcelo','Gabriela']
#     if 'Julio' in lista:
#         print('existe')
#     else:
#         print('Não existe')
#     print(type(lista))
#     print(lista[0])
# variaveis_locais()
# #print(lista[0])

# #lendo dicionarios em json
# import json
# with open('arquivod.json', 'r', encoding='utf8') as f:
#     print(json.load(f))
#     print(type(f))

    # arm = json.load(f)
    # print(type(arm))

# #lendo listas em python      
# with open('dataset.txt', 'r') as arq:
# 	lista = arq.read().splitlines()


f = open('exemplo.txt', 'r')
for line in f:
    print(line)

