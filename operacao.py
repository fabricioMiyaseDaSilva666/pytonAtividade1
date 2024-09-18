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
        num = int(input('Informe um número: '))
        divisores = 0
        for i in range(1,num + 1):
            if num % i == 0:
                divisores += i
        if divisores - num == num:
            return f'{num} é um número perfeito'
        else:
            return f'{num} não é um número perfeito'

    def part2exercicio1(self):
        num1 = 10
        num2 = 20
        x = num2 # Assim dá pra troca dois valores
        num2 = num1
        num1 = x
        return f'Número 10 agora é: {num1} \nNúmero 20 agora é: {num2}'

    def part2exercicio2(self):
        num = int(input('Informe um número: '))
        num -= 1
        return f'O número anterior ao número digitado é: {num}'

    def part2exercicio3(self):
        base = int(input('Informe o primeiro número: '))
        altura = int(input('Informe o segundo número: '))

        area = base * altura

        return f'A área do retângulo é: {area}'

    def part2exercicio4(self):
        dia = int(input('Informe um número de dias: '))
        mes = int(input('Informe o mes: '))
        ano = int(input('Informe o ano: '))
        if mes < 1 or mes > 13:
            return "Erro! Informe um número maior que 0 ou menor que 13"
        mes = mes * 30
        ano = ano * 365
        dia = dia + mes + ano
        return f'A sua idade em forma de dias é {dia}'

    def part2exercicio5(self): # Não está certo
        branco = int(input('Informe o número de votos branco: '))
        nulo = int(input('Informe o número de votos nulos: '))
        valido = int(input('Informe o número de votos validos: '))
        nuloFinal = 0
        validoFinal = 0
        brancoFinal = 0
        total = 0

        validoFinal = (valido + branco + nulo) % 3

        return f'A porcentagen de votos finais é: {validoFinal}'

    def part2exercicio6(self): #salario * reajuste % 100
        salario = int(input('Informe o salario: '))
        if salario < 0:
            return "Número invalido, informe um valor maior que 0"
        porcentual = int(input('Informe o porcentual do reajuste: '))
        reajuste = 0
        salarioFinal = 0

        porcentual = porcentual / 100
        reajuste = porcentual * salario
        salarioFinal = salario + reajuste

        return f'O reajuste do seu salário final é de: {salarioFinal}'

    def part2exercicio7(self):
        distribuidora = 28
        porcentoDistr = 0
        imposto = 45
        impostoFin = 0
        custoCar = int(input('Informe o valor do carro: '))
        dorCabeca = 0
        custoCarFinal = 0

        porcentoDistr = distribuidora / 100
        impostoFin = imposto / 100
        dorCabeca = porcentoDistr * impostoFin
        custoCarFinal = dorCabeca + custoCar

        return f'O valor final do carro, com todos os impostos será de: {custoCarFinal}'

    def part2exercicio8(self):
        nota1 = int(input('Informe a primeira nota: '))
        if nota1 < 0:
            return "Erro! Informe um valor maior que 0"
        nota2 = int(input('Informe a segunda nota: '))
        if nota2 < 0:
            return "Erro! Informe um valor maior que 0"
        nota3 = int(input('Informe a terceira nota: '))
        if nota3 < 0:
            return "Erro! Informe um valor maior que 0"
        mediaFinal = 0
        mediaFinal = (nota1 + nota2 + nota3) / 3

        return f'A média das notas são de: {mediaFinal}'

    def part2exercicio9(self):
        maca = 1.30
        quantidadeMaca = int(input('Informe a quantidade de maçã: '))
        if quantidadeMaca >= 12:
            maca = 1
        return f'O valor total das maçã será de: {maca * quantidadeMaca}'

    def part2exercicio10(self):
        num1 = int(input('Informe um número: '))
        num2 = int(input('Informe um número: '))
        num3 = int(input('Informe um número: '))
        num4 = int(input('Informe um número: '))
        num5 = int(input('Informe um número: '))
        final = num1,num2,num3,num4,num5

        return f'Essa é a ordem crescente\n {sorted(final)}' # O sorted coloca todos os números em forma crescente

    def part2exercicio11(self):
        salario = int(input('Informe o salário: '))
        if salario < 0:
            return "Erro! Informe um valor maior que 0"
        porcentagem = 3
        vendas = int(input('Informe as vendas: '))
        salarioCalculo = 0
        salarioFinal = 0
        if vendas < 0:
            return "Erro! Informe um valior maior que 0"
        if vendas > 1500:
            porcentagem = 5/100
        else:
            porcentagem = 3/100
        salarioCalculo = vendas * porcentagem
        salarioFinal = salario + salarioCalculo
        return f'O salário final será de: {salarioFinal}'

    def part2exercicio12(self):
        saldoTotal = 0
        saldo = int(input('Informe o saldo: '))
        debito = int(input('Informe o débito: '))
        credito = int(input('Informe o crédito: '))

        saldoTotal = saldo - debito + credito

        if saldoTotal < 0:
            return f'{saldoTotal} Saldo negativo'
        else:
            return f'{saldoTotal} Saldo positivo'

    def part2exercicio13(self):
        num = int(input('Informe um número: '))
        resultado = ""
        if num < 0:
            return "Erro! Informe um valor maior que 0"
        if num >= 11:
            return "Erro! Informe um valor menor que 11"
        for i in range(1,11,1):
            resultado += f'\n{num} * {i} = {num * i}'
        return f'A tabuada do {num} é: {resultado}'

    def part2exercicio14(self):
        num = int(input('Informe um número: '))
        resultado = ""
        if num >= 10:
            return "Esse número não é inteiro, informe outro número"
        for i in range(1,num,1):
            resultado += f'\n {i}'
        return {resultado + 1}

    def part2exercicio15(self):
        num1 = int(input('Informe um número: '))
        num2 = int(input('Informe outro número: '))
        num3 = int(input('Informe outro número: '))
        num4 = int(input('Informe outro número: '))
        num5 = int(input('Informe outro número: '))
        negativo = 0

        if num1 < 0:
            negativo = negativo + 1
        if num2 < 0:
            negativo = negativo + 1
        if num3 < 0:
            negativo = negativo + 1
        if num4 < 0:
            negativo = negativo + 1
        if num5 < 0:
            negativo = negativo + 1
        return f'{negativo} números são negativos'

    def part2exercicio16(self):
        num1 = int(input('Informe um número: '))
        num2 = int(input('Informe um número: '))
        num3 = int(input('Informe um número: '))
        num4 = int(input('Informe um número: '))
        num5 = int(input('Informe um número: '))
        soma = 0

        if num1 < 40:
            soma = soma + num1
        if num2 < 40:
            soma = soma + num2
        if num3 < 40:
            soma = soma + num3
        if num4 < 40:
            soma = soma + num4
        if num5 < 40:
            soma = soma + num5
        return soma

    def part2exercicio17(self):
        soma = 0
        valor_intervalo = len(range(15, 101))

        for i in range(15, 101):
            soma += i
        media = soma / valor_intervalo

        print("media geral {}".format(media))

    def part2exercicio18(self):
        num1 = int(input('Informe um número: '))
        num2 = int(input('Informe um número: '))
        num3 = int(input('Informe um número: '))
        media = 0
        soma = 0
        maior = 0
        menor = 0
        if maior < num1:
            maior = num1
        if maior < num2:
            maior = num2
        if maior < num3:
            maior = num3
        menor = [num1, num2, num3]
        soma = sum(menor)
        media = soma / len(menor)
        return f'O maior número é: {maior}\nA média dos números é: {media}'

    def part2exercicio19(self):
        nota1 = int(input('Informe a nota: '))
        if nota1 < 0:
            return "Erro! Informe um valor maior que 0"
        nota2 = int(input('Informe a nota: '))
        if nota2 < 0:
            return "Erro! Informe um valor maior que 0"
        nota3 = int(input('Informe a nota: '))
        if nota3 < 0:
            return "Erro! Informe um valor maior que 0"
        nota4 = int(input('Informe a nota: '))
        if nota4 < 0:
            return "Erro! Informe um valor maior que 0"
        nota5 = int(input('Informe a nota: '))
        if nota5 < 0:
            return "Erro! Informe um valor maior que 0"
        media = (nota1 + nota2 + nota3 + nota4 + nota5) / 5
        contarNota = 0

        if nota1 > media:
            contarNota = contarNota + 1
        if nota2 > media:
            contarNota = contarNota + 1
        if nota3 > media:
            contarNota = contarNota + 1
        if nota4 > media:
            contarNota = contarNota + 1
        if nota5 > media:
            contarNota = contarNota + 1
        return f'A média de notas da turma é: {media}\n{contarNota} estão acima da média'

    def part2exercicio20(self):
        media = 0
        maior = 0
        menor150 = 0
        mediaFilhos = 0
        salario = int(input('Informe o salario: '))
        while salario > 0:
            filhos = int(input('Informe o número de filhos: '))
            salario = int(input('Informe o salario: '))
            mediaFilhos += filhos / 5
            media += salario / 5
            if maior < salario:
               maior = salario
            if salario < 150:
               menor150 += 1
        return f'A média de salario é: {media}\n' \
               f'A média de número de filhos é: {mediaFilhos}\n' \
               f'o maior salário é: {maior}\n' \
               f'A porcentagem de pessoas com salário menor que 150 é de: {menor150 / 100}'