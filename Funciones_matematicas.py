def sumar(op1,op2):

	op1 = float(op1)
	op2 = float(op2)
	resultado = op1+op2
	return detectar(resultado)
	
def restar(op1,op2):
	op1 = float(op1)
	op2 = float(op2)
	resultado = op1-op2
	return detectar(resultado)

def multiplicar(op1,op2):
	op1 = float(op1)
	op2 = float(op2)
	resultado = op1*op2
	return detectar(resultado)

def  dividir(op1,op2):
	op1 = float(op1)
	op2 = float(op2)
	try:
		resultado = op1/op2
		return detectar(resultado)
	except ZeroDivisionError:
		return "Math Error"

def detectar(num):
	flotante = float(num)
	entero = int(num)
	try:
		if (flotante%float(entero) != 0):
			return flotante
		else:
			return entero
	except ZeroDivisionError:
		return "Math Error"
