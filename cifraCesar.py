import string

def criptografa():
    # pegar texto para criptografar
    texto = input("\n Insira o texto que você deseja criptografar: ").upper()

    # pegar letra inicial
    letraInicial = input(
        "\n Por qual letra você deseja começar a Cifra de Cesar?: ").upper()

    # alfabeto
    alfabeto = list(string.ascii_uppercase)

    # montar cifra de cesar
    cifra = alfabeto[alfabeto.index(letraInicial):] + alfabeto[:alfabeto.index(
        letraInicial)]

    # criptografar
    textoCriptografado = ""
    for caracter in texto:
      if caracter in alfabeto:
        caracter = cifra[alfabeto.index(caracter)]
      textoCriptografado += caracter

    print("=========================================")
    print("Texto criptografado: "+ textoCriptografado)



def descriptografa():
    # pegar texto para descriptografar
    texto = input("\n Insira o texto que você deseja descriptografar: ").upper()

    # pegar letra inicial
    letraInicial = input(
        "\n Por qual letra você deseja começar a Cifra de Cesar?: ").upper()

    # alfabeto
    alfabeto = list(string.ascii_uppercase)

    # montar cifra de cesar
    cifra = alfabeto[alfabeto.index(letraInicial):] + alfabeto[:alfabeto.index(
        letraInicial)]

    # descriptografar
    textoDescriptografado = ""
    for caracter in texto:
      if caracter in cifra:
        caracter = alfabeto[cifra.index(caracter)]
      textoDescriptografado += caracter

    print("=========================================")
    print("Texto descriptografado: "+ textoDescriptografado)
