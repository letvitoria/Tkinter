import tkinter as tk

#Instanciar a janela
janela = tk.Tk()
janela.title("Primeiro app")
janela.geometry("500x400+20+20") # Largura x Altura + Posição X + Posição Y
#A janela aparece em uma distância de 20 pixels a partir do topo e 20 pixels a partir da esquerda da tela

#Criar e posicionar o label com a mensagem
mensagem = tk.Label(janela, text="Olá Mundo!")
mensagem.pack() #Gerenciador de geometria
#Mudando a cor de fundo 
janela.configure(bg="lightblue")
#Exibir a janela
janela.mainloop()