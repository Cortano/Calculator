def sumar(op1,op2):
	op1 = float (op1)
	op2 = float (op2)
	resultado = op1+op2
	return resultado
	
def restar(op1,op2):
	op1 = float (op1)
	op2 = float (op2)
	resultado = op1-op2
	return resultado

def multiplicar(op1,op2):
	op1 = float (op1)
	op2 = float (op2)
	resultado = op1*op2
	return resultado

def  dividir(op1,op2):
	op1 = float (op1)
	op2 = float (op2)
	try:
		resultado = op1/op2
		return resultado
	except ZeroDivisionError:
		return "Math Error"
