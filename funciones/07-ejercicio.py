def es_palindromo(texto):
    resultado = ""
    var = ""
    var2 = ""
    for i in range(0, len(texto), 1):
        if texto[i] != " ":
            var += texto[i]
    for j in range(len(texto)-1, -1, -1):
        if (texto[j]) != " ":
            var2 += texto[j]
    print(var)
    print(var2)
    if var.lower() == var2.lower():
        return True
    else:
        return False


print("amo la paloma es palindromo? ", es_palindromo("Amo la paloma"))
print("Hola mundo es palindromo? ", es_palindromo("Hola Mundo"))
print("ojo es? ", es_palindromo("Roma ni se conoce sin oro, ni se conoce sin amor"))
