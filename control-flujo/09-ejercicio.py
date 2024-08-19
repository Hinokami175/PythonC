import math
print("Bienvenido a la calculadora del Dante")
print("Las operaciones Disponibles son: Suma, Resta, Multiplicacion, Division")
comando = ""
comandos = ["suma", "resta", "division", "multipl31icacion"]
numero = None
numero2 = None
res = None
mensaje = ""
while comando.lower() != "salir":
    if numero is None:
        while True:
            try:
                numero = float(input("Ingrese un primer Numero: "))
                break
            except ValueError:
                print("Por favor Ingrese un Valor Numerico")
###################################
    while True:
        comando = input("Ingrese una Operación: ").lower()
        if comando.isalpha():
            break
    if comando in comandos:
        #########################################
        while True:
            try:
                numero2 = float(input("Ingrese un Segundo Numero: "))
                break
            except ValueError:
                print("Por favor Ingrese un Valor Numerico")
            #######################################################

        if comando == "suma":
            res = numero + numero2
        elif comando == "resta":
            res = numero - numero2
        elif comando == "multiplicacion":
            res = numero * numero2

        if comando == "division":
            if numero2 != 0.0:
                res = numero / numero2
            else:
                mensaje = "Operación Invalida. No se Puede Dividir por Cero."

        if res is not None:
            mensaje = f"El Resultado de la operacion {
                comando}, entre los numeros {numero} y {numero2} es {res}."
            numero = res
        print(mensaje)
    else:
        print("Comando Invalido")
