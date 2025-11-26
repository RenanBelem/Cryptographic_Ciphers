# Cifras Criptográficas em Python

Este projeto implementa duas cifras criptográficas clássicas: a **Cifra de César** (Cifra por Substituição Simples) e uma variação da **Cifra de Vigenère** usando a chave fixa "KROM" (Cifra de Fluxo ou *Stream Cipher*).

O programa principal (`main.py`) atua como interface para o usuário escolher entre criptografar ou descriptografar usando uma das duas cifras disponíveis.

-----

## 📂 Estrutura de Arquivos

O projeto é composto por três arquivos Python:

1.  **`main.py`**: O arquivo principal que gerencia a interface do usuário e coordena a execução das cifras.
2.  **`cifraCesar.py`**: Contém as funções para criptografia e descriptografia da Cifra de César.
3.  **`cifraKrom.py`**: Contém as funções para criptografia e descriptografia da Cifra KROM, baseada em um esquema de **XOR binário** com a chave fixa "KROM".

-----

## 🚀 Como Executar

1.  Certifique-se de ter o **Python** instalado.

2.  Salve os três arquivos (`main.py`, `cifraCesar.py`, `cifraKrom.py`) no mesmo diretório.

3.  Execute o arquivo principal a partir do seu terminal:

    ```bash
    python main.py
    ```

4.  Siga as instruções na tela para selecionar a operação (Criptografar/Descriptografar) e a cifra (César/KROM).

-----

## 🔐 Cifra de César (`cifraCesar.py`)

Esta cifra utiliza uma substituição simples baseada em um **deslocamento fixo** no alfabeto.

  * **Entrada Necessária:** O usuário deve informar a **letra inicial** que será usada para construir a cifra (o deslocamento). Por exemplo, se a letra inicial for 'D', a letra 'A' será mapeada para 'D', 'B' para 'E', e assim por diante.
  * **Funcionalidades:**
      * `criptografa()`: Recebe um texto e uma letra inicial para produzir a versão criptografada.
      * `descriptografa()`: Recebe um texto cifrado e a **mesma letra inicial** para reverter a operação e obter o texto original.

-----

## 🛡️ Cifra KROM (`cifraKrom.py`)

Esta cifra é uma implementação de um *stream cipher* (cifra de fluxo) que utiliza uma chave repetida (`KROM`) e a operação **XOR** em representações binárias de 5 bits para cada caractere.

  * **Mapeamento:** Os caracteres válidos (letras maiúsculas de A-Z, números 9, 8, 4, 3, e os símbolos + e /) são mapeados para sequências binárias de 5 bits (00000 a 11111) usando as tabelas `tabelaDeConversao` e `tabelaDeConversaoInversa`.

  * **Operação:** A criptografia/descriptografia é realizada bit a bit utilizando a operação lógica **XOR** (Ou Exclusivo) entre a representação binária do caractere do texto e a representação binária do caractere da chave `KROM`.

      * Lógica XOR: $0 \oplus 0 = 0$, $1 \oplus 1 = 0$, $1 \oplus 0 = 1$, $0 \oplus 1 = 1$.

  * **Propriedade Reversível:** A operação XOR é o seu próprio inverso, o que significa que as funções de criptografia e descriptografia são idênticas.

    $$(Texto \oplus Chave) \oplus Chave = Texto$$

  * **Funcionalidades:**

      * `criptografa()`: Recebe um texto e aplica a cifra KROM com a chave fixa.
      * `descriptografa()`: Recebe um texto cifrado e aplica a **mesma lógica** para obter o texto original.

-----

## ⚙️ Arquivo Principal (`main.py`)

O arquivo principal orquestra o fluxo do programa:

  * Importa as funções dos módulos `cifraCesar` e `cifraKrom`.
  * Apresenta um menu de interação em um *loop* contínuo.
  * Pede ao usuário para selecionar:
    1.  A **Operação** (`1` para Criptografar / `2` para Descriptografar).
    2.  O **Tipo de Criptografia** (`1` para César / `2` para KROM).
  * Chama a função apropriada com base nas escolhas do usuário.

-----
