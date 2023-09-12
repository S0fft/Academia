import numpy as np

matrix = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
])

parameters_to_rank = [0, 1, 2, 3, 4]


def one_dimensional_scaling(matrix, parameters_to_rank):
    num_experts, num_parameters = matrix.shape

    parameter_importance = []

    for param in parameters_to_rank:
        sum_ratios = 0

        for i in range(num_parameters):
            for j in range(num_parameters):
                sum_ratios += matrix[param, i] / matrix[param, j]

        importance = sum_ratios / (num_parameters * (num_parameters - 1))
        parameter_importance.append(importance)

    return parameter_importance


importance_scores = one_dimensional_scaling(matrix, parameters_to_rank)

for param, importance in zip(parameters_to_rank, importance_scores):
    print(f"Параметр {param + 1}: Относительная важность = {importance:.2f}")
