n1 = int(input("Ingresa el primer numero"))
n2 = int(input("ingresa el segundo numero"))

# print(n1+n2)
suma = n1+n2
resta = n2-n1
multi = n1*n2
div = n1/n2

mensaje = f"""
para los numeros {n1} y {n2},
el resultado de la suma es{suma},
el resultado de la resta es {resta},
el resultado de la division es {div},
el resultado de la multiplicacion es {multi}
"""
print(mensaje)
