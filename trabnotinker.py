import tkinter as tk
from tkinter import messagebox
from verificar_alunso_tinker import nova_entrada, verificar_porcentagem_alunos, verificacao_personalisada

def entrada_dados(entry_manha, entry_tarde, entry_noite, entry_data,janela):
    try:
        turno_manha = int(entry_manha.get())
        turno_tarde = int(entry_tarde.get())
        turno_noite = int(entry_noite.get())
        date = entry_data.get()

        nova_entrada(turno_manha, turno_tarde, turno_noite, date)

        messagebox.showinfo("Sucesso", "Dados salvos com sucesso!")

        janela.destroy()

    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida! Certifique-se de fornecer números inteiros.")

def janela_entrada_dados():
    janela = tk.Tk()
    janela.title("Cadastro e Verificação de Frequência")

    label_manha = tk.Label(janela, text="Alunos no turno da manhã:")
    label_manha.pack()
    entry_manha = tk.Entry(janela)
    entry_manha.pack()

    label_tarde = tk.Label(janela, text="Alunos no turno da tarde:")
    label_tarde.pack()
    entry_tarde = tk.Entry(janela)
    entry_tarde.pack()

    label_noite = tk.Label(janela, text="Alunos no turno da noite:")
    label_noite.pack()
    entry_noite = tk.Entry(janela)
    entry_noite.pack()

    label_data = tk.Label(janela, text="Data (DD/MM/AAAA):")
    label_data.pack()
    entry_data = tk.Entry(janela)
    entry_data.pack()

    botao_salvar = tk.Button(janela, text="Salvar", command=lambda: entrada_dados(entry_manha, entry_tarde, entry_noite, entry_data,janela))
    botao_salvar.pack(pady=5)

def janela_principal():
    raiz = tk.Tk()
    raiz.title("Menu academia")
    raiz.geometry("350x200")
    quadro = tk.Frame(raiz)
    texto = tk.Label(quadro, text=f"Escolha a funcao que deseja executae: ")
    texto.pack()
    botao = tk.Button(quadro, text="adicionar novos dados ", command=janela_entrada_dados)
    botao.pack()
    quadro.pack(expand=True)
    raiz.mainloop()

janela_principal()