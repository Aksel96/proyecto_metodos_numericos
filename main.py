TOLERANCIA = 1e-6  # Tolerancia del error de 4 decimales
MAX_ITERACIONES = 6  # Numero maximo de iteraciones de los metodos


def jacobi(matriz, vector_resultados, x0):
    # Obtener la dimensión del sistema
    n = len(vector_resultados)

    # Inicializar el vector solución con la aproximación inicial
    x = x0.copy()

    # Inicializar la variable de iteración
    iteracion = 0

    # Iterar hasta alcanzar el número máximo de iteraciones
    while iteracion < MAX_ITERACIONES:
        # Almacenar la solución de la iteración anterior
        x_anterior = x.copy()

        # Actualizar cada componente de la solución utilizando el método de Jacobi
        for i in range(n):
            # Calcular la suma ponderada de las variables anteriores
            sigma = sum(matriz[i][j] * x_anterior[j] for j in range(n) if j != i)
            # Actualizar la variable actual utilizando la fórmula de Jacobi
            x[i] = (vector_resultados[i] - sigma) / matriz[i][i]

        # Calcular los errores relativos para cada variable
        errores_relativos = [abs((x[i] - x_anterior[i]) / x[i]) if x[i] != 0 else 0 for i in range(n)]
        # Calcular el máximo error relativo
        error_relativo_max = max(errores_relativos)

        # Imprimir información sobre la iteración actual
        print(f"Iteración {iteracion + 1}:")
        print(f"x = {x[0]:.6f}, y = {x[1]:.6f}, z = {x[2]:.6f}")
        print(
            f"Error en x: {errores_relativos[0]:.6f} , Error en y: {errores_relativos[1]:.6f} , Error en z: {errores_relativos[2]:.6f} ")
        print("---------------------------------------------------------------------------------------------------")

        # Verificar si se alcanzó la convergencia (error relativo máximo menor que la tolerancia)
        if error_relativo_max < TOLERANCIA:
            print("Convergencia alcanzada.")
            break

        # Incrementar la variable de iteración
        iteracion += 1

    # Devolver el vector solución
    return x


def gauss_jordan(matrizNDim, vectorResultados):  # Funcion del metodo de gauss jordan
    n = len(matrizNDim)  # Obtiene la dimensión de la matriz cuadrada

    # Fase de eliminación hacia adelante
    for p in range(n - 1):
        for j in range(p + 1, n):
            valor = -matrizNDim[j][p] / matrizNDim[p][p]

            # Actualiza la fila j de la matriz y el elemento correspondiente en el vector de resultados
            for i in range(n):
                matrizNDim[j][i] = valor * matrizNDim[p][i] + matrizNDim[j][i]
            vectorResultados[j] = valor * vectorResultados[p] + vectorResultados[j]

    x = [0] * n  # Inicializa la lista para almacenar la solución

    # Fase de sustitución hacia atrás para encontrar las soluciones del sistema
    for i in range(n - 1, -1, -1):
        suma = sum(matrizNDim[i][j] * x[j] for j in range(i, n))
        x[i] = (vectorResultados[i] - suma) / matrizNDim[i][i]  # Calcula la solución para la variable x[i]

    return list(x)  # Devuelve la lista de soluciones


# Función para calcular el porcentaje de error relativo entre elementos correspondientes de dos listas
def calculate_error(previous, current):
    # Calcula los errores utilizando una comprensión de listas
    errors = [abs((current[i] - previous[i]) / current[i]) * 100 if current[i] != 0 else 0 for i in range(len(current))]

    # Formatea los errores con seis decimales usando una comprensión de listas
    formatted_errors = [f'{error:.6f}' for error in errors]

    # Devuelve los errores formateados
    return formatted_errors


# Función que implementa el método de Gauss-Seidel para resolver un sistema de ecuaciones lineales
def gauss_seidel(matriz, vector_resultados, valores_iniciales):
    # Obtiene el número de ecuaciones/variables
    n = len(vector_resultados)

    # Inicializa la solución actual con la suposición inicial
    x = valores_iniciales.copy()

    # Itera hasta la convergencia o se alcance el número máximo de iteraciones
    for iteration in range(MAX_ITERACIONES):
        # Crea una copia de la solución actual para almacenar la nueva solución
        x_new = x.copy()

        # Actualiza cada componente de la solución utilizando el método de Gauss-Seidel
        for i in range(n):
            # Calcula la suma de los productos de los coeficientes y los valores correspondientes en la solución actual
            sum_ax = sum(matriz[i][j] * x_new[j] for j in range(n) if j != i)

            # Actualiza el componente de la solución actual utilizando la fórmula de Gauss-Seidel
            x_new[i] = (vector_resultados[i] - sum_ax) / matriz[i][i]

        # Calcula el error entre la solución actual y la anterior
        error = calculate_error(x, x_new)

        # Formatea la nueva solución con seis decimales utilizando una comprensión de listas
        formatted_x = [f'{value:.6f}' for value in x_new]

        # Imprime información de la iteración, incluyendo el número de iteración, la solución actual y el error
        print(f"Iteración {iteration + 1}: x = {formatted_x},\nError (%) = {error}")

        # Verifica si el error para todos los componentes está por debajo de la tolerancia especificada
        if all(float(err) < TOLERANCIA for err in error):
            # Si es así, rompe el bucle de iteración
            break

        # Actualiza la solución actual para la próxima iteración
        x = x_new

    # Devuelve la solución final
    return x


