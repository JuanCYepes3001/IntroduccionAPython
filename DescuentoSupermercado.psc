Algoritmo PromocionConDescuento
    Definir n, qP, totalP, totalD, i Como Entero
    Definir vP Como Real
    i = 1
    n = 3
    Escribir "¿Cuantos productos desea llevar?"
    Leer qP
    
    Mientras i <= qP  Hacer
        Escribir "Precio producto " , i, ": "
        Leer vP
        i = i + 1
        totalP = totalP + vP
        Si i <= n Entonces
            vP = vP * 0.2
            vP = redon(vP)
            totalD = totalD + vP
        FinSi
        
        Si i >= n y i <= n*2 Entonces
            vP= vP * 0.1
            vP = redon(vP)
            totalD = totalD + vP
        FinSi
        
        Si i >= n*2 y i <= n*3 Entonces
            vP = vP * 0.05
            vP = redon(vP)
            totalD = totalD + vP
        FinSi
        
        Si i >= n*3 Entonces
            vP = vP
            totalD = totalD + vP
        FinSi
        
    FinMientras
    
    Escribir "Total: " , totalP
    Escribir "Descuento: " , totalD
    Escribir "Por pagar: " , totalP - totalD
FinAlgoritmo