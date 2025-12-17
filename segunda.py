import tkinter as tk


def abrir_segunda_janela():
    segunda_janela = tk.Toplevel()
    segunda_janela.title("Segundda janela")
    segunda_janela.config(bg="#352066")

    #Tamanho 
    largura_janela = 300
    altura_janela = 200

    #dimensões da tela do monitor
    largura_tela = segunda_janela.winfo_screenmmwidth()
    altura_tela = segunda_janela.winfo_screenmmwidth()
    
    #Calcular as cordenadas p/ centralizar a janela 2
    x = (largura_tela - largura_janela) // 2
    y = (altura_tela - altura_janela) // 2

    #Definir a geometria da janela 2
    segunda_janela.geometry(f"{largura_janela} x {altura_janela} + {x} + {y}")

#Criar janela principal 

janela_principal = tk.Tk()
janela_principal.title("Janela Principal")
janela_principal.geometry("600x500")
#Configurar evento de click na jenela principal
janela_principal.bind("<Button-1>", lambda event: abrir_segunda_janela()) #Botão esquerdo do mouse p/ bind |Captura o click e executa o evento lambda
#Exibir a janela
janela_principal.mainloop()