#consiste em comparar dois valores, verificar qual é menor e colocar na posição correta

#função built-in sorted() e o método sort() presente nos objetos da classe list

#pesquisar exercicios com sorted e sort

lista = [7,4]

if lista[0] > lista[1]:
    aux = lista[1]
    lista[1] = lista[0]
    lista[0] = aux

print(lista)

#usando atribuição composta do python

lista2 = [5,-1]
if lista2[0] > lista2[1]:
    lista2[0], lista2[1] = lista2[1], lista2[0]

print(lista2)

#selection sort (ordenação por seleção)
#percorre toda a lista, procurando o menor valor para ocupar a posição 0
#a partir da posição 1, percorre toda a lista procurando o menor valor para ocupar a posição 1
#a partir da posição 2, percorre toda a lista procurando o menor valor para ocupar a posição 2
#esse processo é repetido n-1 vezes, sendo n o tamanho da lista

#bubble sort (ordenação por bolha)
#faz a ordenação sempre a partir do inicio da lista comparando um valor com seu vizinho
#é repetido até que todos os valores estejam na posição correta
#seleciona o  valor na posição 0 e compara com seu vizinho, se for menor há troca, se não seleciona o próximo e compara repetindo o processo
#depois que termina até o fim da lista, ele recomeça verificando do indice 0 e faz todo o mesmo processo

#merge sort(ordenação por  junção)
#faz a ordenação em duas etapas
#divide a lista em sublistas
#e junta(merge) as sublistas já ordenadas
#o paradigma de dividir e conquistar envolve 3 etapas em cada nível
#1. dividir o problema em vários subproblemas
#2. conquistar os subproblemas, resolvendo-os recursivamente, se os tamanhos dos subproblemas forem pequenos o suficiente, apenas resolva de maneira direta
#3. combinar as soluções dos subproblemas na solução do problema original
