#=============================================================|
#      |Created By Gabriel Melo in 2021, jun 22|              |
#      |Criado com o intuito de ajudar outros DEV|            |
# ============================================================|

# --------------------- IMPORT ---------------------
from random import randint

# --------------------- FUNCTION -------------------

def gerador_de_senhas(qntNum, qntLetters, qntCarac):
    """
    Função para gerar senhas com a quantidade desejada/
    Function to generate a password.
    """
    # Variaveis/Variables
    letras = ["a","A","b","B","c","C","d","D","e","E","f","F","g","G","h","H","i",
          "I","j","J","k","K","l","L","m","M","n","N","o","O","p","P","q","Q",
          "r","R","s","S","t","T","u","U","v","V","w","W","x","x","y","Y","z",
          "Z"] # 51 Letras/Letters
    caracteres_especiais = ["!","@","#","$","%","&","*"] # 7 Caracteres especiais/Special Caracteres
    senha = []
    password = ""
    # Tratar possivel erro ao digitar
    try:
        soma_de_qnt = int(qntNum) + int(qntLetters) + int(qntCarac)
    except ValueError:
        return "Somente Números/Just Numbers"

    # Laço para criar a senha parte NUMERAL
    # Loop for numbers in Password
    for numbersgm in range(0, int(qntNum)):
        senha.append(randint(0,9))

    # Laço para criara a parte de caracteres e adiconar em senha
    # Loop for letters, and insert on senha
    for lettersgm in range(0, int(qntLetters)):
        senha.insert(randint(0, soma_de_qnt), letras[randint(0, 51)])

    # Laço para os caracteres especiais
    # Loop for special caracteres
    for caracteresgm in range(0, int(qntCarac)):
        senha.insert(randint(0, soma_de_qnt), caracteres_especiais[randint(0, 6)])

    # Laço para abrir a lista e deixar mais légivel a senha em formato de STRING
    # Open the list and turn a string.
    for pasword in senha:
        password += str(pasword)
    
    return str(password)
