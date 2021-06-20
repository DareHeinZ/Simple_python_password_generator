from random import randint


letras = ["a","A","b","B","c","C","d","D","e","E","f","F","g","G","h","H","i",
          "I","j","J","k","K","l","L","m","M","n","N","o","O","p","P","q","Q",
          "r","R","s","S","t","T","u","U","v","V","w","W","x","x","y","Y","z",
          "Z"
         ]

caracteres_especiais = ["!","@","#","$","%","&","*"]

def gerador_de_senhas(qnt_de_num, qnt_de_letras, qnt_carac_espc):
    """
    Função para gerar senhas com a quantidade desejada de numeroes e caracteres
    """
    
    # VARIAVEIS
    senha = []
    vezes_numeros = 0
    password = ""

    soma_de_qnt = int(qnt_de_num) + int(qnt_de_letras) + int(qnt_carac_espc)
    
    # Laço para criar a senha parte NUMERAL
    while True:
        senha.append(randint(0,9))
        vezes_numeros += 1
        if vezes_numeros == int(qnt_de_num):
            break

    # Laço para os caracteres especiais
    for m in range(0, int(qnt_carac_espc)):
        senha.insert(randint(0, soma_de_qnt), caracteres_especiais[randint(0, 6)])


    # Laço para criara a parte de caracteres e adiconar em senha
    for m in range(0, int(qnt_de_letras)):
        senha.insert(randint(0, soma_de_qnt), letras[randint(0, 51)])

    # Laço para abrir a lista e deixar mais légivel a senha em formato de STRING
    for pasword in senha:
        password += str(pasword)
    
    # Retorna a senha pronta
    return str(password)
