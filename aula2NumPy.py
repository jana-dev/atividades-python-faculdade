import numpy

#Objetos do tipo array NumPy
#biblioteca científica com python
#poderoso objeto matriz (array) n-dimensional
#ferramentas para integrar código c/c++ e fortran
#recursos úteis de álgebra linear, transformação de Fourier e números aleatórios

matriz_1_1 = numpy.array([1,2,3]) #cria matriz com 1 linha e 1 coluna
print(type(matriz_1_1))
print(f"Matriz_1_1 = {matriz_1_1}")

matriz_2_2 = numpy.array([[1,2], [3,4]]) #matriz com 2 linhas e 2 colunas
print(f"Matriz_2_2 = \n {matriz_2_2}")

matriz_3_2 = numpy.array([[1,2], [3,4], [5,6]]) #3 linhas 2 colunas
print(f"Matriz_3_2 = \n {matriz_3_2}")

matriz_2_3 = numpy.array([[1,2,3], [4,5,6]])
print(f"Matriz_2_3 = \n {matriz_2_3}")