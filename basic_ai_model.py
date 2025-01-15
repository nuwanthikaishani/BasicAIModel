import tensorflow as tf
import numpy as np
from tensorflow.keras import layers, models

# Generate synthetic data
data = np.array([[i] for i in range(10)])  # Numbers 0 to 9
labels = np.array([0 if i <= 5 else 1 for i in range(10)])  # 0 if <= 5, else 1

# Build the model
model = models.Sequential([
    layers.Dense(8, activation='relu', input_shape=(1,)),  # Input layer
    layers.Dense(1, activation='sigmoid')                 # Output layer
])

# Compile the model
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit(data, labels, epochs=20, verbose=0)  # Train silently for simplicity

# Test the model
test_data = np.array([[3], [7]])  # Test with two numbers: 3 and 7
predictions = model.predict(test_data)

# Output the results
for i, pred in enumerate(predictions):
    print(f"Input: {test_data[i][0]} - Predicted Category: {'<= 5' if pred < 0.5 else '> 5'}")
