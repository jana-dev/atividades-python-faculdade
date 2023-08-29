texto = "Aprendendo Python na disciplina de linguagem de programação"

print(f"Tamanho do texto = {len(texto)}")
print(f"Python in texto = {'Python' in texto}")
print(f"Quantidade de a no texto = {texto.count('a')}")
print(f"As 5 primeiras letras são: {texto[0:5]}")

vogais = ['a', 'e', 'i', 'o', 'u']
for vogal in vogais:
    print(f'Posição = {vogais.index(vogal)}, valor = {vogal}')


#slipt() usada para cortar um texto e transforma-lo em lista.
#Pode ser usada sem nenhum parâmetro, nesse caso a string será cortada a cada espaço em branco
#Caso seja passado um parâmetro texto.slipt(","), então o corte é feito no parâmetro específicado

palavras = texto.split()
print(f"palavras = {palavras}")
print(f"Comprimento de palavras = {len(palavras)}")

#Compreensões de lista, também chamada de listcomp
#É utilizada quando dada uma sequência, deseja-se criar uma nova sequência porém com informações originais transformadas ou filtradas por um critério.

#Lista:estrutura de dados sequencial que possui como principal característica ser mutável.
#novos valores podem ser adicionados ou movidos
#em python usa-se para criar: lista = []
#lista = ['a', 'b', 'c']
#usando o listcomp [x for x in iterable]
#usando construtor de tipo list()

linguagens = ['Python', 'Java', 'Javascript', 'C', 'C#', 'C++', 'Swift', "Lua"]

print(f"Antes da listcomp = {linguagens}")

linguagens = [item.lower() for item in linguagens]
print(f'Depois da listcomp = {linguagens}')

#map() é utilizada para aplicar uma determinada função em cada item de um objeto iterável

print("Exemplo map")
cidades = '''Curitiba Mandirituba Florianopolis Londrina Cascavel Itapoa Matinhos'''.split()
nova_lista = map(lambda x: x.lower(), cidades) #forma diferente de fazer a atividade de cima
print(f'A nova lista é = {nova_lista}')
nova_lista = list(nova_lista)
print(f'Agora sim, nova lista é = {nova_lista}')

#range() cria um objeto iterável
#usamos o construtor list() para transformar uma lista com números
#criamos uma nova lista com filter() que irá retornar somente pares

numeros = list(range(0,21))

numeros_pares = list(filter(lambda x: x%2 == 0, numeros))
print(numeros_pares)

#tuplas são imutáveis tupla1 = (), tupla2 = ('a', 'b', 'c'), construtor de tipo tuple()

vogais2 = ('a', 'e', 'i', 'o', 'u')
print(f'Tipo do objeto vogais = {type(vogais)}')

for p, x in enumerate(vogais2):
    print(f'Posição = {p}, valor = {x}')

