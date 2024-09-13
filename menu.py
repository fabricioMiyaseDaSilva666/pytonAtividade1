from operacao import Operacao

class Menu:
    def __init__(self):
        self.opcao = -1
        self.opera = Operacao()
        self.num1 = 0
        self.num2 = 0

    def mostrarMenu(self):
        print('\n-----MENU-----\n\n' +
              'Escolha uma das opções abaixo: ' +
              '\n0.  Sair' +
              '\n1.  Somar' +
              '\n2.  Subtrair' +
              '\n3.  Dividir' +
              '\n4.  Multiplicar' +
              '\n5.  Potência' +
              '\n6.  Raiz' +
              '\n7.  Tabuada' +
              '\n8.  exercicio1' +
              '\n9.  exercicio2' +
              '\n10. exercicio3' +
              '\n11. exercicio4' +
              '\n12. exercicio5' +
              '\n13. exercicio6' +
              '\n14. exercicio7' +
              '\n15. exercicio8' +
              '\n16. exercicio9' +
              '\n17. exercicio10' +
              '\n18. exercicio11' +
              '\n19. exercicio12' +
              '\n20. exercicio13' +
              '\n21. exericico14' +
              '\n22. exercicio15' +
              '\n23. exercicio16' +
              '\n24. exercicio17' +
              '\n25. exercicio18' +
              '\n26. exercicio19' +
              '\n27. exercicio20')

    def coletar(self):
        self.num1 = int(input('Informe o primeiro número: '))
        self.num2 = int(input('Informe o segundo número: '))

    def operacao(self):
        while self.opcao != 0:
            self.mostrarMenu()  # Chamar as Opções
            self.opcao = int(input('Escolha uma das opções acima: '))
            if self.opcao == 0:
                print('Obrigado!!!')
            if self.opcao == 1:
                self.coletar() # Chamando o input por meio so coletar
                print(f'A soma dos números é: {self.opera.somar(self.num1, self.num2)}')

            elif self.opcao == 2: #O elif é a mesma coisa do else if
                self.coletar()
                print(f'A subtração dos números digitados é: {self.opera.subtrair(self.num1, self.num2)}')

            elif self.opcao == 3:
                self.coletar()
                print(f'A divisão dos números digitados é: {self.opera.dividir(self.num1, self.num2)}')

            elif self.opcao == 4:
                self.coletar()
                print(f'A multiplicação dos números digitados é: {self.opera.multiplicar(self.num1, self.num2)}')

            elif self.opcao == 5:
                self.coletar()
                print(f'A potência dos números digitados é: {self.opera.potencia(self.num1, self.num2)}')

            elif self.opcao == 6:
                self.coletar()
                print(f'A Raiz de {self.num1} é: {self.opera.raiz(self.num1)}')
                print(f'A Raiz de {self.num2} é: {self.opera.raiz(self.num2)}')

            elif self.opcao == 7:
                self.coletar()
                print(f'A tabuada de {self.num1} é: {self.opera.tabuada(self.num1)}')
                print(f'A tabuada de {self.num2} é: {self.opera.tabuada(self.num2)}')

            elif self.opcao == 8:
                print(self.opera.exercicio1())

            elif self.opcao == 9:
                print(self.opera.exercicio2())

            elif self.opcao == 10:
                print(self.opera.exercicio3())

            elif self.opcao == 11:
                print(self.opera.exercicio4())

            elif self.opcao == 12:
                print(f'O número é: {self.opera.exercicio5()}')

            elif self.opcao == 13:
                print(self.opera.exercicio6())

            elif self.opcao == 14:
                print(self.opera.exercicio7())

            elif self.opcao == 15:
                print(self.opera.exercicio8())

            elif self.opcao == 16:
                print(self.opera.exercicio9())

            elif self.opcao == 17:
                print(self.opera.exercicio10())

            elif self.opcao == 18:
                print(self.opera.exercicio11())

            elif self.opcao == 19:
                print(self.opera.exercicio12())

            elif self.opcao == 20:
                print(self.opera.exercicio13())

            elif self.opcao == 21:
                print(self.opera.exercicio14())

            elif self.opcao == 22: # Não feito
                print(self.opera.exercicio15())

            elif self.opcao == 23:
                print(self.opera.exercicio16())

            elif self.opcao == 24:
                print(self.opera.exercicio17())

            elif self.opcao == 25:
                print(self.opera.exercicio18())

            elif self.opcao == 26:
                print(self.opera.exercicio19())

            elif self.opcao == 27:
                print(self.opera.exercicio20())
