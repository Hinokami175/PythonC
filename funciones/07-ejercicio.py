import time


def es_palindromo(texto):
    inicio = time.time()
    var = ""
    var2 = ""
    signos = [".", ",", ";", ":", "...", " ", "?", "¿", '""', "''"]
    time.sleep(1)
    for i in range(0, len(texto), 1):
        if texto[i] not in signos:
            var += texto[i]
    for j in range(len(texto)-1, -1, -1):
        if (texto[j]) not in signos:
            var2 += texto[j]
    fin = time.time()
    print(fin-inicio)
    if var.lower() == var2.lower():
        return True
    else:
        return False


print("amo la paloma es palindromo? ", es_palindromo("Amo la paloma"))
print("Hola mundo es palindromo? ", es_palindromo("Hola Mundo"))
print("ojo es? ", es_palindromo("Roma ni se conoce sin oro, ni se conoce sin amor"))
