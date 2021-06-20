from tkinter import *
from gerador_senha import *

root = Tk()
numeros = IntVar()
letras = IntVar()
escolha = 0
msg_numeral = "Digite a quantidade de números que deseja na senha"
msg_letra = "Digite a quantidade de letras que deseja na senha"
msg_carac = "Digite a quantidade de caracteres que deseja na senha"

def get_value(leitura_num, leitura_letra, leitura_carac):
    """
    Pega os 3 valores, que são decididos pelo usuario
    Caso o usuario queria somente uma senha simples
    Os outros dois valores recebem 0
    Dessa forma eu fiz as outras opções
    """
    qnt_de_num = leitura_num
    qnt_de_letras = leitura_letra
    qnt_carac_espc = leitura_carac
    eu = gerador_de_senhas(qnt_de_num=qnt_de_num, qnt_de_letras=qnt_de_letras, qnt_carac_espc=qnt_carac_espc)
    texto_tk = Entry(frameGerarSenhas, width=30)
    texto_tk.insert(0, f"{eu}")
    texto_tk.grid(row=7, column=0)

def escolha_num(value):
    """
    Essa função, faz a verificação do Radio Button, para
    Entender em qual posição o usuario escolheu, e a partir
    Dela deicidir qual será o tipo de senha de seu desejo
    E fazendo ainda mais modalidades.
    """
    if value == 1: # Para caso o usuario escolha uma senha simples
        for widget in frameGerarSenhas.winfo_children():
            widget.destroy()
        texto_numeral = Label(frameGerarSenhas, text=msg_numeral)
        texto_numeral.grid(row=0, column=0)
        entrada_num = Entry(frameGerarSenhas)
        entrada_num.grid(row=1, column=0)
        generateButton = Button(frameGerarSenhas, text="Gerar Senha", command=lambda: get_value(entrada_num.get(), 0, 0))
        generateButton.grid(row=2, column=0)
        
    if value == 2: # Senha de número com letras
        for widget in frameGerarSenhas.winfo_children():
            widget.destroy()
        texto_numeral = Label(frameGerarSenhas, text=msg_numeral)
        texto_numeral.grid(row=0, column=0)
        entrada_num = Entry(frameGerarSenhas)
        entrada_num.grid(row=1, column=0)
        texto_letra = Label(frameGerarSenhas, text=msg_letra)
        texto_letra.grid(row=2, column=0)
        entrada_letra = Entry(frameGerarSenhas)
        entrada_letra.grid(row=3, column=0)
        generateButton = Button(frameGerarSenhas, text="Gerar Senha", command=lambda: get_value(entrada_num.get(), entrada_letra.get(), 0))
        generateButton.grid(row=4, column=0)
 
    if value == 3:# Senha de número com caracteres especiais
        for widget in frameGerarSenhas.winfo_children():
            widget.destroy()
        texto_numeral = Label(frameGerarSenhas, text=msg_numeral)
        texto_numeral.grid(row=0, column=0)
        entrada_num = Entry(frameGerarSenhas)
        entrada_num.grid(row=1, column=0)
        texto_carac = Label(frameGerarSenhas, text=msg_carac)
        texto_carac.grid(row=2, column=0)
        entrada_carac = Entry(frameGerarSenhas)
        entrada_carac.grid(row=3, column=0)
        create_button = Button(frameGerarSenhas, text="Gerar Senha", command=lambda: get_value(entrada_num.get(), 0, entrada_carac.get()))
        create_button.grid(row=4, column=0)
    
    if value == 4:# Senha completa, com todos os outros
        for widget in frameGerarSenhas.winfo_children():
            widget.destroy()
        texto_numeral = Label(frameGerarSenhas, text=msg_numeral)
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

# Aqui funciona o root, onde está toda a tela principal, e os frames
root.geometry("800x600+0+0")
root.title("Gerador De Senhas")

myLabel = Label(root, text="GERADOR DE SENHAS")
myLabel.pack()

# Frames
frame_escolhas = LabelFrame(root, text="Escolhas", padx=10, pady=20)
frame_escolhas.pack()
frameGerarSenhas = LabelFrame(root, text="Gerar Senha", pady=40, padx=40)
frameGerarSenhas.pack()

# Radio Buttons
botao_so_num = Radiobutton(frame_escolhas, text="012345", variable=numeros, value=1, command=lambda: escolha_num(numeros.get()))
botao_so_num.grid(row=0, column=0)
botao_letra = Radiobutton(frame_escolhas, text="123ABC", variable=numeros, value=2, command=lambda: escolha_num(numeros.get()))
botao_letra.grid(row=0, column=1)
botao_carac_espc = Radiobutton(frame_escolhas, text="123$#@", variable=numeros, value=3, command=lambda: escolha_num(numeros.get()))
botao_carac_espc.grid(row=0, column=2)
botao_compl = Radiobutton(frame_escolhas, text="123ABC!@#", variable=numeros, value=4, command=lambda: escolha_num(numeros.get()))
botao_compl.grid(row=0, column=3)
botaoSair = Button(root, text="EXIT", command=root.quit)
botaoSair.pack()

root.mainloop()