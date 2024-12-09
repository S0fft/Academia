import random


def activation_function(x):
    return 1 if x >= 0 else 0


def custom_function(x1, x2):
    return 1 if (not x1 and not x2) else 0


def train_perceptron(inputs, outputs, weights, bias, learning_rate, epochs):
    num_samples = len(inputs)
    num_features = len(inputs[0])

    for epoch in range(epochs):
        total_error = 0

        for i in range(num_samples):
            weighted_sum = bias
            for j in range(num_features):
                weighted_sum += inputs[i][j] * weights[j]

            prediction = activation_function(weighted_sum)

            error = outputs[i] - prediction
            total_error += abs(error)

            for j in range(num_features):
                weights[j] += learning_rate * error * inputs[i][j]
            bias += learning_rate * error

        print(f"Epoch {epoch + 1}, Total Error: {total_error}")
        if total_error == 0:
            break

    return bias


def main():
    random.seed()

    inputs = [
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ]

    outputs = [custom_function(x[0], x[1]) for x in inputs]

    weights = [random.uniform(-0.5, 0.5) for _ in range(2)]
    bias = random.uniform(-0.5, 0.5)
    learning_rate = 0.2
    epochs = 10

    print("Training data:")
    for i in range(len(inputs)):
        print(f"Input: {inputs[i]} -> Output: {outputs[i]}")

    bias = train_perceptron(inputs, outputs, weights, bias, learning_rate, epochs)

    print(f"Trained weights: {weights}, Bias: {bias}")
    print("Testing trained perceptron:")
    for input_vector in inputs:
        weighted_sum = bias
        for j in range(2):
            weighted_sum += weights[j] * input_vector[j]
        prediction = activation_function(weighted_sum)
        print(f"Input: {input_vector} -> Prediction: {prediction}")


if __name__ == "__main__":
    main()
