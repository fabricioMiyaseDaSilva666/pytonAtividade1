from menu import Menu # Conectando a main a classe
# Executa as transações entre classes
#  Se o from... estiver com a cor igual a de um comentário, é porque ele não ta sendo usado ou chamado
if __name__ == '__main__':# O if __name__ == '__main__' no inicio, vai ser impostante pra mostra as coisas pro usuario
    men = Menu()
    men.operacao()