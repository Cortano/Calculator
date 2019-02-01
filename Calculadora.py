from Tkinter import *
from Funciones_matematicas import *


root = Tk()

root.title("Calculadora")

frame=Frame(root)
frame.pack()

operacion = ""
opc=0
resultado = 0

#-----------PANTALLA------------------

mostrando=StringVar()
operacionActual=StringVar()

pantalla=Entry(frame, textvariable=mostrando)
pantalla.grid(row=0, column=1,pady=10,padx=10,columnspan=3)
pantalla.config(justify="right")
pantalla.insert(0, "0")
pantalla2=Entry(frame, width=3, textvariable=operacionActual)
pantalla2.grid(row=0,column=4, pady=10, padx=10)
pantalla2.insert(0," ")

#------------EVENTOS--------------------
def Clear():
	global operacion,resultado,opc
	operacion = ""
	opc=0
	resultado=0
	mostrando.set("0")
	operacionActual.set("")

def codigoBoton(num):
	global operacion

	if(operacion!=""):
		mostrando.set(num)
		operacion=""
	else:
		mostrando.set(mostrando.get() + num)

def suma(num):
	global operacion, resultado,opc
	if (opc == 0):
		resultado = float(num)
	elif (opc == 1):
		resultado += float(num)
	else:
		elResultado()

	operacion = "+"
	opc = 1
	operacionActual.set(operacion)
	mostrando.set(resultado)

def resta(num):
	global operacion, resultado, opc
	if (resultado == 0 and opc == 0):
		resultado = float(num)
	elif(opc == 2):
		resultado -= float(num)
	else:
		elResultado()
	operacion = "-"
	opc = 2
	operacionActual.set(operacion)
	mostrando.set(resultado)

def multiplica(num):
	global operacion, resultado, opc
	
	if (resultado == 0 and opc == 0):
		resultado = float(num)
	elif (opc == 3):
		resultado *= float(num)
	else:
		elResultado()
	operacion = "*"
	opc = 3
	operacionActual.set(operacion)
	mostrando.set(resultado)

def divide(num):
	global operacion, resultado,opc
	if (resultado == 0 and opc == 0):
		resultado = float(num)
	elif(opc == 4):
		resultado /= float(num)
	else:
		elResultado()

	operacion = "/"
	opc = 4
	operacionActual.set(operacion)
	mostrando.set(resultado)

def elResultado():
	global operacion, resultado, opc

	if (opc == 1):
		resultado = sumar(resultado,mostrando.get())
		mostrando.set(resultado)
	elif (opc == 2):
		resultado = restar(resultado,mostrando.get())
		mostrando.set(resultado)
	elif (opc == 3):
		resultado = multiplicar(resultado,mostrando.get())
		mostrando.set(resultado)
	elif (opc == 4):
		resultado = dividir(resultado,mostrando.get())
		mostrando.set(resultado)



#-----------FILA 1----------------------

boton7=Button(frame, text="7",width=5, height=3, command=lambda:codigoBoton("7"))
boton7.grid(row=1, column=1)
boton8=Button(frame, text="8",width=5, height=3, command=lambda:codigoBoton("8"))
boton8.grid(row=1, column=2)
boton9=Button(frame, text="9",width=5, height=3, command=lambda:codigoBoton("9"))
boton9.grid(row=1, column=3)
botonDiv=Button(frame, text="/",width=5, height=3, command=lambda:divide(mostrando.get()))
botonDiv.grid(row=1, column=4)

#--------------FILA 2-------------------

boton4=Button(frame, text="4",width=5,height=3, command=lambda:codigoBoton("4"))
boton4.grid(row=2, column=1)
boton5=Button(frame, text="5",width=5,height=3, command=lambda:codigoBoton("5"))
boton5.grid(row=2, column=2)
boton6=Button(frame, text="6",width=5,height=3, command=lambda:codigoBoton("6"))
boton6.grid(row=2, column=3)
botonMult=Button(frame, text="*",width=5,height=3, command=lambda:multiplica(mostrando.get()))
botonMult.grid(row=2, column=4)

#--------------FILA 3-------------------

boton1=Button(frame, text="1",width=5,height=3, command=lambda:codigoBoton("1"))
boton1.grid(row=3, column=1)
boton2=Button(frame, text="2",width=5,height=3, command=lambda:codigoBoton("2"))
boton2.grid(row=3, column=2)
boton3=Button(frame, text="3",width=5,height=3, command=lambda:codigoBoton("3"))
boton3.grid(row=3, column=3)
botonSum=Button(frame, text="+",width=5,height=3, command=lambda:suma(mostrando.get()))
botonSum.grid(row=3, column=4)

#--------------FILA 4-------------------

botonCom=Button(frame, text=".",width=5,height=3, command=lambda:codigoBoton("."))
botonCom.grid(row=4, column=1)
boton0=Button(frame, text="0",width=5,height=3, command=lambda:codigoBoton("0"))
boton0.grid(row=4, column=2)
botonIgual=Button(frame, text="=",width=5,height=3, command=lambda:elResultado())
botonIgual.grid(row=4, column=3)
botonRest=Button(frame, text="-",width=5,height=3, command=lambda:resta(mostrando.get()))
botonRest.grid(row=4, column=4)

#--------------FILA 5---------------------

botonCE=Button(frame, text="Clear",command=Clear,width=30,height=3)
botonCE.grid(row=5,column=1,columnspan=4)

root.mainloop()