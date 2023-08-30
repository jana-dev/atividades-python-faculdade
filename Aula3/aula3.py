#orientação a objetos

#classe é uma abstração que que descreve entidades do mundo real
#quando são instanciadas dão origem a objetos com características similares
#a classe é o modelo e o objeto é uma instância

#abstração classes e objetos
#objetos são os componentes de um programa OO.
#a Classe é uma forma de organizar os dados de um objeto e seus comportamentos
#entende-se por instância a existencia em memória do objeto

#cada diagrama de classes é definido por 3 seções separadas:
#1. o nome da classe
#2. os dados
#3. os comportamentos

#atributos:
#os dados armazenados de um objeto representam o estado do objeto
# contém as informações que diferenciam os vários objetos
#características de um objeto
#podem ser: variáveis: nome, peso, altura, cor, cpf, etc.

#métodos:
#ações que os objetos podem exercer quando solicitados
#onde podem interagir e se comunicar com outros objetos
#exemplo: andar(), pular(), comprar() etc.

#herança:
#é possível fazer o reuso de código, criando soluções mais organizadas
#permite que uma classe herde os atributos e métodos de outra classe

#encapsulamento:
#ato de combinar os atributos e métodos na mesma entidade
#prática de tornar atributos privados, quando estes são encapsulados em métodos para guardar e acessar seus valores
#ocultação de informação

#polimorfismo:
#significa muitas formas, permite ao dev usar o mesmo elemento de formas diferentes

#classes e métodos em python:

class PrimeiraClasse:
    def imprimir_mensagem(self,nome): #criando um método
        print(f"Olá {nome}, seja bem vindo!!!")

objeto1 = PrimeiraClasse() #Instanciando um objeto do tipo PrimeiraClasse
objeto1.imprimir_mensagem('Jana') #Invocando o método

#construtor de classe:
#atributos de instância, também chamadas de variáveis de instancias
#esse atributo é capaz de receber um valor diferente para cada objeto
#a sintaxe é: self.nome_atributo
#ao instanciar um novo objeto, é possivel determinar um estado inicial para variáveis de instancias por meio do método construtor da classe

class Televisao:
    def __init__(self):
        self.volume = 10
    def aumentar_volume(self):
        self.volume +=1
    def diminuir_volume(self):
        self.volume -=1

tv = Televisao()
print(f"Volume ao ligar a tv = {tv.volume}")
tv.aumentar_volume()
print(f"Volume atual = {tv.volume}")

#variáveis e métodos privados
#em linguagens como Java, C#, as classes, os atributos e os métodos são acompanhados de modificadores de acesso: public, private e protected
#em Python NAO existem modificadores, tudo é publico
#para simbolizar o privado, por convenção, usa-se um sublinhado antes do nome: _cpf, _calcular()

class ContaCorrente:
    def __init__(self):
        self._saldo = None
    def depositar(self,valor):
        self._saldo += valor
    def consultar_saldo(self):
        return self._saldo
    
#herança em python:
#uma classe aceita múltiplas heranças

#métodos mágicos em python
#quando uma classe é criada ela herda, mesmo que nao declarado explicitamente todos os recursos de uma classe-base chamada objetc
#exemplo dir()

#método construtor na herança e sobrecrita
#na herança, quando adicionamos a função __init__(), a classe filho não herdará o construtor dos pais
#o construtor da classe filho, sobrescreve o da classe pai.
#para utilizar o construtor da classebase, é necessário invoca-lo explicitamente, dentro do ocnstrutor filho ex: ClassePai.__init__()
#obs: não entendi nada depois pesquisar por fora com exemplos práticos porque só na teoria fica difícil

#herança múltipla
#python permite que uma classe filha herde recursos de mais de uma superclasse
#basta declarar cada classe separada por vírgula

#pesquisar mais sobre OO em python, fazer exercícios práticos e também ver se realmente na prática é comum se utilizar desse paradigma