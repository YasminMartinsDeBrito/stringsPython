minha_variavel = "Hello Q3"
print(minha_variavel)

nome = 'Yasmin'
print(nome[-1])
print(nome[:2])
print(nome[2:])
print(nome[1:4:2])

# join
minha_lista = ['1','2','3']
novo = '+'.join(minha_lista)
print(novo)

# split
s = '1 + 2 + 3'
novos = s.split('+')
print(novos)

# capitalize
s = 'alguma STRING'
caps = s.capitalize()
print(caps)


# count
s = 'O rato roeu a roupa'
sc = s.count('ro')
print(sc)

# endswith
s = "Bem vindos ao Q3."
bem = s.endswith('3.')
print(bem)

# lower
s = "ALGUMA STRING"
bes = s.lower()
print(bes)

# upper
s = 'alguma string'
nova = s.upper()
print(nova)

# replace
s = 'Alguma string'
meu = s.replace('g','z')
print(meu)

