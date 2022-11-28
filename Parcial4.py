#Universidad del Valle de Guatemala
#Matematica Discreta I
#Seccion 10
#Catedratico Mario Castillo
#Segundo Semestre 2022
#Jose Daniel Gomez Cabrera 21429
#Actividad: Parcial Practico 4

import numpy as np


def main():
    print("\n--> Conjuntos (Obtener contraseña): ----\n")
    R = analyze_set(1, 100, ">")
    S = analyze_set(1, 100, "!=")
    print(f"R: {R}, S: {S}, Suma: {(R + S)}")
    print("\n--> Propiedades de una Relación: ----\n")
    print(relation_properties(
        [[0, 1, 2, 3], [0, 1, 3], [0, 2], [1, 2, 3], [0, 2, 3]]))
    print(relation_properties([[0, 1, 2, 3], [0, 1, 2], [1], [2, 3], [0, 3]]))
    print("\n--> Composición de Relaciones: ----\n")
    print(composition_of_relationShip(
        [[1], [1, 2], [0, 1, 2]], [[1], [0, 1, 2], [0]]))


def get_matrix(digraph: list):
    values = {}

    for i in digraph[0]:
        values[i] = []

    for i in range(len(values)):
        j = i + 1
        for elem in digraph[j]:
            values[i].append(elem)

    matrix = []
    for i in values:
        m = []
        for j in range(len(values)):
            m.append("1") if j in values[i] else m.append("0")
        matrix.append(m)

    return values, matrix


def get_product(matrix1: list, matrix2: list):
    matrix_product = []  
    for i in range(len(matrix1)):
        columns_to_sum = []
        for j in range(len(matrix1[i])):
            if matrix1[j][i] == "1":
                columns_to_sum.append(j)

        if len(columns_to_sum) > 1:  # Add requested numbers
            the_sum = {}
            for l in columns_to_sum:
                for k in range(len(matrix2[i])):
                    numero = int(matrix2[k][l])
                    the_sum[k] = numero if not k in the_sum else the_sum[k] + numero
                    if the_sum[k] > 1:
                        the_sum[k] = 1

            matrix_product.append([str(the_sum[i]) for i in the_sum])

        elif len(columns_to_sum) == 1:  # Copy
            matrix_product.append([str(matrix2[k][columns_to_sum[0]])
                                  for k in range(len(matrix2[i]))])

    return np.array(matrix_product).transpose()


def relation_properties(digraph: list):
    digraph_result = get_matrix(digraph)
    values = digraph_result[0]
    matrix = digraph_result[1]

    yes = []
    no = []
    yes.append("REFLEXIVA") if reflexiveVerification(
        values) else no.append("REFLEXIVA")
    yes.append("SIMETRICA") if symmetricVerification(
        matrix) else no.append("SIMETRICA")
    yes.append("ANTISIMETRICA") if antisymmetricVerification(
        matrix) else no.append("ANTISIMETRICA")
    yes.append("TRANSITIVA") if transitiveVerification(
        matrix) else no.append("TRANSITIVA")

    bits = []
    bits.append(1) if reflexiveVerification(values) else bits.append(0)
    bits.append(1) if symmetricVerification(matrix) else bits.append(0)
    bits.append(1) if antisymmetricVerification(matrix) else bits.append(0)
    bits.append(1) if transitiveVerification(matrix) else bits.append(0)

    return f"==> {digraph}\nLa Matriz P = {matrix} indica que la relación es:\nSI: {yes}\nNO: {no}\nLista Binaria: {bits}\n"


def reflexiveVerification(values: list):
    for i in values:
        if not i in values[i]:
            return False
    return True


def symmetricVerification(matrix: list):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i != j:
                if matrix[i][j] != matrix[j][i]:
                    return False
    return True


def antisymmetricVerification(matrix: list):
    matrix1 = np.array(matrix)
    matrix2 = np.array(matrix).transpose()

    count = 0
    for i in range(len(matrix1)):
        for j in range(len(matrix1[i])):
            if i != j:
                if matrix1[i][j] == matrix2[i][j]:
                    count += 1

    return True if count <= len(matrix) else False


def transitiveVerification(matrix: list):
    m_power_2 = get_product(matrix, matrix)
    matrix = np.array(matrix)

    check = matrix == m_power_2
    return check.all()


def composition_of_relationShip(digraph_r: list, digraph_s: list):
    res_digraph1 = get_matrix(digraph_r)
    res_digraph2 = get_matrix(digraph_s)

    matrix1 = res_digraph1[1]
    matrix2 = res_digraph2[1]

    product_r_to_s = get_product(matrix1, matrix2)
    edge_list_r_to_s = make_edge_list(product_r_to_s)

    product_s_to_r = get_product(matrix2, matrix1)
    edge_list_s_to_r = make_edge_list(product_s_to_r)

    results = "\n"
    results += f"R = {digraph_r},\nS = {digraph_s}\n"
    results += f"R ° S\n{product_r_to_s}\n-> Lista de aristas: {edge_list_r_to_s}\n\nS ° R\n{product_s_to_r}"
    return results + f"\n-> Lista de aristas: {edge_list_s_to_r}\n"


def make_edge_list(matrix: list):
    edge_list = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "1":
                edge_list.append([i, j])
    return edge_list


def analyze_set(start_set: int, finish_set: int, type_of_analyze: str):
    coincidences = 0
    for i in range(start_set, finish_set+1):
        for j in range(start_set, finish_set+1):
            if check_condition(i, j, type_of_analyze):
                coincidences += 1
    return coincidences


def check_condition(i: int, j: int, type_of_analyze: str):
    if type_of_analyze == ">":
        if i > j:
            return True
    if type_of_analyze == "!=":
        if i != j:
            return True
    return False


if __name__ == "__main__":
    main()
