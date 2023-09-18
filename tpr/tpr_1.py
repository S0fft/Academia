import numpy as np

# Замените этот пример на вашу матрицу оценок экспертов
matrix = np.array([
    [5, 4, 3, 2, 1],
    [4, 3, 2, 1, 5],
    [3, 2, 1, 5, 4],
    [2, 1, 5, 4, 3],
    [1, 5, 4, 3, 2],
])

parameters_to_rank = [0, 1, 2, 3, 4]

def one_dimensional_scaling(matrix, parameters_to_rank):
    num_experts, num_parameters = matrix.shape

    # Создаем матрицу Z и матрицу P
    Z = np.zeros((num_parameters, num_parameters))
    P = np.zeros((num_parameters, num_parameters))

    for i in range(num_parameters):
        for j in range(num_parameters):
            if i != j:
                Z[i, j] = np.sum(matrix[:, i] > matrix[:, j])
                P[i, j] = np.sum(matrix[:, i] < matrix[:, j])

    parameter_importance = []

    for param in parameters_to_rank:
        sum_ratios = 0

        for i in range(num_parameters):
            for j in range(num_parameters):
                if i != j:
                    sum_ratios += (Z[i, j] - Z[j, i]) / (Z[i, j] + P[i, j])

        importance = sum_ratios / (num_parameters - 1)
        parameter_importance.append(importance)

    return parameter_importance

importance_scores = one_dimensional_scaling(matrix, parameters_to_rank)

for param, importance in zip(parameters_to_rank, importance_scores):
    print(f"Параметр {param + 1}: Відносна важливість = {importance:.2f}")
