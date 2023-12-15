def invertir_numero(numero):
    invertido = 0
    for i in range(n, 0, -1):
        invertido *= 10
        invertido += numero % 10
        numero //= 10
    return invertido
menu = 0

while menu < 3:
    print("Programa para invertir numeros")
    print("Elija la opcion que desea realizar")
    print ("1. Invertir numero de 3 digitos exactos")
    print ("2. Invertir numero de n digitos ")
    print ("3. Salir del programa")
    menu = int(input(" "))
    if menu == 1:
        numero = int(input("Digite el numero que desea invertir: "))
        n = len(str(numero))
        if n < 3 :
            print ("El numero ingresado no es de 3 digitos")
        else : 
            invertido = invertir_numero(numero)
            print("El número invertido es:", invertido)
    if menu == 2:
        numero = int(input("Ingrese un número de n dígitos: "))
        n = len(str(numero))
        invertido = invertir_numero (numero)
        print("El número invertido es:", invertido)




