# Alunos: Lucas Cavalherie e Renan Belem

import cifraCesar
import cifraKrom

while (True):
    print("===================")
    print("(Re)Iniciando o Sistema")

    print("O que você deseja fazer? \n Criptografar - 1 \n Descriptografar - 2")
    operacao = input("\n Resposta: ")
    print("Qual criptografia você deseja utilizar?\n Cesar - 1 \n Krom - 2")
    tipo = input("\n Resposta: ")

    if (tipo == "1" and operacao == "1"):
        cifraCesar.criptografa()
    elif (tipo == "1" and operacao == "2"):
        cifraCesar.descriptografa()
    elif (tipo == "2" and operacao == "1"):
        cifraKrom.criptografa()
    elif (tipo == "2" and operacao == "2"):
        cifraKrom.descriptografa()
    else:
        print("VOCÊ DIGITOU ERRADO KELLY!")
