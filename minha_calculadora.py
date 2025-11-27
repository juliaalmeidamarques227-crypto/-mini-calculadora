import tkinter as tk

# Função para adicionar texto na entrada
def clicar(botao):
    atual = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(0, atual + botao)

# Função para calcular o resultado
def calcular():
    try:
        expressao = entrada.get()
        resultado = eval(expressao)
        entrada.delete(0, tk.END)
        entrada.insert(0, str(resultado))
    except:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Erro")

# Função para limpar a entrada
def limpar():
    entrada.delete(0, tk.END)

# Criando a janela
janela = tk.Tk()
janela.title("Calculadora Simples")
janela.geometry("300x380")

# Caixa de entrada
entrada = tk.Entry(janela, width=20, font=("Arial", 20), justify="right")
entrada.pack(pady=10)

# Frame para os botões
frame = tk.Frame(janela)
frame.pack()

# Lista de botões
botoes = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

linha = 0
coluna = 0

for botao in botoes:
    if botao == "=":
        cmd = calcular
    else:
        cmd = lambda x=botao: clicar(x)

    tk.Button(
        frame,
        text=botao,
        width=5,
        height=2,
        font=("Arial", 14),
        command=cmd
    ).grid(row=linha, column=coluna, padx=5, pady=5)

    coluna += 1
    if coluna > 3:
        coluna = 0
        linha += 1

# Botão de limpar
tk.Button(
    janela, text="C", width=20, height=2, font=("Arial", 14), command=limpar
).pack(pady=5)

# Executando a janela
janela.mainloop()
