# importando tiknter

from tkinter import *
from tkinter import ttk
from turtle import color
from unittest import result

# cores

cor1 = "#0a0a0a" #preto
cor2 = "#ffffff" #branco
cor3 = "#c230bf" #roxo
cor4 = "#666566" #cinza
cor5 = "#b34273" #rosa

janela = Tk()
janela.title("Calculadora Danyels")
janela.geometry("261x318")
janela.config(bg=cor1)

frame_tela = Frame(janela, width=319, height=50, bg=cor4)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=319, height=268)
frame_corpo.grid(row=1, column=0)

# variavel todos valores

todos_valores = ''

# criando label

valor_texto = StringVar()

# criando funcao

def entrar_valores(event):

    global todos_valores

    todos_valores = todos_valores + str(event)
     
    # passando valor para tela
    valor_texto.set(todos_valores)

# funcao calculadora

def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))
    todos_valores = str(resultado)

# limpar tela

def limpar_tela():
    global todos_valores
    todos_valores =""
    valor_texto.set('')



app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=3, relief=FLAT, anchor='e', justify=RIGHT, font=('Ivy 20'), bg=cor3, fg=cor2)
app_label.place(x=0, y=-6)

# criando botoes

b_1 = Button(frame_corpo, command=limpar_tela, text='Clean', width=12, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)
b_2 = Button(frame_corpo, command= lambda:entrar_valores('%'), text='%', width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=126, y=0)
b_3 = Button(frame_corpo, command= lambda:entrar_valores('/'), text='/', width=6, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=190, y=0)

b_4 = Button(frame_corpo, command= lambda:entrar_valores('7'), text='7', width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=55)
b_5 = Button(frame_corpo, command= lambda:entrar_valores('8'), text='8', width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=63, y=55)
b_6 = Button(frame_corpo, command= lambda:entrar_valores('9'), text='9', width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=126, y=55)
b_7 = Button(frame_corpo, command= lambda:entrar_valores('*'), text='*', width=6, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=190, y=55)

b_8 = Button(frame_corpo, command= lambda:entrar_valores('4'), text='4', width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=110)
b_9 = Button(frame_corpo, command= lambda:entrar_valores('5'), text='5', width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=63, y=110)
b_10 = Button(frame_corpo, command= lambda:entrar_valores('6'), text='6', width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=126, y=110)
b_11 = Button(frame_corpo, command= lambda:entrar_valores('-'), text='-', width=6, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=190, y=110)

b_12 = Button(frame_corpo, command= lambda:entrar_valores('1'), text='1', width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=165)
b_13 = Button(frame_corpo, command= lambda:entrar_valores('2'), text='2', width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=63, y=165)
b_14 = Button(frame_corpo, command= lambda:entrar_valores('3'), text='3', width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=126, y=165)
b_15 = Button(frame_corpo, command= lambda:entrar_valores('+'), text='+', width=6, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=190, y=165)

b_16 = Button(frame_corpo, command= lambda:entrar_valores('0'), text='0', width=12, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=220)
b_17 = Button(frame_corpo, command= lambda:entrar_valores('.'), text='.', width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_17.place(x=126, y=220)
b_18 = Button(frame_corpo, command=calcular, text='=', width=6, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_18.place(x=190, y=220)

janela.mainloop()

