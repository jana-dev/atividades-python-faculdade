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

#tuplas são imutáveis e podem ser construidas de 3 formas:
#tupla1 = (), tupla2 = ('a', 'b', 'c'), construtor de tipo tuple()

vogais2 = ('a', 'e', 'i', 'o', 'u')
print(f'Tipo do objeto vogais = {type(vogais)}')

for p, x in enumerate(vogais2):
    print(f'Posição = {p}, valor = {x}')
# a utilização de tuplas ocorre em casos nas quais a ordem dos elementos é importante e não pode ser alterada

#Objetos do tipo set:
#habilita operações matematicas de conjuntos como:
#união, intersecção, diferença etc
#pode ser usado em testes de associação e remoção de valores duplicados de uma sequencia
#podemos também adicionar um novo elemento a um conjunto com a função add(valor)
#e remover com a função remove(valor)
#podem ser construidos: set1 = {'a', 'b', 'c'}
#usando o construtor de tipo: set(iterable)

def remover_duplicatas(lista):
    conjunto = set(lista)
    lista_sem_duplicatas = list(conjunto)
    return lista_sem_duplicatas

# Lista com duplicatas
numeros = [2, 4, 6, 8, 4, 10, 6, 12, 14, 8]

# Remover duplicatas usando a função
numeros_sem_duplicatas = remover_duplicatas(numeros)

print("Lista original:", numeros)
print("Lista sem duplicatas:", numeros_sem_duplicatas)

# a função remover_duplicatas recebe uma lista como entrada e converte essa lista em um conjunto utilizando set(). 
# Isso remove automaticamente os elementos duplicados, já que conjuntos não permitem elementos repetidos.
#Em seguida, a função converte o conjunto novamente em uma lista para retornar o resultado sem duplicatas.

#Objetos do tipo mapping
#possuem um mapeamento entre uma chave e um valor
#o objeto que possui essa propriedade é o dict (dicionário)
#como esse objeto é mutável, conseguimos atribuir um novo valor a uma chave já existente

#podem ser construidos: dicionario1 = {}, dicionario2 = {'one':1, 'two':2, 'three':3}, usando construtor de tripo dict()
#Não é possível criar um set vazio set={}, pois essa é a forma de construção de um dict

#exemplo1 de criação:
dici_1 = {}
dici_1['nome'] = "Jana"
dici_1['idade'] = 28

#exemplo2 de criação na forma chave:valor
dici_2 = {'nome': 'Jana', 'idade': 28}

#exemplo3 criação com uma lista de tuplas, cada tupla representa um par chave:valor
dici_3 = dict([('nome', "Jana"), ('idade', 28)])




