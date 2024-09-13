import math

class Operacao: # A classe começa com letra maiuscula, e só o class pode fica colado no canto
    def __init__(self): # Esse é o Construtor do Pyton
        self.num1 = 0 # Se eu quiser adicionar mais uma coisa, eu coloco aqui, e eu teria que fazer auterações no coletar
        self.num2 = 0

    def coletar(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def somar(self, num1, num2):
        self.coletar(num1, num2) #Utilizando o método coletar
        return self.num1 + self.num2

    def subtrair(self, num1, num2):
        self.coletar(num1, num2)
        return self.num1 - self.num2

    def multiplicar(self, num1, num2):
        self.coletar(num1, num2)
        return self.num1 * self.num2

    def dividir(self, num1, num2):
        self.coletar(num1, num2)
        if self.num2 <= 0:
            return "Impossível dividir!"
        else:
            return self.num1 / self.num2

    def tabuada(self, num1): # O num1 não é muito importante, porque ele só precisas saber que tem que ter relação a uma variavel
        resultado = ""       # Mas na hora de chmar ele pode ser qualquer coisa
        for i in range(0,11,1): # Esse i tem a mesma função do i antigo de contar o range é pra contar de quanto em quanto
            resultado += f'\n{num1} * {i} = {num1 * i}'
        return resultado

    def potencia(self, base, expoente):
        return pow(base, expoente)

    def raiz(self, num):
        return math.sqrt(num)

    def exercicio1(self):
        msg = ""
        for i in range(1,11,1):
            msg += f'\n{i}'
        return msg

    def exercicio2(self):
        pares = ""
        for i in range(1,21,1):
            if i % 2 == 0:
                pares += f'\n{i}'
        return pares

    def exercicio3(self):
        calculo = 1
        for i in range(1,101,1):
            calculo = calculo + i
        return calculo

    def exercicio4(self):
        multiplo = 5
        resultado = ""
        for i in range(1,51,1):
            resultado += f'\n{multiplo} * {i} = {multiplo * i}'
        return resultado

    def exercicio5(self):
        resultado = ""
        self.num = int(input('Informe um número: '))# Desse jeito, o que eu escrever, vai ser enviado para o num
        if self.num % 2 == 0:
            resultado = "Número par"
        else:
            resultado = "Número impar"
        return resultado

    def exercicio6(self):
        resultado = ""
        self.num = int(input('Informe um número: '))
        if self.num >= 1:
            resultado = "O número é positivo"
        if self.num <= -1:
            resultado = "O número é negativo"
        if self.num == 0:
            resultado = "O númeoro é igual a 0"
        return resultado

    def exercicio7(self):
        tabuada = ""
        self.num = int(input('Informe um número'))
        for i in range(0,11,1):
            tabuada += f'\n{self.num} * {i} = {self.num * i}'
        return tabuada

    def exercicio8(self):
        resultado = ""
        self.num = int(input('Informe um número'))
        for i in range(0,self.num,1):
            resultado += f'\n{i}'
        return resultado

    def exercicio9(self):
        resultado = 1
        self.num = int(input('infome um número'))
        for i in range(0,self.num,1):
            resultado = resultado + i
        return resultado

    def exercicio10(self): # Assim eu posso mostra os números primos até um valor expecifico, nesse caso até o 20
        primo = "1\n2\n3\n5" # Caso eu queira outro valor, eu só preciso muda aquele 21
        for i in range(5,21,1):
            if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
                primo += f'\n{i}'
        return primo

    def exercicio11(self, num):
        if num == 2 or num == 3 or num == 5:
            return f'O {num} é primo!'
        elif num % 2 != 0 and num % 3 != 0 and num % 5 != 0:
            return f'O {num} é primo!'
        return f'O {num} não é primo!'


    def exercicio12(self):
        resposta = 1
        self.num = int(input('Informe um número: '))
        for i in range(1,self.num + 1):
            resposta *= i
        return resposta

    def exercicio13(self):
        resposta = 1
        for i in range(1,11,1):
            resposta = resposta + i
        return resposta


    def exercicio14(self):
        resposta = ""
        self.num = int(input('Informe um número: '))
        if self.num == 1 or self.num == 2 or self.num == 3 or self.num == 5 or self.num == 8 or self.num == 13 or self.num == 21:
            resposta = "O número faz parte da sequência de Fibonacci!"
        else:
            resposta = "O número não faz parte da sequência de Fibonacci!"
        return resposta

    def exercicio15(self): # Não feito
        resposta = ""
        self.num = int(input('Informe um número: '))

    def exercicio16(self):
        par = ""
        impar = ""
        self.num = int(input('Informe um número: '))
        for i in range(1,self.num,1):
            if i % 2 == 0:
                par += f'\nNúmero par: {i}'
            if i % 2 != 0:
                impar += f'\nNúmero impar: {i}'
        return f'{par} \n{impar}'

    def exercicio17(self):
        primo = "1\n2\n3\n5"
        self.num = int(input('Informe um número: '))
        for i in range(5,self.num,1):
            if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
                primo += f'\n{i}'
        return primo

    def exercicio18(self):
        resposta = 0
        contar = ""
        self.num = int(input('Informe um número: '))
        while self.num > 1:
            if self.num % 2 == 0:
                self.num = self.num / 2
                contar = f'\n{self.num}'
            else:
                self.num = 3 * self.num + 1
                resposta += 1
                contar = f'\n{self.num}'
            return f'{contar}\nResultado: {resposta}'

    def exercicio19(self):
        par = 0
        impar = 0
        self.num = int(input('Informe um número: '))
        for i in range(1,self.num,1):
            if i % 2 == 0:
                par += i
            else:
                impar = i + impar
        return f'A soma dos pares é: {par}\nA soma dos impares é: {impar}'

    def exercicio20(self):
        resposta = ""
        self.num = int(input('Informe um número: '))
        for i in range(1,self.num,1):
            if i % self.num == 0:
                resposta = resposta + i
        if resposta == self.num:
            return f'O número {resposta} é um número perfeito'
        else:
            return f'O número {resposta - self.num} não é um número perfeito'
