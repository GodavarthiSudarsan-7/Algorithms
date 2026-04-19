
data = [
    [2,8,3,-1],
    [3,7,4,-1],
    [1,9,2,-1],
    [2,8,3,-1],
    [6,5,7,1],
    [7,5,8,1],
    [5,5,7,1],
    [6,4,8,1]
]


w = [0.01, -0.01, 0.01]
b = 0.0

learning_rate = 0.001
lambda_param = 0.01
epochs = 2000


for _ in range(epochs):
    for row in data:
        x = row[:3]
        y = row[3]

        result = w[0]*x[0] + w[1]*x[1] + w[2]*x[2] + b

        if y * result >= 1:
            for j in range(3):
                w[j] -= learning_rate * (2 * lambda_param * w[j])
        else:
            for j in range(3):
                w[j] -= learning_rate * (2 * lambda_param * w[j] - y * x[j])
            b -= learning_rate * (-y)


def predict(x):
    result = w[0]*x[0] + w[1]*x[1] + w[2]*x[2] + b
    return 1 if result >= 0 else -1


test = [6,5,7]
pred = predict(test)

print("Prediction:", "At Risk" if pred==1 else "Healthy")