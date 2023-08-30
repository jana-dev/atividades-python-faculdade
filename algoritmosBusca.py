#Temos a operação in ou not in usada para verificar se um valor está em uma sequência

nomes = 'Jana Marcela Ezequiel Lucas Bianca Joanita Priscila'.split()

print('Jana' in nomes)
print('Larissa' in nomes)

#Busca Linear (ou sequencial)

#percorre os elementos da sequencia procurando aquele de destino
#começa por uma das extremidades até encontrar ou nao o valor
#pesquisa linear pode ser muito custoso computacionalmente

#para implementar a busca linear, vamos precisar de uma estrutura de repetição for e uma if para verificar se o valor é o que buscamos

def executar_busca_linear(lista,valor):
    for elemento in lista:
        if valor == elemento:
            return True
    return False

lista_numerica = [10, 5, 8, 20, 4, 2, 1, 3]
print(lista_numerica)
resultado_busca_linear = executar_busca_linear(lista_numerica,80)
print(resultado_busca_linear)

vogais = 'aeiou'
resultado = vogais.index('e')
print(resultado)

#estudo da viabilidade de um algoritmo, em termos de espaço e tempo de processamento, é chamado de análise da complexidade do algoritmo

#busca binária é outro algoritmo para buscar um valor em uma sequencia
#a diferença entre linear e binário é que com binário os valores precisam estar ordenados
#lógica:
#encontra o item do meio da sequencia (meio da lista)
#se o valor procurado == ao item do meio, a busca encerra
#se não for, verifica se o valor buscado é maior ou menos que o valor central
#se for maior, então a busca acontecerá na metade superior e a inferior é descartada
#se não for, a busca irá acontecer na metade inferior da sequencia e a superior é descartada
#ao encontrar o valor central a busca binária a divide em duas partes, o que justifica o nome

def executar_busca_binaria(lista,valor):
    minimo = 0
    maximo = len(lista) - 1

    while minimo <= maximo:
        #encontra o elemento que dividie a lista no meio
        meio = (minimo + maximo) // 2
        #verifica se o valor procurado está a esquerda ou a direita do valor central
        if valor < lista[meio]:
            maximo = meio - 1
        elif valor > lista[meio]:
            minimo = meio + 1
        else:
            return True #se o valor for encontrado para aqui
        
    return False #se chegar até aqui, significa que o valor não foi encontrado

lista_binaria = [1,3,5,6,8,9,12,15,18,23,25,34,35,36,42,56,76,78,89,90,91,95,100]    
resultado_busca_binaria = executar_busca_binaria(lista_binaria,8)
print(resultado_busca_binaria)


