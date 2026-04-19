data = [
    [2,8,3,0],
    [3,7,4,0],
    [1,9,2,0],
    [2,8,3,0],
    [6,5,7,1],
    [7,5,8,1],
    [5,5,7,1],
    [6,4,8,1]
]
w = [-0.3, 0.4, 0.2]
b = -0.1

learning_rate = 0.01
epochs = 1000  
def sigmoid(z):
    return 1 / (1 + (2.71828 ** (-z)))
for _ in range(epochs):
    for row in data:
        x = row[:3]
        y = row[3]

        z = w[0]*x[0] + w[1]*x[1] + w[2]*x[2] + b
        y_pred = sigmoid(z)

        error = y_pred - y

        for j in range(3):
            w[j] -= learning_rate * error * x[j]

        b -= learning_rate * error


def predict(x):
    z = w[0]*x[0] + w[1]*x[1] + w[2]*x[2] + b
    y_pred = sigmoid(z)
    return 1 if y_pred >= 0.5 else 0
test = [5,5,7]
result = predict(test)

print("Weights:", w)
print("Bias:", b)
print("Prediction:", "At Risk" if result==1 else "Healthy")