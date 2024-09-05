pessoa ={
    'nome': 'Luiz', #String
    'sobrenome': 'Miranda',
    'idade': 18, #Int
    'altura': 1.8, #Float
    'endereços':[ #Lista
        {'rua': 'TAL', 'número': 123},
        {'rua': 'TAL2', 'número': 321},
    ]
}
"""
#Acessa tudo do dicionário
#print(pessoa, type(pessoa))
#Acessa uma parte específica do dic
print(pessoa['nome'])
print()
#Pega tudo só que organizado
for chave in pessoa:
    print(chave, pessoa[chave])
"""

"""
"""
#Manuplando chaves e valores em dic
chave = 'nome'
pessoa[chave] = 'Jorge'
pessoa['sobrenome']= 'Otário'
#print(pessoa)
print(pessoa[chave])
del pessoa['sobrenome']
NaoAchou = pessoa.get('sobrenome', 'Não achou')
print(NaoAchou)