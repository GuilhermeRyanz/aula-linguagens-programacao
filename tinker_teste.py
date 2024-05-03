from tkinter import *

contador = 0

raiz = Tk()
raiz.title("Calanguinho")
raiz.geometry("350x200")
quadro = Frame(raiz)
texto = Label(quadro, text=f"Contador: {str(contador)}")
texto.pack()

def soma():
    global contador
    contador = contador + 1
    texto["text"] =f"Contaodor: {contador}"

botao = Button(quadro, text="+1", command=soma)
botao.pack()
quadro.pack(expand=True)
raiz.mainloop()