def llenado_matriz(numFil=0):  # Funcion que llena la matriz y el vector de resultados
    matrizNDim = []  # Matriz donde se iran agregando los renglones de la matriz
    vectorResultados = []  # Arreglo donde se agregara el vecto de resultados
    for i in range(numFil):
        valMatriz = []  # Temporal de que almacena los imputs del usuario
        if i == 0:
            print("----    Introduce los valores separados por un espacio")
            print("----    Ej: Si la ecuacion es 3x + 1y - 4z = 7, deberas colocar: \" 3 1 -4 7 \"")
        valUsuario = input("Valores de la Ecuacion {}: ".format(i + 1))
        valFila = valUsuario.split(" ")  # Se hace split al input del usuario para conseguir el valor de cada incognita
        for j in range(len(valFila)):
            valMatriz.append(int(valFila[j]))  # Llenamos la matriz temporal con el imput del usuario
        matrizNDim.append(valMatriz[0:-1])  # Agregagos en la matriz los elementos del primero al penultimo
        vectorResultados.append(valMatriz[-1])  # Agregamos al vector de resultados el ultimo valor de la matriz temp
    return matrizNDim, vectorResultados  # Retornamos la matriz llenada y el vector


def llenar_x0():
    val_x0 = []
    x0 = input("Dame los valores iniciales separados por un espacio: ")
    splic_xo = x0.split(" ")
    for i in range(len(splic_xo)):
        val_x0.append(int(splic_xo[i]))
    return val_x0


def menu_home():  # Funcion que pinta en la pantalla el menu de opciones
    print("\n\n----------------------------------------------------")
    print("\t\t\tMETODOS NUMERICOS")
    print("\tPARA RESOLVER SISTEMAS DE ECUACIONES")
    print("\n Menu de opciones:")
    print("a) Gauss - Seidel")
    print("b) Jacobi")
    print("c) Gauss - Jordan")
    print("s) Salir")
    print("----------------------------------------------------")


def elegir_opciones_menu():  # Funcion que retorna la opcion elegida por el usuario
    opcion = input("Escribe tu opcion:")
    while opcion != "a" and opcion != "b" and opcion != "c" and opcion != "s":
        print("\t¡Opcion no valida ingresela nuevamente!")
        opcion = input("Escribe tu opcion: ")
    return opcion


def main():
    salir = "N"
    while salir != "S":  # Mientras salir no sea SI, se ejecutara el porgrama en bucle
        menu_home()
        opcion = elegir_opciones_menu()

        match opcion:  # Usamos un switch para ejecutar el metodo con la opcion deseada
            case "a":  # Caso para el metodo de gauss seidel
                print("Solucion de un sistema de ecuaciones por el metodo de Gauss-Seidel")
                numero_filas = int(input("Introduce el numero de incognitas que tiene la matriz: "))
                matriz, vector_resultados = llenado_matriz(numero_filas)
                x0 = llenar_x0()
                solucion = gauss_seidel(matriz,vector_resultados,x0)
                print("Solución final:")
                formatted_solution = [f'{value:.6f}' for value in solucion]
                print(f"x = {formatted_solution[0]}, y = {formatted_solution[1]}, z = {formatted_solution[2]}")
            case "b":  # Caso para jacobi
                print("Solucion de un sistema de ecuaciones por el metodo de Jacobi")
                numero_filas = int(input("Introduce el numero de incognitas que tiene la matriz: "))
                matriz, vector_resultados = llenado_matriz(numero_filas)
                x0 = llenar_x0()
                resultado = jacobi(matriz, vector_resultados, x0)
                print(F"Solucion final: {resultado}")
            case "c":  # caso para gauss jordan
                print("Solucion de un sistema de ecuaciones por el metodo de Gauss-Jordan")
                numero_filas = int(input("Introduce el numero de incognitas que tiene la matriz: "))
                matriz, vector_resultados = llenado_matriz(numero_filas)
                resultado = gauss_jordan(matriz, vector_resultados)
                print("El valor de las incognitas en orden es el siguiente: {}".format(resultado))
            case "s":  # caso de salir del programa
                break
            case _:
                print("Error en la opcion")

        # Preguntamos al usuario si quiere seguir usando el programa
        print("¿Quieres salir del programa?")
        salir = input("SI [S] , NO [N]: ").upper()


if __name__ == '__main__':
    main()
    print("Saliendo del programa...")
