print("Olá mundo") 

#é uma linguagem interpretada
#permite atribuição múltipla

#variáveis são espaços alocados na memória RAM pra armazenar valores temporariamente
#não precisa ser tipado pois a tipagem é dinâmica

#para saber o tipo de dado de uma variável
x = 10
nome = "Jana"
nota = 8.5
flag = True
print(type(x))
print(type(nome))
print(type(nota))
print(type(flag))
#tudo é objeto por isso aparecem com "class"

idade = int(input("Digite sua idade: "))
print(idade)

#existem várias formas de imprimir valores
#modo1:
materia = input("Qual é sua materia? ")
print("Boas vindas a disciplina de %s" % (materia))

#modo2:
print("Boas vindas a disciplina de {}".format(materia))

#modo3 e mais usada:
print(f"Boas vindas a disciplina de {materia}")

#primeiro resolve os parenteses do mais interno para o externo
#exponenciação
#multiplicação e divisão
#soma e subtração
op1 = 2 + 3 * 5
op2 = (2 + 3) * 5
op3 = 4/2 ** 2
op4 = 13 % 3 + 4

#operadores relacionais: == != > < >= <=

if idade > 17:
    print("Você é maior de idade!")
else:
    print("Você é menor de idade!")

semaforo = "amarelo"
if semaforo == "verde":
    print("Pode passar")
elif semaforo == "amarelo":
    print("Atenção!!!")
else:
    print("Pare!!!")

#estruturas lógicas and or not

if semaforo == "verde" and idade > 17:
    print("Você provavelmente já tirou a carteira")

if idade < 18 or semaforo == "vermelho":
    print("Você provavelmente ainda não pode dirigir")

booleano = True
booleano = not booleano
print(booleano)

#estruturas de repetição:

numero = 1
while numero != 0:
    numero = int(input("Digite um número: "))

    if numero % 2 == 0:
        print("Número par!")
    else:
        print("Número ímpar!")


sobrenome = "Tavares"

# for i in sobrenome:
#     print(i)

for i, j in enumerate(sobrenome):
    print(f"Posição = {i}, valor = {j}")

for x in range(5):
    print(x)
#resultado: 0, 1, 2, 3, 4

#a função range() pode ser usada de 3 formas:
#passando um único argumento que representa a quantidade de vezes que o laço deve repetir
# passando dois argumentos, um que representa o inicio das repetições e outro o limite superior (nao incluido) do valor da variável de controle
# passando 3 argumentos, inicio da repetição, limite superior(nao incluido) do valor da variável de controle e um que representa o incremento

texto1 = "Linguagem de programação"

for c in texto1:
    if c == 'a':
        break
    else:
        print(c)

# for c in texto1:
#     if c == 'a':
#         continue
#     else:
#         print(c)

#função built-in é um objeto que está integrado ao núcleo do interpretador, não precisa ser feito instalação adicional

def faculdade(disciplina,curso):
    print(f"Minha primeira função em Python desenvolvida na disciplina de {disciplina}, do curso: {curso}")

faculdade("Linguagem de Programação", "Desenvolvimento Mobile")


#Funções com Parâmetros

#1. Parâmetro posicional, obrigatório, sem valor default, tentar invocar a função sem passar os parâmetros, irá acarretar em erro
def somar(a,b):
    return a + b

resp = somar(2, 3)
print(resp)

#2. Parâmetro posicional, obrigatório com valor default, quando a função for invocada caso nenhum valor seja passado o default é utilizado
def calcular_desconto(valor, desconto=0):
    valor_com_desconto = valor - (valor * desconto)
    return valor_com_desconto

valor1 = calcular_desconto(100) #não aplica nenhum desconto
valor2 = calcular_desconto(100, 0.30) #aplica desconto de 30%

print(f"Valor sem desconto = {valor1}")
print(f"Valor com desconto = {valor2}")

#3. Parâmetro nominal, obrigatório, sem valor default, não importa a posição dos parâmetros pois são identificados pelo nome, é obrigatório passar todos os valores
#4. nesse também pode ter valor default e no momento de evocar pode usar só o parâmetro sem valor default
def converter_maiuscula(texto2, flag_maiuscula):
    if flag_maiuscula: #se for verdadeiro
        return texto2.upper()
    else: #se for falso
        return texto2.lower()
    
conversao = converter_maiuscula(flag_maiuscula=False, texto2="JaNainA")
print(conversao)

#5. Parâmetro posicional e não obrigatório(args) a passagem é feita de modo posicional porém a quantidade não é conhecida
# def imprimir_parametros(*args):
#     qtd_parametros = len(args)
#     print(f"Quantidade de parametros = {qtd_parametros}")

#     for i, valor in enumerate(args):
#         print(f"Posição = {i}, valor = {valor}")

# print("Chamada 1")
# imprimir_parametros("Curitiba", 10, 34.67, "Jana")
# print("Chamada 2")
# imprimir_parametros(28, "Fazenda Rio Grande")

#6. Parâmetro nominal e nao obrigatório (kwargs), feita de modo nominal e não posicional, permitindo acessar o valor do parametro quanto o nome da variável que o armazena
# o retorno do type será 'dict' de dicionário
def imprimir_parametros(**kwargs):
    print(f"Tipo de objeto recebido = {type(kwargs)}")
    qtd_parametros = len(kwargs)
    print(f"Quantidade de parametros = {qtd_parametros}")

    for chave, valor in kwargs.items():
        print(f"Variável = {chave}, valor = {valor}")

print("Chamada 1")
imprimir_parametros(cidade="Curitiba", idade=10, temp=34.67, nome="Jana")
print("Chamada 2")
imprimir_parametros(desconto=30, valor=100)

#funções anonimas
#é ideal para funções simples e rápidas na mesma linha
somar = lambda x,y: x + y
somar(x=5, y=7)

