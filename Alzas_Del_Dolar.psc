Algoritmo Alzas_Del_Dolar
	Escribir "¿De que periodo de tiempo quiere ver el alza del dolar?"
	Leer d
	Escribir "Ingrese el precio del dolar  para cada uno de los ", d , " dias"
	Leer precioDolar
	mayorAlza = 0
	Para i = 2 hasta d Hacer
		Leer precioDolar
		Si (precioDolar - precioDolarAnterior) > mayorAlza Entonces
			mayorAlza = precioDolar - precioDolarAnterior
		FinSi
		precioDolarAnterior = precioDolar
	FinPara
	Si mayorAlza > 0 Entonces 
		taza = mayorAlza - precioDolarAnterior
		Escribir "La mayor alza fue de ", taza
	SiNo
		Escribir "No hubo alzas"
	FinSi
FinAlgoritmo
