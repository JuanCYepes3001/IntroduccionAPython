Algoritmo Evaluaciones
	Definir certamen1 , certamen2, certamen3, examen, promedioCertamenes Como Real
	Escribir "Ingrese la nota del primer certamen:"
	leer certamen1
	Escribir "Ingrese la nota del segundo certamen:"
	leer certamen2
	Si certamen1 < 2 o certamen2 < 2 Entonces
		Escribir "Reporobado"
	SiNo
		Si certamen1 > 9 Y certamen2 > 9 Entonces
			Escribir "Aprobado"
		SiNo
			EScribir "Ingrese la nota del tercer certamen"
			leer certamen3
			promedioCertamenes = (certamen1+certamen2+certamen3)/3
			Si promedioCertamenes >= 7 Entonces
				Escribir "Aprobado"
			SiNo
				Escribir "Ingrese la nota del examen"
				leer examen
				Si promedioCertamenes < 3 o examen < 5 Entonces
					Escribir "Reprobado"
				SiNo
					Escribir "Aprobado"
				FinSi
			FinSi
		FinSi
	FinSi
	
FinAlgoritmo
