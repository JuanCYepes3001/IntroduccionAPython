Algoritmo MaquinaDeAlimentos
	Definir tipoProducto Como Caracter
	Definir montoIngresado, precioProducto, vuelto, moneda Como Entero
	Escribir  "Elija producto: (A, B o C)"
	Leer tipoProducto
	Segun tipoProducto Hacer
		"A":
			precioProducto = 270
		"B":
			precioProducto = 340
		"C":
			precioProducto = 390
	FinSegun
	Escribir "IngreseMonedas"
	montoIngresado = 0
	Mientras montoIngresado < precioProducto Hacer
		
		Leer moneda
		montoIngresado = montoIngresado + moneda
	FinMientras
	vuelto = montoIngresado - precioProducto
	Escribir "Su vuelto es de:"
	Mientras  vuelto >= 100 Hacer
		Escribir "100"
		vuelto = vuelto - 100
	FinMientras
	Mientras  vuelto >= 50 Hacer
		Escribir "50"
		vuelto = vuelto - 50
	FinMientras
	Mientras  vuelto >= 10 Hacer
		Escribir "10"
		vuelto = vuelto - 10
	FinMientras
FinAlgoritmo
