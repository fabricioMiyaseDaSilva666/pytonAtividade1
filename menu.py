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
              '\n27. exercicio20' +
              '\n28. part2exercicio1' +
              '\n29. part2exercicio2' +
              '\n30. part2exercicio3' +
              '\n31. part2exercicio4' +
              '\n32. part2exercicio5' +
              '\n33. part2exercicio6' +
              '\n34. part2exercicio7' +
              '\n35. part2exercicio8' +
              '\n36. part2exercicio9' +
              '\n37. part2exercicio10' +
              '\n38. part2exercicio11' +
              '\n39. part2exercicio12' +
              '\n40. part2exercicio13' +
              '\n41. part2exercicio14' +
              '\n42. part2exercicio15' +
              '\n43. part2exercicio16' +
              '\n44. part2exercicio17' +
              '\n45. part2exercicio18' +
              '\n46. part2exercicio19' +
              '\n47. part2exercicio20')

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

            elif self.opcao == 28:
                print(self.opera.part2exercicio1())

            elif self.opcao == 29:
                print(self.opera.part2exercicio2())

            elif self.opcao == 30:
                print(self.opera.part2exercicio3())

            elif self.opcao == 31:
                print(self.opera.part2exercicio4())

            elif self.opcao == 32: # Não está certo
                print(self.opera.part2exercicio5())

            elif self.opcao == 33:
                print(self.opera.part2exercicio6())

            elif self.opcao == 34:
                print(self.opera.part2exercicio7())

            elif self.opcao == 35:
                print(self.opera.part2exercicio8())

            elif self.opcao == 36:
                print(self.opera.part2exercicio9())

            elif self.opcao == 37:
                print(self.opera.part2exercicio10())

            elif self.opcao == 38:
                print(self.opera.part2exercicio11())

            elif self.opcao == 39:
                print(self.opera.part2exercicio12())

            elif self.opcao == 40:
                print(self.opera.part2exercicio13())

            elif self.opcao == 41:
                print(self.opera.part2exercicio14())

            elif self.opcao == 42:
                print(self.opera.part2exercicio15())

            elif self.opcao == 43:
                print(self.opera.part2exercicio16())

            elif self.opcao == 44:
                print(self.opera.part2exercicio17())

            elif self.opcao == 45:
                print(self.opera.part2exercicio18())

            elif self.opcao == 46:
                print(self.opera.part2exercicio19())

            elif self.opcao == 47:
                print(self.opera.part2exercicio20())
