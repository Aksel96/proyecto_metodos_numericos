TOLERANCIA = 1e-6  # Tolerancia del error de 4 decimales
MAX_ITERACIONES = 6  # Numero maximo de iteraciones de los metodos
MATRIZ_DEFECTO = [[4, 2, -1],
                  [-5, 5, 1],
                  [-2, -3, 4]]
VECTOR_DEFECTO = [7, 12, 15]
VALORES_INICIALES_DEF = [0, 0, 0]


def jacobi(matriz, vector_resultados, x0):
    # Obtener la dimensión del sistema
    n = len(vector_resultados)

    # Inicializar el vector solución con la aproximación inicial
    x = x0.copy()

    iteracion = 0

    while iteracion < MAX_ITERACIONES:
        # Almacenar la solución de la iteración anterior
        x_anterior = x.copy()

        # Actualizar cada componente de la solución utilizando el método de Jacobi
        for i in range(n):
            # Calcular la suma de las variables anteriores
            sigma = sum(matriz[i][j] * x_anterior[j] for j in range(n) if j != i)
            # Actualizar la variable actual utilizando la fórmula de Jacobi
            x[i] = (vector_resultados[i] - sigma) / matriz[i][i]

        errores_relativos = [abs((x[i] - x_anterior[i]) / x[i]) if x[i] != 0 else 0 for i in range(n)]
        error_relativo_max = max(errores_relativos)

        print(f"Iteración {iteracion + 1}:")
        print(f"x = {x[0]:.6f}, y = {x[1]:.6f}, z = {x[2]:.6f}")
        print(
            f"Error en x: {errores_relativos[0]:.6f} , Error en y: {errores_relativos[1]:.6f} , Error en z: {errores_relativos[2]:.6f} ")
        print("---------------------------------------------------------------------------------------------------")

        # Verificar si se alcanzó la convergencia (error relativo máximo menor que la tolerancia)
        if error_relativo_max < TOLERANCIA:
            print("Convergencia alcanzada.")
            break

        iteracion += 1

    return x


def gauss_jordan(matriz, resultados):  # Funcion gauss jordan
    filas, columnas = len(matriz), len(matriz[0])

    for i in range(filas):
        # Hacer que el elemento diagonal sea 1
        elem_diagonal = matriz[i][i]
        for j in range(columnas):
            matriz[i][j] /= elem_diagonal
        resultados[i] /= elem_diagonal

        # Hacer ceros en la columna actual (excepto en el elemento diagonal)
        for k in range(filas):
            if k != i:
                factor = matriz[k][i]
                for j in range(columnas):
                    matriz[k][j] -= factor * matriz[i][j]
                resultados[k] -= factor * resultados[i]

        print(f"Iteración {i + 1}:")
        imprimir_matriz(matriz, resultados)

    return resultados


def imprimir_matriz(matriz, resultados):  # Funcion que imprime la matriz con formato
    for i in range(len(matriz)):
        fila = [f"{coef:.2f}" for coef in matriz[i]]
        print(f"{fila} | {resultados[i]:.2f}")
    print("-" * 30)


# Función para calcular el porcentaje de error relativo entre elementos correspondientes de dos listas
def calculate_error(previous, current):
    errors = [abs((current[i] - previous[i]) / current[i]) * 100 if current[i] != 0 else 0 for i in range(len(current))]

    formatted_errors = [f'{error:.6f}' for error in errors]

    return formatted_errors


# Función que implementa el método de Gauss-Seidel para resolver un sistema de ecuaciones lineales
def gauss_seidel(matriz, vector_resultados, valores_iniciales):
    # Obtiene el número de variables
    n = len(vector_resultados)

    # Inicializa la solución actual con la suposición inicial
    x = valores_iniciales.copy()

    # Itera hasta la convergencia o se alcance el número máximo de iteraciones
    for iteration in range(MAX_ITERACIONES):
        x_new = x.copy()

        # Actualiza cada componente de la solución utilizando el método de Gauss-Seidel
        for i in range(n):
            # Calcula la suma de los productos de los coeficientes y los valores correspondientes en la solución actual
            sum_ax = sum(matriz[i][j] * x_new[j] for j in range(n) if j != i)

            # Actualiza el componente de la solución actual utilizando la fórmula de Gauss-Seidel
            x_new[i] = (vector_resultados[i] - sum_ax) / matriz[i][i]

        error = calculate_error(x, x_new)

        formatted_x = [f'{value:.6f}' for value in x_new]

        print(f"Iteración {iteration + 1}: \nx = {formatted_x[0]}, y = {formatted_x[1]}, z = {formatted_x[2]}")
        print(f"Error en x: {error[0]} , Error en y: {error[1]} , Error en z: {error[2]}")
        print("---------------------------------------------------------------------------------------------------")

        # Verifica si el error para todos los componentes está por debajo de la tolerancia especificada
        if all(float(err) < TOLERANCIA for err in error):
            break

        # Actualiza la solución actual para la próxima iteración
        x = x_new

    return x


