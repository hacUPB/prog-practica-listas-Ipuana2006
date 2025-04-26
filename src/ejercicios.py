# Ejercicio 1: Suma de elementos en una lista de listas
def suma_matriz(matriz):
 fil = len(matriz)
 col = len(matriz[0])
 acumulador = 0
 for i in range(fil):      # indice de lass filas
    for j in range(col):  # indice de columnas
        acumulador += matriz[i][j]
 return acumulador


# Ejercicio 2: Encontrar el valor máximo en una matriz
def maximo_matriz(matriz):
    maximo = matriz[0][0]  # inicializacion del maximo, asigna el primer elemento de la matriz ala variable maximo porque nececitamos un valor inicial.
    for filas in matriz:  #recorre las filas, itera sobre cada fila de la matriz 
        for elemento in filas:  #recorre los elementos de la fila actual, tomara los valores de cada uno de los elemnetos y  itera en cada uno 
            if elemento > maximo: # verifica si el elemento actual es mayor, compara el elemento actual con el valor almacenado en maximo
                maximo = elemento #actualiza el valor del maximo con el elemento actual solo si se cumple la condición del if
    return maximo 

# Ejercicio 3: Verificar si un número es primo
def es_primo(n):
    """
    Recibe un número y devuelve True si es primo, False en caso contrario.
    Incluir el código aquí para determinar si un número es primo.
    """
    pass

# Ejercicio 4: Transponer una matriz
def transponer_matriz(matriz):
    """
    Recibe una lista de listas y devuelve la matriz transpuesta.
    Incluir el código aquí para transponer la matriz.
    """
    pass

# Ejercicio 5: Filtrar números pares
def filtrar_pares(lista):
    """
    Recibe una lista de números y devuelve una nueva lista con solo los números pares.
    Incluir el código aquí para filtrar los números pares.
    """
    pass

# Ejercicio 6: Contar la cantidad de palabras en una frase
def contar_palabras(frase):
    """
    Recibe una frase y devuelve el número de palabras.
    Incluir el código aquí para contar las palabras en la frase.
    """
    pass

# Ejercicio 7: Crear una tabla de multiplicar
def tabla_multiplicar(n):
    """
    Recibe un número y devuelve una lista con su tabla de multiplicar del 1 al 10.
    Incluir el código aquí para generar la tabla de multiplicar.
    """
    pass

# Ejercicio 8: Contar números negativos en una lista
def contar_negativos(lista):
    """
    Recibe una lista de números y devuelve la cantidad de números negativos.
    Incluir el código aquí para contar los números negativos en la lista.
    """
    pass

# Ejercicio 9: Determinar si una lista está ordenada
def lista_ordenada(lista):
    """
    Recibe una lista de números y devuelve True si está ordenada de menor a mayor.
    Incluir el código aquí para verificar si la lista está ordenada.
    """
    pass

# Ejercicio 10: Cifrar un texto con el cifrado César
def cifrado_cesar(texto, desplazamiento):
    """
    Recibe un texto y un desplazamiento, y devuelve el texto cifrado usando el cifrado César.
    Incluir el código aquí para cifrar el texto con el cifrado César.
    """
    pass


#Aquí comienza el progrma principal. No modifiques el código debajo de esta línea.
def main():
    lista = [[4,5,6],[6,7,8]]
    resultado = maximo_matriz(lista)
    print(f'El maximo es el numero: {resultado}')


if __name__ == "__main__":
    main()