#=============================================================|
#      |Created By Gabriel Melo in 2021, jun 22|              |
#      |Criado com o intuito de ajudar outros DEV|
# ============================================================|

# ----------------------- IMPORTS ---------------------------
from tkinter import *
from password_generator import *

# ---------------------- FUNCTIONS ---------------------------
def get_value(readNum, readLetra, readCarac):
    """
    Pega os 3 valores, que são decididos pelo usuario.
    Take the 3 values from user.
    """
    senhaGerada = gerador_de_senhas(qntNum=readNum, qntLetters=readLetra, qntCarac=readCarac)
    texto_tk = Entry(frameGerarSenhas, width=30)
    texto_tk.insert(0, f"{senhaGerada}")
    texto_tk.grid(row=7, column=0)

def choiceNum(value):
    radioLocation = caract.get()
    msg_number = "Digite a quantidade de números que deseja na senha"
    msg_letra = "Digite a quantidade de letras que deseja na senha"
    msg_carac = "Digite a quantidade de caracteres que deseja na senha"
    """
    Essa função, faz a verificação do Radio Button, para
    Entender em qual posição o usuario escolheu, e a partir
    Dela deicidir qual será o tipo de senha de seu desejo
    E fazendo ainda mais modalidades.
    """
    # Loop to clean the frame
    for widget in frameGerarSenhas.winfo_children():
            widget.destroy()
    if radioLocation == 1:#gm
        # Verify the Radio Button, and choice a Password
        if value == 1:
            generateButton = Button(frameGerarSenhas, text="Gerar Senha", command=lambda: get_value(10, 0, 0))
            generateButton.grid(row=3, column=0)
        if value == 2:
            generateButton = Button(frameGerarSenhas, text="Gerar Senha", command=lambda: get_value(7, 3, 0))
            generateButton.grid(row=3, column=0)
        if value == 3:
            generateButton = Button(frameGerarSenhas, text="Gerar Senha", command=lambda: get_value(7, 0, 3))
            generateButton.grid(row=3, column=0)
        if value == 4:
            generateButton = Button(frameGerarSenhas, text="Gerar Senha", command=lambda: get_value(5, 2, 3))
            generateButton.grid(row=3, column=0)

    if radioLocation == 2:
        if value == 1:
            texto_senha = Label(frameGerarSenhas, text="|Opção para gerar apenas senhas com números|")
            texto_senha.grid(row=0, column=0)
            texto_numeral = Label(frameGerarSenhas, text=msg_number)
            texto_numeral.grid(row=1, column=0)
            entrada_num = Entry(frameGerarSenhas)
            entrada_num.grid(row=2, column=0)
            generateButton = Button(frameGerarSenhas, text="Gerar Senha", command=lambda: get_value(entrada_num.get(), 0, 0))
            generateButton.grid(row=3, column=0)
        
        if value == 2:
            texto_numeral = Label(frameGerarSenhas, text=msg_number)
            texto_numeral.grid(row=0, column=0)
            entrada_num = Entry(frameGerarSenhas)
            entrada_num.grid(row=1, column=0)
            texto_letra = Label(frameGerarSenhas, text=msg_letra)
            texto_letra.grid(row=2, column=0)
            entrada_letra = Entry(frameGerarSenhas)
            entrada_letra.grid(row=3, column=0)
            generateButton = Button(frameGerarSenhas, text="Gerar Senha", command=lambda: get_value(entrada_num.get(), entrada_letra.get(), 0))
            generateButton.grid(row=4, column=0)
 
        if value == 3:
            texto_numeral = Label(frameGerarSenhas, text=msg_number)
            texto_numeral.grid(row=0, column=0)
            entrada_num = Entry(frameGerarSenhas)
            entrada_num.grid(row=1, column=0)
            texto_carac = Label(frameGerarSenhas, text=msg_carac)
            texto_carac.grid(row=2, column=0)
            entrada_carac = Entry(frameGerarSenhas)
            entrada_carac.grid(row=3, column=0)
            create_button = Button(frameGerarSenhas, text="Gerar Senha", command=lambda: get_value(entrada_num.get(), 0, entrada_carac.get()))
            create_button.grid(row=4, column=0)
    
        if value == 4:
            texto_numeral = Label(frameGerarSenhas, text=msg_number)
            texto_numeral.grid(row=0, column=0)
            entrada_num = Entry(frameGerarSenhas)
            entrada_num.grid(row=1, column=0)
            texto_letra = Label(frameGerarSenhas, text=msg_letra)
            texto_letra.grid(row=2, column=0)
            entrada_letra = Entry(frameGerarSenhas)
            entrada_letra.grid(row=3, column=0)
            texto_carac = Label(frameGerarSenhas, text=msg_carac)
            texto_carac.grid(row=4, column=0)
            entrada_carac = Entry(frameGerarSenhas)
            entrada_carac.grid(row=5, column=0)
            create_button = Button(frameGerarSenhas, text="Gerar Senha", command=lambda: get_value(entrada_num.get(), entrada_letra.get(), entrada_carac.get()))
            create_button.grid(row=6, column=0)

# ------------------------ DRAW TKINTER FUNCTIONS ---------------------------
def drawWindow(root):
    """Draw on Screen."""
    root.geometry("450x550+600+100")
    headLabel = Label(root, text="GERADOR DE SENHAS/PASSWORD GENERATOR")
    headLabel.pack()
    root.title("Gerador De Senhas")
    labelText = Label(root, text="Created by Gabriel Melo", relief=SUNKEN, anchor=E, bg="GREY", fg="BLUE")
    labelText.pack()
        
def drawFrames(root):
    """Draw Frames on Window."""
    global frameGerarSenhas, frame_options, frame_escolhas
    frame_options = LabelFrame(root, text="Opções", pady=10, padx=40)
    frame_escolhas = LabelFrame(root, text="Escolhas", padx=40, pady=20)
    frameGerarSenhas = LabelFrame(root, text="Gerar Senha", pady=40, padx=40)
    frame_options.pack()
    frame_escolhas.pack()
    frameGerarSenhas.pack()

def drawRadioButtons():#gm
    """Draw Radio Buttons on Window."""
    global caract
    caract = IntVar()
    Radiobutton(frame_options, text="Gerar Automáticamente", variable=caract, value=1).grid(row=0, column=0)
    Radiobutton(frame_options, text="Escolher Tamanho", variable=caract, value=2).grid(row=0, column=1)

def drawButtons(root):
    """Draw Buttons on Window."""
    buttonNumbers = Button(frame_escolhas, text="012345", command=lambda: choiceNum(1), borderwidth=3)
    botao_letra = Button(frame_escolhas, text="123ABC", command=lambda: choiceNum(2), borderwidth=3)
    botao_carac_espc = Button(frame_escolhas, text="123$#@", command=lambda: choiceNum(3), borderwidth=3)
    botao_compl = Button(frame_escolhas, text="123ABC!@#", command=lambda: choiceNum(4), borderwidth=3)
    buttonExit = Button(root, text="EXIT", command=root.quit, fg="RED")
    buttonExit.pack()
    buttonNumbers.grid(row=0, column=0)
    botao_letra.grid(row=0, column=1)
    botao_carac_espc.grid(row=0, column=2)
    botao_compl.grid(row=0, column=3)