def llenado_matriz(numFil=0):  # Funcion que llena la matriz y el vector de resultados
    matrizNDim = []
    vectorResultados = []
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
                opcion_matriz = input("Quieres usar la matriz y los valores iniciales por defecto? [S/ SI , N/ NO] ").upper()
                if opcion_matriz == "S":
                    print("La matriz original es:")
                    imprimir_matriz(MATRIZ_DEFECTO, VECTOR_DEFECTO)
                    solucion_defecto = gauss_seidel(MATRIZ_DEFECTO,VECTOR_DEFECTO,VALORES_INICIALES_DEF)
                    print("Solución final:")
                    formatted_solution = [f'{value:.6f}' for value in solucion_defecto]
                    print(f"x = {formatted_solution[0]}, y = {formatted_solution[1]}, z = {formatted_solution[2]}")
                else:
                    numero_filas = int(input("Introduce el numero de incognitas que tiene la matriz: "))
                    matriz, vector_resultados = llenado_matriz(numero_filas)
                    # Se llenan los valores iniciales
                    x0 = llenar_x0()
                    print("La matriz es:")
                    imprimir_matriz(matriz, vector_resultados)
                    solucion = gauss_seidel(matriz, vector_resultados, x0)
                    print("Solución final:")
                    formatted_solution = [f'{value:.6f}' for value in solucion]
                    print(f"x = {formatted_solution[0]}, y = {formatted_solution[1]}, z = {formatted_solution[2]}")
            case "b":  # Caso para jacobi
                print("Solucion de un sistema de ecuaciones por el metodo de Jacobi")
                opcion_matriz = input("Quieres usar la matriz por defecto? [S/ SI , N/ NO] ").upper()
                if opcion_matriz == "S":
                    print("La matriz original es:")
                    imprimir_matriz(MATRIZ_DEFECTO, VECTOR_DEFECTO)
                    solucion_jacobi_defecto = jacobi(MATRIZ_DEFECTO,VECTOR_DEFECTO,VALORES_INICIALES_DEF)
                    print(F"Solucion final: {solucion_jacobi_defecto}")
                else:
                    numero_filas = int(input("Introduce el numero de incognitas que tiene la matriz: "))
                    matriz, vector_resultados = llenado_matriz(numero_filas)
                    # Se dan los valore iniciales
                    x0 = llenar_x0()
                    print("La matriz es:")
                    imprimir_matriz(matriz, vector_resultados)
                    resultado = jacobi(matriz, vector_resultados, x0)
                    print(F"Solucion final: {resultado}")
            case "c":  # caso para gauss jordan
                print("Solucion de un sistema de ecuaciones por el metodo de Gauss-Jordan")
                opcion_matriz = input("Quieres usar la matriz por defecto? [S/ SI , N/ NO] ").upper()
                if opcion_matriz == "S":
                    print("La matriz original es:")
                    imprimir_matriz(MATRIZ_DEFECTO, VECTOR_DEFECTO)
                    resultado_defecto = gauss_jordan(MATRIZ_DEFECTO, VECTOR_DEFECTO)
                    print(
                        "El valor de las incognitas en orden es el siguiente: {}".format(resultado_defecto))
                else:
                    numero_filas = int(input("Introduce el numero de incognitas que tiene la matriz: "))
                    matriz, vector_resultados = llenado_matriz(numero_filas)
                    print("La matriz es:")
                    imprimir_matriz(matriz, vector_resultados)
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
