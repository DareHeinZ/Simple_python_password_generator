#=============================================================|
#      |Created By Gabriel Melo in 2021, jun 22|              |
#      |Criado com o intuito de ajudar outros DEV|            |
# ============================================================|

# ------------------------ IMPORTS ----------------------------
from tkinter import *
import generator_functions as gf

# --------------------- TK MAIN LOOP --------------------------
root = Tk()
gf.drawWindow(root)
gf.drawFrames(root)
gf.drawRadioButtons()
gf.drawButtons(root)
root.mainloop()