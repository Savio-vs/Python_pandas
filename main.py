from tkinter import *
from tkinter import ttk
import tkinter as tk
def janela2():
    janela = Tk()
    janela.title("Cotação Atual de Moedas")
    texto = Label(janela, text="iniciando algo")
    texto.grid(column=0, row=0, padx=10, pady=10)

    # botao = Button(janela, text="Buscar cotações", command=pegar_cotacoes)
    # botao.grid(column=0, row=1, padx=10, pady=10)

    # texto_resposta = Label(janela, text="")
    # texto_resposta.grid(column=0, row=2, padx=10, pady=10)


    janela.mainloop()


