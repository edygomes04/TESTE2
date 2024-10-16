import tkinter as tk
from tkinter import messagebox

def mostrar_mensagem():
    messagebox.showinfo("Informação", "Botão Clicado!")

janela = tk.Tk()
janela.title("Interface Gráfica com Tkinter")
janela.geometry("300x200")
rotulo = tk.Label(janela, text="Bem-vindo à sua primeira interface gráfica!")
rotulo.pack(pady=20)
botao = tk.Button(janela, text="Clique Aqui", command=mostrar_mensagem)
botao.pack(pady=20)
janela.mainloop()