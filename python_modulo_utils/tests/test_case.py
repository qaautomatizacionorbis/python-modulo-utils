import datetime
import random
from datetime import timedelta

class TestCases(object):
	"""Biblioteca de casos de prueba"""

	def __init__(self,Longitud):
		self.longitud = Longitud

	def decimal_igual_longitud(self):
		valor = "0."
		if self.longitud > 2:
			for x in range(1,self.longitud-1):
				valor = valor + str(x)
		return float(valor)
	
	def decimal_mayor_longitud(self):
		valor = "0."
		if self.longitud >2:
			for x in range(1,self.longitud):
				valor = valor + str(x)
		return float(valor)
		
	def valor_booleano(self):
		valor = False
		x = random.randint(0, 1)
		if x == 1:
			valor = True
		return valor
	
	def valor_fecha(self):
		valor = datetime.datetime.now()
		return valor.strftime("%x")
	
	def valor_hora(self):
		valor = datetime.datetime.now()
		return valor.strftime("%X")
		
	def fecha_futura(self):
		valor = datetime.datetime.now() + timedelta(days=1)
		return valor
		
	def fecha_pasada(self):
		dia = 1
		mes = 1
		ano = 1900
		valor = datetime.datetime(ano,mes,dia)
		return valor
	
	def numero_mayor_longitud(self):
		valor = "2"
		for x in range(1,self.longitud+2):
			valor = valor + "2"
		return int(valor)
		
	def numero_igual_longitud(self):
		valor = "2"
		for x in range(1,self.longitud+1):
			valor = valor + "2"
		return int(valor)

	def espacio_igual_longitud(self):
		valor = ""
		for x in range(1,self.longitud+1):
			valor = valor + " "
		return valor
		
	def espacio_mayor_longitud(self):
		valor = ""
		for x in range(1,self.longitud+2):
			valor = valor + " /"
		return valor
	
	def texto_igual_longitud(self):
		valor = ""
		for x in range(1,self.longitud+1):
			valor = valor + "B"
		return valor
	
	def texto_mayor_longitud(self):
		valor = ""
		for x in range(1,self.longitud+2):
			valor = valor + "U"
		return valor
	
	def caracteres_especiales_xml(self):
		valor = "$%&%&/%(=&(%)/$(&/%[]{}·─;:─{}[]~¬{\º···#####%/(%(&%·$·&%·/&($/·%$"
		return valor[:self.longitud]	

	def caracteres_matematicos(self):
		valor = "+-*/.%+-*//**.%+-*/.%+-*/.%+-*/.%+-*/.%+-*/.%+-*/.%+-*/.%/.%+-*/.%+-*/.%+-*/.%+-*/.%"
		return valor[:self.longitud]

	def caracteres_puntuacion(self):
		valor = ";.:.;.:.;.:.;.:.;.:.;.:.;.:.;.:.;.:.;.:.;.:.;.:.;.:.;.:.;.:.;.:.;.:.;.:.;.:."
		return valor[:self.longitud]	

	def agrupacion_parentesis(self):
		valor = "()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()"
		return valor[:self.longitud]

	def agrupacion_corchetes(self):
		valor = "[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]"
		return valor[:self.longitud]

	def agrupacion_llaves(self):
		valor = "{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}"
		return valor[:self.longitud]

	def agrupacion_interrogacion(self):
		valor = "¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?"
		return valor[:self.longitud]

	def agrupacion_exclamacion(self):
		valor = "¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!¡!"
		return valor[:self.longitud]

	def carcateres_agrupacion(self):
		valor = "{}[]()<>{}[]()<>{}[]()<>{}[]()<>{}[]()<>{}[]()<>{}[]()<>{}[]()<>{}[]()<>{}[]()<>{}[]()<>"
		return valor[:self.longitud]