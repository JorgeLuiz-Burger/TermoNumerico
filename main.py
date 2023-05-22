"""
Termo numérico -
    Jogo para adivinhar um número de X caracteres corretamente cada número em sua posição
"""

# Inclusão de bibliotecas necessárias
import random
import os
import colorama

# Dicionário de símbolos usados
correctPosition = 'C'
WrongPosition = 'P'
NonPresent = 'N'
testMore = '?'

# Informações importantes para o jogo
maxIndex = 5
guessNumber = []


def installNecessaryModules():
    os.system("pip install colorama >NUL")


# Criando o número randomicamente
def createNumber():
    global guessNumber

    # Iniciando zerado
    guessNumber = []

    # Gerando um número aleatório de 1 algarismo para cada dígito do número
    for i in range(0, maxIndex):
        guessNumber.append(random.randint(0, 9))

    # print(guessNumber)


# Validando os dados recebidos do usuário
def testNumber(value):
    global guessNumber
    global correctPosition
    global WrongPosition
    global NonPresent
    global testMore
    results = []

    repeatGuess = {
        '0': 0,
        '1': 0,
        '2': 0,
        '3': 0,
        '4': 0,
        '5': 0,
        '6': 0,
        '7': 0,
        '8': 0,
        '9': 0,
    }

    # Primeiramente encontrando os valores corretos
    for index in range(0, maxIndex):
        # Posição correta
        if (int(value[index]) == guessNumber[index]):
            results.append(correctPosition)
            # Acrescendo no dicionário de tentativas
            repeatGuess[value[index]] += 1

        else:
            results.append(testMore)

    # Validando existência dos demais
    for index in range(0, maxIndex):
        # Somente testar os não validados
        if results[index] == testMore:
            # Número não encontrado
            if int(value[index]) not in guessNumber:
                results[index] = NonPresent

            else:
                counterGuess = guessNumber.count(int(value[index]))

                # Se o número encontrado tiver repetições irá marcar apenas os primeiros aparecimentos como Presente
                if (repeatGuess[value[index]] <= counterGuess - 1):
                    results[index] = WrongPosition
                    repeatGuess[value[index]] += 1

                # Não encontrado no vetor
                else:
                    results[index] = NonPresent

    # Possui caracter errado?
    error = ((NonPresent in results) or (WrongPosition in results))

    # Mostrando o resultado na tela
    print("--> ", end='')
    for index in range(0, maxIndex):
        if results[index] == correctPosition:
            print(colorama.Fore.GREEN + value[index] + ' ', end='')

        elif results[index] == WrongPosition:
            print(colorama.Fore.YELLOW + value[index] + ' ', end='')

        elif results[index] == NonPresent:
            print(colorama.Fore.RED + value[index] + ' ', end='')
    print(" \n")

    # Retornando o erro ou acerto para a aplicação
    return error


def getUserTry():
    numberOk = False
    maxLifes = maxIndex + 2

    while(not numberOk):
        # Solicitando o número ao jogador
        numberTry = input(f"Você possui {maxLifes} tentativas para adivinhar o número de {maxIndex} caracteres.")

        # Número de caracteres recebidos incorreto
        if len(numberTry) != maxIndex:
            print(f"\t Tamanho total do número não aceito, favor digitar {maxIndex} caracteres.\n")

        # Algum caracter recebido está incorreto
        elif not numberTry.isnumeric():
            print("\t Encontrado um texto, favor colocar apenas caracteres numéricos.\n")

        # Validando tentativa
        else:
            # Possui algum erro
            if testNumber(numberTry):
                # Ainda existem tentativas válidas
                if (maxLifes > 1):
                    maxLifes -= 1

                # Não há mais tentativas
                else:
                    print("-"*(10 + (2 * maxIndex) + len("O número era [ ")))
                    print(f"\t/*/* FIM DE JOGO */*/")
                    txtError = "\tO número era [ "
                    for index in range(0, maxIndex):
                        txtError += str(guessNumber[index]) + " "
                    txtError += "]"
                    print(txtError)
                    print("-"*(10 + (2 * maxIndex) + len("O número era [ ")))
                    print("\n")

                    # Encerrando o loop
                    numberOk = True

            # Número adivinhado corretamente
            else:
                print("-"*(10 + len("/*/* FIM DE JOGO */*/")))
                print(f"\t /*/* FIM DE JOGO */*/")
                print("\t Parabéns você venceu.")
                print("-"*(10 + len("/*/* FIM DE JOGO */*/")))
                print("\n")

                # Encerrando o loop
                numberOk = True


if __name__ == '__main__':

    # Validando se é necessário instalar os módulos extras
    if (0) or (os.path.exists('main.exe')):
        installNecessaryModules()

    # Permitindo a alteração de cores no terminal
    colorama.init(autoreset=True)

    # Jogo
    retry = 1
    while (retry):
        # Criando o número a ser adivinhado
        createNumber()

        # Jogando os números no terminal
        getUserTry()

        # Finalizou o jogo
        print("_" * len("Pressione 's' para jogar novamente."))
        txt = input("Pressione 's' para jogar novamente.")
        if (txt.lower() != 's'):
            retry = 0
        else:
            os.system("cls")

"""
Passo a passo para gravação do executável

1. Ir na pasta do projeto atual
2. Digitar CMD na barra de endereço
3. Utilizar o comando
    pyinstaller --onefile main.py
"""

# End of file
