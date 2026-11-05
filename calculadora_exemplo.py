import tkinter as tk #importa o tkinter com o alias tk (apelido)

#esta função será executada quando o usuário clicar no botão somar
def somar():
    #.get() lê o conteúdo quando o usuário clicar no botão somar
    # float() converte esse texto em número
    n1 = float(entrada1.get())
    n2 = float(entrada2.get())
    
    resultado = n1 + n2
    
    #altera o texto do label para mostrar a soma na janela
    lbl_resultado.config(text=f"Resultado: {resultado}")
    
#cria a janela principal
janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("350x250") # largura x altura, em pixels

#cria o texto e a caixa de entrada do primeiro número
lbl_numero1 = tk.Label(janela, text="Primeiro número:")
lbl_numero1.pack() #posiciona o componente na janela

entrada1 = tk.Entry(janela)
entrada1.pack()

#cria o texto e a caixa de entrada do segundo número
lbl_numero2 = tk.Label(janela, text="Segundo número:")
lbl_numero2.pack()

entrada2 = tk.Entry(janela)
entrada2.pack()

#cria botão e associa o clique à função somar
botao_somar = tk.Button(
    janela,
    text="Somar",
    command=somar #sem (): a função será chamada somente no clique
)
botao_somar.pack(pady=15) #adiciona espaço vertical ao redor do botão

#cria o espaço onde o resultado será exibido
lbl_resultado = tk.Label(janela,text="Resultado:")
lbl_resultado.pack()

#mantém a janela aberta e aguardando as ações do usuário
janela.mainloop()







