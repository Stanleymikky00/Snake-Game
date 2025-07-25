import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical

# 1 Load training and test data
X_train = np.load("X_train.npy")
X_test = np.load("X_test.npy")
y_train = np.load("y_train.npy")
y_test = np.load("y_test.npy")

# 2 encode the output labels (Up, Down, Left, Right)
y_train_cat = to_categorical(y_train, num_classes=4)
y_test_cat = to_categorical(y_test, num_classes=4)

# 3️ Building the model
model = Sequential([
    Dense(64, activation='relu', input_shape=(4,)),  # 4 input features
    Dense(32, activation='relu'),
    Dense(4, activation='softmax')  # 4 classes for directions
])

# 4️ Compiling the model
model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# 5 Train the model
model.fit(
    X_train, y_train_cat,
    epochs=30,
    batch_size=16,
    validation_data=(X_test, y_test_cat)
)

# 6️ Evaluating
loss, acc = model.evaluate(X_test, y_test_cat)
print(f"\n✅ Test accuracy: {acc:.2f}")

# 7️ Saving the model
model.save("snake_model.keras")
print("✅ Model saved as snake_model.keras")


#Sequential = simple feedforward neural network

#Dense = fully connected layers

#softmax = outputs probabilities for 4 directions

#categorical_crossentropy = good for multi-class classification

#to_categorical = turns [0, 1, 2, 3] into one-hot encoding

