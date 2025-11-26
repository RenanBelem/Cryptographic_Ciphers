tabelaDeConversao = {
    "A": "11000",
    "B": "10011",
    "C": "01110",
    "D": "10010",
    "E": "10000",
    "F": "10110",
    "G": "01011",
    "H": "00101",
    "I": "01100",
    "J": "11010",
    "K": "11110",
    "L": "01001",
    "M": "00111",
    "N": "00110",
    "O": "00011",
    "P": "01101",
    "Q": "11101",
    "R": "01010",
    "S": "10100",
    "T": "00001",
    "U": "11100",
    "V": "01111",
    "W": "11001",
    "X": "10111",
    "Y": "10101",
    "Z": "10001",
    "9": "00100",
    "8": "11111",
    "+": "11011",
    "4": "01000",
    "3": "00010",
    "/": "00000"
}

tabelaDeConversaoInversa = {
    "11000": "A",
    "10011": "B",
    "01110": "C",
    "10010": "D",
    "10000": "E",
    "10110": "F",
    "01011": "G",
    "00101": "H",
    "01100": "I",
    "11010": "J",
    "11110": "K",
    "01001": "L",
    "00111": "M",
    "00110": "N",
    "00011": "O",
    "01101": "P",
    "11101": "Q",
    "01010": "R",
    "10100": "S",
    "00001": "T",
    "11100": "U",
    "01111": "V",
    "11001": "W",
    "10111": "X",
    "10101": "Y",
    "10001": "Z",
    "00100": "9",
    "11111": "8",
    "11011": "+",
    "01000": "4",
    "00010": "3",
    "00000": "/"
}


def criptografa():
    # pegar texto para criptografar
    texto = input("\n Insira o texto que você deseja criptografar: ").upper()

    # utilizar a chave KROM para criptografia
    chave = ["K", "R", "O", "M"]

    # criptografar
    textoCriptografado = ""
    chaveIndex = 0
    for caracter in texto:

        if chaveIndex >= len(chave):
            chaveIndex = 0

        if caracter in tabelaDeConversao:
            caracterDaTabela = tabelaDeConversao[caracter]
            chaveDaTabela = tabelaDeConversao[chave[chaveIndex]]

            caracterFinalEmBinario = ""
            for index in range(5):
                if (caracterDaTabela[index] == chaveDaTabela[index]):
                    caracterFinalEmBinario += "0"
                else:
                    caracterFinalEmBinario += "1"

            caracter = tabelaDeConversaoInversa[caracterFinalEmBinario]

        textoCriptografado += caracter
        chaveIndex += 1

    print("=========================================")
    print("Texto criptografado: " + textoCriptografado)


def descriptografa():
    # pegar texto para descriptografar
    texto = input("\n Insira o texto que você deseja descriptografar: ").upper()

    # utilizar a chave KROM para descriptografia
    chave = ["K", "R", "O", "M"]

    # descriptografar
    textoDescriptografado = ""
    chaveIndex = 0
    for caracter in texto:

        if chaveIndex >= len(chave):
            chaveIndex = 0

        if caracter in tabelaDeConversao:
            caracterDaTabela = tabelaDeConversao[caracter]
            chaveDaTabela = tabelaDeConversao[chave[chaveIndex]]

            caracterFinalEmBinario = ""
            for index in range(5):
                if (caracterDaTabela[index] == chaveDaTabela[index]):
                    caracterFinalEmBinario += "0"
                else:
                    caracterFinalEmBinario += "1"

            caracter = tabelaDeConversaoInversa[caracterFinalEmBinario]

        textoDescriptografado += caracter
        chaveIndex += 1

    print("=========================================")
    print("Texto descriptografado: " + textoDescriptografado)