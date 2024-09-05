"""
Métodos úteis
len - quantas chaves
keys - iterável com as chaves
values - iterável com os valores
items - iterável com chaves e valores
setdefault - adiciona valor se a chave não existe
copy - retorna uma cópia rasa(shallow copy)
get - obtém uma chave
pop - Apaga um item com a chave especifíca (del)
popitem - Apaga o último item adicionado
update - Atualiza um dicionário com outro
"""
pessoa = {
    'nome': 'Luiz',
    'sobrenome':'Miranda',
    #'idade': 900
}

#pessoa.setdefault('idade',0)
#rint(pessoa['idade'])

#print(len(pessoa))
#print(list(pessoa.key()))
#print(list(pessoa.values()))
#print(list(pessoa.items()))

#nome = pessoa.pop('nome')
#print(nome)
#print(pessoa)

#ultima_chave = pessoa.popitem()
#print(ultima_chave)

pessoa.update({
    'nome': 'Jorge',
    'idade': 222,
})
# OU
#pessoa.update(nome='Jorge', idade=222)
# OU
#tupla=('nome', 'Jorge', 'idade', 22222)
#pessoa.update(tupla)


#for valor in pessoa.values():
#   print(valor)
#for chave, valor in pessoa.items():
#   print(chave,valor)


"""
#------COPY--------
import copy
d1 = {
    'c1':1,
    'c2':2,
    'l1':[0, 1, 2],
}
#d2 = d1.copy() #Cópia sem valor mutávels
d2 = copy.deepcopy(d1) #Cópia firme
d2['c1'] =1000
d2['l1'][1] = 999999
print(d1)
print(d2)
"""